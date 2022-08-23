import os
import glob
from typing import List

import numpy as np
import torch
from skimage.color import lab2rgb
import streamlit as st



def upload_st_files_local(uploaded_files: List[st.uploaded_file_manager.UploadedFile]):
    blobs_to_remove = [
        f"images_gray/*", 
        f"images_color/*",
        f"images_original/*"]
    globs = [glob.glob(blob_to_remove) for blob_to_remove in blobs_to_remove]
    for item in globs:
        for _file in item:
            os.remove(_file) 

    for uploaded_file in uploaded_files:
        with open(os.path.join("images_gray", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer()) 
