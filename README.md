## Preparing for r3live

### Build

```bash
cd /your/catkin/workspace/src/
git clone https://github.com/h-wata/r3live_tools
cd /your/catkin/workspace/
catkin b r3live_tools
source devel/setup.bash
```

### camera calibration

[camera_calibration(ROS wiki)](http://wiki.ros.org/camera_calibration)

```bash
rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.04 image:=/image_color
```

### Record bag files for calibration

Get some Bag files that record `Image` and `Pointcloud2` topic for a few second.
Place your bag files for calibration in the `/path/to/r3live_tools/bags`.

### Create image and pcd files from bag file.

```bash
roslaunch r3live_tools bag_to_image_and_pcd.launch file_name:=__bag_file__.bag image_topic:=/camera/image_color
./scripts/rename_calib_files.py 0
# export ./calib/images/0.jpg and ./calib/pcds/0.pcd
```

Repeat for the number of bag files placed.

### Livox Lidar and camera calibration

[hku-mars/livox_camera_calib(Github)](https://github.com/hku-mars/livox_camera_calib)

Build `livox_camera_calib` according to the README.md in the link above.

Fix `common` and `camera` parameter in `multi_calib.yaml` by the command below.

```bash
rosed livox_camera_calib multi_calib.yaml
```

```yaml
# Data path. adjust them!
common: # <- Modify to your path.
    image_path:  "/path/to/r3live_tools/calib/images"
    pcd_path:  "/path/to/r3live_tools/calib/pcds"
    result_path:  "/path/to/r3live_tools/calib/extrinsic.txt"
    data_num: 3
# Camera Parameters. Adjust them!
camera: # <- Modify the parameters to those obtained in camera_calibration
    camera_matrix: [1704.1857 , 0.0,      886.5115,
                    0.0,     1719.5228,  467.9244,
                    0.0,     0.0,      1.0     ]
    dist_coeffs: [-0.0963, 0.0708, 0.0011, -0.0017, 0.000000]

# Calibration Parameters.!
calib:
    calib_config_file: "/path/to/livox_camera_calib/config/config_outdoor.yaml"
    use_rough_calib: true # set true if your initial_extrinsic is bad
```

Start calibration with the command below.

```bash
roslaunch livox_camera_calib multi_calib.launch
```

Run the calibration on several files, and if the image and point cloud fit well adopt the `extrinsic.txt`.

### Transpose extrinsic parameter

The rotation matrix in `extrinsic.txt` needs to be transposed.

```bash
./scripts/transpose_extrinsic_parameter.py
# Export
# camera_ext_R:
# array([ 0.00483695,  0.0733586 ,  0.997294  , -0.999731  , -0.022263  ,
#         0.00648639,  0.0226786 , -0.997057  ,  0.0732312 ])
# camera_ext_T:
# array([-0.35275 , -0.159217, -0.24572 ])
```

Copy the calculated parameters onto the `r3live/config/r3live_config.yaml` and modify the `camera` parameters to those obtained in camera_calibration.

### Please enjoy r3live!!

```
roslaunch r3live_tools r3live_bag.launch
```
