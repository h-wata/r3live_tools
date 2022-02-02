#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""Export transpose extrinsic parameter from extrinsic.txt."""

import pprint

import numpy as np
import rospkg

ROOT_DIR = rospkg.RosPack().get_path('r3live_tools')
print(ROOT_DIR)
ext_file = ROOT_DIR + "/calib/extrinsic.txt"

ext = np.loadtxt(ext_file, delimiter=',', unpack=False, max_rows=3)
print("extrinsic.txt:")
print(ext)
ext = np.hsplit(ext, [3])

ext_r = ext[0].transpose().flatten()
ext_t = ext[1].transpose().flatten()
print("\n***************************")
print("Please copy to r3live config file")
print("***************************\n")
print("camera_ext_R: ")
pprint.pprint(ext_r)
print("camera_ext_T: ")
pprint.pprint(ext_t)
