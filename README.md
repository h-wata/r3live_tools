## Setup for r3live

### camera calibration

```
$ rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.04 image:=/image_color
```

### Record bag files for calibration
数秒のImageとPointcloudを記録したBagファイルを取得します。

`r3live_tools/bags`にBagファイルを置きます。

### Create image and pcd files from bag file.

```
$ roslaunch r3live_tools bag_to_image_and_pcd.launch file_name:=calib-0.bag
$ ./scripts/rename_calib_files.py 0
# export ./calib/images/0.jpg and ./calib/pcds/0.pcd
```
取得したBagファイルの分上記を繰り返します。

### livox_camera_calib

下記を実行し`common`のファイルパスと `camera`のパラメータを修正します。
```bash
$ rosed livox_camera_calib multi_calib.yaml
```

```bash
$ roslaunch livox_camera_calib multi_calib.launch
```

いくつかのファイルでキャリブレーションを実行して、うまく導出されたところで`extrinsic.txt`を採用する。

### Transpose extrinsic parameter

導出された`extrinsic.txt`を転置する必要があるので下記のコマンドを実行する。
```
$ ./scripts/transpose_extrinsic_parameter.py
```
算出された`camera_ext_R`と`camera_ext_T`のパラメータを`r3live/config/r3live_config.yaml`に転記する。

