# Car Insurance Car Rotation

### How to run 

on 177 server, the conda environment is:

`/home/wudi/anaconda2/envs/wudi/bin/python`

The bash shell for the Flask server is (e.g., using CUDA device=4, and listening to port=5003):

`CUDA_VISIBLE_DEVICES=4 FLASK_ENV=development FLASK_APP=interface_carInsurance_AAE.py flask run -p 5003`

(without using AAE)

`CUDA_VISIBLE_DEVICES=4 FLASK_ENV=development FLASK_APP=interface_carInsurance.py flask run -p 5003`
 
 
If you need to install your own environment, the following is the gist for
installation requirements:

#### Installation Requirements
- OS: Ubuntu 16.04 LTS 
- nvidia drivers v.384.130
- 4 x NVIDIA GeForce GTX 1080

- Python 3.6.9
- CUDA 9.0
- cuddn 7.4
- pytorch 1.1 (or +)
- GCC(G++): 4.9/5.3/5.4/7.3
- mmdet: 1.0.rc0+d3ca926  
(Or you can install the mmdet from the uploaded files. The newest mmdet 1.4+ has different API in calling mmcv.
Hence, we would recommend install the mmdet from the uploaded files using:
`python setup.py install`)


## Main script to run 
For local debug, the main file to run locally is:

`interface_AAE_local.py` (this one use AAE as a second step to refine the rotation)
or `interface_local.py` (this is the original implementation using Kaggle winning solution).

### Data pipeline

- Get `image_base64, fx, fy, cx, cy, ZRENDER, SCALE` from Flask service in terms of POST method.

- Get the camera intrinsics from the post method and transform the base64 image to RGB image.

- Save a temporary image in the `./upload_imgs`  folder.

- Get the result from Kaggle competition model and remove the temporary image.

- Refine using AAE for the car 3D information.

- return the result in terms of json.

### Configurations
 All the data and network configurations for the first stage are in the .config file:
 `config='/home/wudi/code/Kaggle_PKU_Baidu/configs/htc/htc_hrnetv2p_w48_20e_kaggle_pku_no_semantic_translation_wudi_car_insurance.py'` 

