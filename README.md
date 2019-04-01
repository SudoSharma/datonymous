# Datonymous AnonNet
#### De-identifing patient faces for facilitating protected health information (PHI) exchange among relevant stakeholders.

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
In order to replicate the AnonNet Jupyter Notebook, you'll need to install `fastai` and `PyTorch`. The best resource for this is [the following website](https://docs.fast.ai/). The actual Jupyter Notebook contains any other information you might need to fully replicate our approach to facial keypoint detection. Note that this is a transfer learning approach which utilizes a pretrained ResNet34 deep neural network model as the backbone to a custom Anon head which fine-tunes the overall network for our particular dataset. 

In order to run the `realtime_anon.py` script, you will need to install `dlib`, `cv2`, `imutils`, `sklearn`, and `numpy`. All of these except `cv2` are relatively easy to install. Please create a conda or virtualenv environment and install all dependencies using either conda or pip. You will need to install `cv2` using `$ pip install opencv-python`. Once this is done, simply clone this repository, and execute `python realtime_anon.py` to de-identify your face in real-time. 

## Datasets
While further instructions are included in the AnonNet Jupyter Notebook, for your reference, we developed AnonNet with the help of the "Helen" open source dataset available [at this location](http://www.ifp.illinois.edu/~vuongle2/helen/). In this dataset, you'll find 2330 high resolution images of faces with annotated key features, including eyes, eyebrows, nose, mouth, and jawline, of which, we only utilized the eyes, eyebrows, and mouth, since these are most important for patient identification. 

## Demo / Proof of Concept
In addition to `realtime_anon.py` we also have another proof-of-concept for an de-identifying on-demand service at the following [GitHub repository](https://github.com/jaasmaz/datanonyms-javascript).

## Acknowledgements
Thank you to the [School of AI](https://www.theschool.ai/) and [Accenture](https://www.accenture.com/us-en) for hosting this hackathon!