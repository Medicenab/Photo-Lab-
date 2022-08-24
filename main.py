import os
import glob
import time
import numpy as np
import streamlit as st
from PIL import Image
from pathlib import Path
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
from skimage.color import rgb2lab, lab2rgb

from utils import upload_st_files_local

import torch
from torch import nn, optim
from torchvision import transforms
from torchvision.utils import make_grid
from torch.utils.data import Dataset, DataLoader

from model import make_dataloaders, visualize_res
st.set_page_config(
    page_title="Photo Lab",
    page_icon="random",
)

st.title("Photo Lab ✨📸")
st.text('Bring old Pictures Back to Life!')
uploaded_files = st.file_uploader("Upload a B&W picture", accept_multiple_files=True)
upload_st_files_local(uploaded_files)



data='images_gray'
modelo="models/model_GAN_100epochs.pth"

if uploaded_files:
    color=st.button('Click me')
    if color:
        
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success('Done!')
        path_result = glob.glob(data + "/*.jpg")
        res_dl = make_dataloaders(paths=path_result, split='val')
        data_res = next(iter(res_dl))
        Ls, abs_ = data_res['L'], data_res['ab']
        files_lenght=(len(path_result))
        visualize_res(modelo,data_res,files_lenght)

        for x in range(files_lenght):
            images = [f"images_original/input_{x}.png",
            f"images_color/colorization_{x}.png"]
            st.image(images, caption=["B&W", "Color"])
            with open(f"images_color/colorization_{x}.png", "rb") as file:
                st.download_button(label = "Descarga", data = file, file_name=f"colorized {x}.png",mime="image/png")

