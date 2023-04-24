# Segmentation of renal structures

Repository for paper
```
Segmentation of renal structures based on contrast
computed tomography scans using a convolutional
neural network
```

**Aim**. Develop a neural network to build 3D models of kidney neoplasms and adjacent structures.
**Materials and methods**. DICOM data (Digital Imaging and Communications in Medicine standard) from 41 patients with kidney
neoplasms were used. Data included all phases of contrast-enhanced multispiral computed tomography. We split the data: 32
observations for the training set and 9 – for the validation set. At the labeling stage, the arterial, venous, and excretory phases
were taken, affine registration was performed to jointly match the location of the kidneys, and noise was removed using a
median filter and a non-local means filter. Then the masks of arteries, veins, ureters, kidney parenchyma and kidney neoplasms
were marked. The model was the SegResNet architecture. To assess the quality of segmentation, the Dice score was compared
with the AHNet, nnU-Net models and with three variants of the nnUnet (lowres, fullres, cascade) model.
**Results**. On the validation subset, the values of the Dice score of the SegResNet architecture were: 0.89 for the normal
parenchyma of the kidney, 0.58 for the kidney neoplasms, 0.86 for arteries, 0.80 for veins, 0.80 for ureters. The mean values
of the Dice score for SegResNet, AHNet and nnUnet were 0.79; 0.67; and 0.75, respectively. When compared with the nn-
UNet model, the Dice score was greater for the kidney parenchyma in SegResNet – 0.89 compared to three model variants:
lowres – 0.69, fullres – 0.70, cascade – 0.69. At the same time, for the neoplasms of the parenchyma of the kidney, the Dice
score was comparable: for SegResNet – 0.58, for nnUnet fullres – 0.59; lowres and cascade had lower Dice score of 0.37
and 0.45, respectively.
**Conclusion**. The resulting SegResNet neural network finds vessels and parenchyma well. Kidney neoplasms are more
difficult to determine, possibly due to their small size and the presence of false alarms in the network. It is planned to increase
the sample size to 300 observations and use post-processing operations to improve the model

For more information about this work, please read the following paper:
```
Chernenkiy I.М., Chernenkiy M.M., Fiev D.N., Sirota E.S. Segmentation of renal structures based on contrast
computed tomography scans using a convolutional neural network. Sechenov Medical Journal. 2023; 14(1): 45–55.
https://doi.org/10.47093/2218-7332.2023.14.1.45-55
```

# Usage

`Evaluate.ipynb` - downloads and creates masks for CT data based on three phases.
`EvalnnUnetForPaper.ipynb` - Uses nnUnet as baseline.
`MeasureMetrics.ipynb` - Calculates metrics.
