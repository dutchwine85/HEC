import shutil
from pathlib import Path

shutil.rmtree("/Users/tomweston/PycharmProjects/HEC/z_img_output/")

Path("/Users/tomweston/PycharmProjects/HEC/z_img_output").mkdir(parents=True, exist_ok=True)

shutil.rmtree("/Users/tomweston/PycharmProjects/HEC/z_img_chosen/")

Path("/Users/tomweston/PycharmProjects/HEC/z_img_chosen").mkdir(parents=True, exist_ok=True)