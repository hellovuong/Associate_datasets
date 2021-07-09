#!/bin/bash
rosbag record -b 0 /camera/accel/imu_info /camera/gyro/imu_info /camera/color/camera_info /camera/color/image_raw /camera/accel/sample /camera/gyro/sample
