# Datonymous AnonNet
### De-identifing patient faces for facilitating protected health information (PHI) exchange among relevant stakeholders.

## Team Members
- Abhi Sharma
- Jasim Alazzawi
- Josh Matz
- Prathamesh Prabhudesai

## Abstract
This repository contains an implementation of AnonNet, our submission to the School of AI Hackathon on March 31st, 2019. AnonNet detects key identifying features on a person's face, i.e., the eyes, eyebrows, and mouth. Using this information, accurate pixelation and/or censor bar placement can de-identify an individual. This has several benefits, including but not limited to:
- Reducing the risk of protected patient information from being leaked
- Reducing the administrative burden of manually de-identifying patient information
- Increasing the availability and access to anonymized information, leading to innovation in the Healthcare space

## Instructions to Reproduce
In order to replicate the AnonNet Jupyter Notebook, you'll need to install `fastai` and `PyTorch`. The best resource for this is [the following website](https://docs.fast.ai/). 

In order to run the `realtime_anon.py` script, you will need to install `dlib`, `cv2`, `imutils`, `sklearn`, and `numpy`. All of these except `cv2` are relatively easy to install. Please create a conda or virtualenv environment and install all dependencies using either conda or pip. You will need to install `cv2` using `$ pip install opencv-python`. 