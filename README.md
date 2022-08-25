# captchas_solution
to recognize the letters in a captchas image

## Requirements
- Ubuntu18
- Anaconda or similar tool
- Python3

## Folder Structure
├── create_model.py  
├── example  
│   ├── images  
│   │   ├── input00.png  
│   │   ├── input01.png  
...  
│   │   └── input24.png  
│   ├── model.pkl  
│   └── result.txt  
├── predict_captchas.py  
└── README.md  

- create_model.py is the first step to generate a model or letter dictionary for inference later.
- example folder is the output sample generated from this solution including the letter dictionary saved in model.pkl, letter visualization result in images folder and result.txt is the required output format of this task.
- predict_captchas.py is the second step of this solution to predict an unknown captchas image.

## Docs
This README.md is the documentation of this solution.

## Getting Started
If you are using Anaconda, you may follow the steps below.  
Please change the obsolute path accordingly based on your system path.  
cd /home/ccng/workspace/captchas_solution  
conda create -n python37 python=3.7  
conda activate python37  
pip install numpy opencv-python matplotlib  

### Step 1: Model Generation
python create_model.py

### Step 2: Model Prediction
python predict_captchas.py
 
