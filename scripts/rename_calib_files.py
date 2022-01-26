#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import shutil
import os
import glob
import sys

""" rename image and pcd files for livox_camera_calib

python rename_calib_files.py (int N)
example:
    $python rename_calib_files.py 0
    # export calib/images/0.jpg and calib/pcds/0.pcd
"""


def remove_glob(pathname):
    for p in glob.glob(pathname):
        os.remove(p)


ROOT_DIR = os.path.abspath(os.pardir)
image_dir = ROOT_DIR + "/calib/images"
pcd_dir = ROOT_DIR + "/calib/pcds"

shutil.move(image_dir + 'frame0.jpg', image_dir + sys.argv[1] + ".jpg")

pcd_files_list = glob.glob(pcd_dir + "out_*.pcd")
shutil.move(pcd_files_list[0], pcd_dir + sys.argv[1] + ".pcd")

remove_glob(pcd_dir + "out_*.pcd")
remove_glob(image_dir + "frame*.jpg")
