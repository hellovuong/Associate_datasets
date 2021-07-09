# Associate_datasets
This repo is used to record datasets from Realsense camera in rosbag format and parsing it to EuRoC format

### Usage
1. Run commands inside repo folder:
```
chmod +x record_color.sh
./record_color.sh
```
This will start record datasets. If you want to record other topic, change/add topic inside script.

2. Convert image topic to image files:
```
mkdir color
python bag_to_images.py example.bag ./color /camera/color/image_raw
```
Where ```example.bag``` is name of your rosbag file. If you are using stereo or different topic image, specify it as your need.

3. Parsing IMU data and image timestamps:
```
python export_data.py
```
You need to change rosbag file name inside the script. The output will include 3 file: ```times_color.txt```, ```accel.txt```, ```gyro.txt```, which are image timestamp, accel/gyro data, respectively

4. Interpolate IMU data:
```
python imu_interp.py
```
The script interpolates accel data base on gyro timestamps and write it into ```imu.txt```.

Now, you have your dataset under EuRoC format. I attached an example Mono+Inertial of ORB_SLAM3 to work with your new datasets.
