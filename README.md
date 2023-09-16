# Brain Tumor Segmentation with UNet and deployment with FastAPI

An efficient and user-friendly application for brain tumor segmentation in medical images using a U-Net model and deploying with FastAPI.

![Screenshot 2023-09-13 at 23 09 15](https://github.com/iitimii/Brain-Tumour-Segmentation-with-UNet/assets/106264110/1a9855bf-16f5-4a4a-85de-fc4f0c7bc6a7)

## Table of Contents

- [Overview](#overview)
- [MRI Image Types](#mri-image-types)
  - [T1-Weighted Images](#t1-weighted-images)
  - [T2-Weighted Images](#t2-weighted-images)
  - [FLAIR (Fluid-Attenuated Inversion Recovery) Images](#flair-fluid-attenuated-inversion-recovery-images)
  - [T1-Contrast-Enhanced (T1CE) Images](#t1-contrast-enhanced-t1ce-images)
- [Brain Tumor Types](#brain-tumor-types)
  - [Necrotic Tumors](#necrotic-tumors)
  - [Edema Tumors](#edema-tumors)
  - [Enhancing Tumors](#enhancing-tumors)
- [U-Net Model for Segmentation](#u-net-model-for-segmentation)
- [Prediction Using FLAIR and T1-CE Images](#prediction-using-flair-and-t1-ce-images)

## Overview

This Brain Tumor Segmentation project combines the power of deep learning with FastAPI to provide a robust, accessible, and highly accurate solution for brain tumor segmentation in medical images. It addresses different tumor types, including necrotic, edema, and enhancing tumors, and supports multiple MRI image types.

**Key Features:**

- Brain tumor segmentation in medical images.
- User-friendly web interface powered by FastAPI.
- Accurate segmentation of different tumor components.
- Utilizes a U-Net model for precise segmentation.

## MRI Image Types

Medical imaging plays a pivotal role in brain tumor diagnosis and segmentation. This project supports various MRI image types, each offering unique insights into brain structures and pathologies.

### T1-Weighted Images

**Characteristics:**

- T1-weighted images emphasize tissue density differences in the brain.
- Ideal for anatomical reference with CSF appearing dark, gray matter intermediate, and white matter bright.

**Clinical Significance:**

- Used for identifying structural abnormalities and assessing brain anatomy.

### T2-Weighted Images

**Characteristics:**

- T2-weighted images highlight tissue water content variations.
- CSF appears bright, gray matter intermediate, and white matter dark.

**Clinical Significance:**

- Effective for detecting water content-related abnormalities like edema and inflammation.

### FLAIR (Fluid-Attenuated Inversion Recovery) Images

**Characteristics:**

- FLAIR images suppress CSF signal, making it appear dark.
- Valuable for detecting lesions near CSF spaces.

**Clinical Significance:**

- Helpful for diagnosing conditions like multiple sclerosis and brain tumors.

### T1-Contrast-Enhanced (T1CE) Images

**Characteristics:**

- T1CE images follow contrast agent administration.
- Abnormal tissues take up the contrast agent, appearing bright.

**Clinical Significance:**

- Critical for identifying enhancing lesions, such as tumors and active inflammation areas.

## Brain Tumor Types

In brain tumor segmentation, it's essential to understand the different tumor types and their characteristics.

### Necrotic Tumors

**Characteristics:**

- Necrotic tumors exhibit tissue death areas within the tumor.
- Appear as dark, non-enhancing regions on medical imaging.

**Clinical Significance:**

- Accurate segmentation aids in treatment planning by identifying viable tumor tissue.

### Edema Tumors

**Characteristics:**

- Edema results in swelling of surrounding brain tissue.
- Manifests as regions of increased signal intensity, particularly on T2-weighted images.

**Clinical Significance:**

- Accurate segmentation helps plan surgery and minimize damage to healthy tissue.

### Enhancing Tumors

**Characteristics:**

- Enhancing tumors exhibit contrast uptake after contrast agent administration.
- Appear as bright, enhancing areas on post-contrast MRI scans.

**Clinical Significance:**

- Identifying enhancing regions is vital for treatment planning, as they represent actively growing tumor areas.

## U-Net Model for Segmentation

This Brain Tumor Segmentation project leverages a U-Net deep learning model for accurate tumor segmentation. The U-Net architecture is renowned for its effectiveness in medical image segmentation tasks.

**Key Highlights:**

- U-Net is used to generate precise segmentation masks for brain tumors.
- It is trained on labeled medical images to learn the distinctive features of tumor regions.

## Prediction Using FLAIR and T1-CE Images

For the tumor prediction process, the application utilizes FLAIR (Fluid-Attenuated Inversion Recovery) and T1-Contrast-Enhanced (T1CE) images, as they provide essential information about tumor characteristics.

**Workflow:**

- The U-Net model takes input in the form of FLAIR and T1-CE images.
- The model processes these images to create a tumor segmentation mask, highlighting tumor regions.
- The segmented results are displayed in the application, allowing medical professionals to visualize and analyze the tumor.

This approach leverages the unique characteristics of FLAIR and T1-CE images to enhance the accuracy of tumor prediction and segmentation, providing valuable insights for medical diagnosis and treatment planning.



- Clone the Repo
- Run this command in your terminal
- ```streamlit run app.py```
