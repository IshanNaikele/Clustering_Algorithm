import os 
from dotenv import load_dotenv

import kagglehub

load_dotenv()

download_path="./Dataset"
dataset_handle = "shwetabh123/mall-customers"

path=kagglehub.dataset_download(dataset_handle,output_dir=download_path)

if path and os.path.exists(path) :
    print(f"Dataset Downloaded : {dataset_handle}")
    files=os.listdir(path)
    print(f"Files present in Dataset {dataset_handle} : {files}")
else :
    print("Dataset Download failed or path is wrong or file name is wrong ")
