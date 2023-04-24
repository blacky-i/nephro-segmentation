import numpy as np
from monai.transforms.transform import MapTransform
from monai.transforms import InvertibleTransform

class ReplaceImages(MapTransform, InvertibleTransform):
    def __init__(self, keys_merge, keys_out, allow_missing_keys=True):
        self.keys_merge = keys_merge
        self.keys_out = keys_out
        self.key_target_meta = keys_merge + '_meta_dict'
        self.allow_missing_keys = allow_missing_keys
    def __call__(self, data):
        
        data[self.keys_out] = data[self.keys_merge]
        data[self.keys_out + '_meta_dict'] = data[self.key_target_meta]
        return data
    def inverse(self, data):
        data[self.keys_merge] = data[self.keys_out]
        data[self.keys_merge + '_meta_dict'] = data[self.keys_merge + '_meta_dict']
        return data

class ConcatImages(MapTransform, InvertibleTransform):
    def __init__(self, keys_merge, keys_out,  allow_missing_keys=True):
        self.keys_merge = keys_merge
        self.keys_out = keys_out
        self.key_target_meta = keys_merge[0] + '_meta_dict'
        self.allow_missing_keys = allow_missing_keys
    def __call__(self, data):
        
        if isinstance(data, list):
            for data_row in data:
                data_row[self.keys_out] = np.concatenate([data_row[key] for key in self.keys_merge])
                data_row[self.keys_out + '_meta_dict'] = data_row[self.key_target_meta]
                
                #print('row-',data_row[self.keys_out].shape)
        else:
            data[self.keys_out] = np.concatenate([data[key] for key in self.keys_merge])
            data[self.keys_out + '_meta_dict'] = data[self.key_target_meta]
            #print('dict-',data[self.keys_out].shape)
        return data
    def inverse(self, data):
#         if isinstance(data, list):
#             for data_row in data:
#                 print(data_row.keys())
#                 for idx, key in enumerate(self.keys_merge):
#                     data_row[key] = data_row[self.keys_out][idx]
#         else:
        print(data.keys())
#             out = np.split(data[self.keys_out], axis=0)
#             for idx, key in enumerate(self.keys_merge):
#                 data[key] = data[self.keys_out][idx]
#         data[self.keys_merge] = data[self.keys_out]
#         data[self.keys_merge + '_meta_dict'] = data[self.keys_merge + '_meta_dict']
        return data