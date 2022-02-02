#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""rename image and pcd files for livox_camera_calib.

python rename_calib_files.py (int N)
example:
    $python rename_calib_files.py 0
    # export calib/images/0.jpg and calib/pcds/0.pcd
"""

import glob
import os
import shutil
import sys

import rospkg


def remove_glob(pathname):
    # type:(str) -> None
    """Remove files searched by glob."""
    for p in glob.glob(pathname):
        os.remove(p)


def find_glob(pathname):
    # type:(str) -> list
    """Find files by glob."""
    files = glob.glob(pathname)
    if len(files) > 0:
        return files
    else:
        print("Error: " + pathname + " is not found")
        exit()


if len(sys.argv) < 2:
    print("Error: this script requires an argument.")
    exit()

ROOT_DIR = rospkg.RosPack().get_path('r3live_tools')
print(ROOT_DIR)
image_dir = ROOT_DIR + "/calib/images/"
pcd_dir = ROOT_DIR + "/calib/pcds/"

image_files = find_glob(image_dir + 'frame*.jpg')
shutil.move(image_files[0], image_dir + sys.argv[1] + ".jpg")

pcd_files = find_glob(pcd_dir + "out_*.pcd")
shutil.move(pcd_files[0], pcd_dir + sys.argv[1] + ".pcd")

remove_glob(pcd_dir + "out_*.pcd")
remove_glob(image_dir + "frame*.jpg")
