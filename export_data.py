#!/usr/bin/env python2
"""
merge accel and gyro message into one IMU topic in the given bag
"""
import rosbag
import sys
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry

export_odom = False
export_times_left = False
export_times_right = False
export_times_color = True
export_accel = True
export_gyro = True
def main():
    files = ['room.bag']
    i=0
    for file in files:
        
        odom_t = []
        img_t = []
        img_right_t = []
        odom = []
        accel = []
        accel_t = []
        gyro = []
        gyro_t = []
        img_color_t = []
        
        with rosbag.Bag(file) as inbag:
                print ("-------------------- Input: %s ------------------------------" % file)
                print (inbag)
                for topic,msg,t in inbag.read_messages():
                    if export_odom:
                        if topic == "/odom":
                            odom_t.append(t)
                            odom.append(msg)
                    if export_times_left:
                        if topic == "/camera/infra1/image_rect_raw":
                            img_t.append(t)
                    if export_times_right:
                        if topic == "/camera/infra2/image_rect_raw":
                            img_right_t.append(t)
                    if export_times_color:
                        if topic == "/camera/color/image_raw":
                            img_color_t.append(t)
                    if export_gyro:
                        if topic == "/camera/gyro/sample":
                            gyro.append(msg)
                            gyro_t.append(t)
                    if export_accel:
                        if topic == "/camera/accel/sample":
                            accel.append(msg)
                            accel_t.append(t)
        if export_odom:
            with open('odom.txt', 'w') as outfile:
                outfile.write('timestamps x y z q_x q_y q_z q_w' + '\n')
                for odo, t in zip(odom, odom_t):

                    x = odo.pose.pose.position.x
                    y = odo.pose.pose.position.y
                    z = odo.pose.pose.position.z

                    q_x = odo.pose.pose.orientation.x
                    q_y = odo.pose.pose.orientation.y
                    q_z = odo.pose.pose.orientation.z
                    q_w = odo.pose.pose.orientation.w

                    outfile.write(str(t.to_nsec()) + ' ' + str(x) + ' ' + str(y) + ' ' + str(z) +' '+ str(q_x) + ' ' + str(q_y) + ' ' + str(q_z) +' ' + str(q_w) +'\n')
        if export_times_left:
            with open('times_left.txt', 'w') as outfile:
                for t in img_t:
                    outfile.write(str(t.to_nsec()) + '\n')
        if export_times_color:
            with open('times_color.txt', 'w') as outfile:
                for t in img_color_t:
                    outfile.write(str(t.to_nsec()) + '\n')

        if export_times_right:
            with open('times_right.txt', 'w') as outfile:
                for t in img_right_t:
                    outfile.write(str(t.to_nsec()) + '\n')
        if export_accel:
            with open('accel.txt', 'w') as outfile:
                outfile.write('#timestamp [ns],a_RS_S_x [m s^-2],a_RS_S_y [m s^-2],a_RS_S_z [m s^-2]'+'\n')
                for inertial, t in zip(accel, accel_t):

                    a_x = inertial.linear_acceleration.x
                    a_y = inertial.linear_acceleration.y
                    a_z = inertial.linear_acceleration.z
                    outfile.write(str(t.to_nsec()) + ',' + str(a_x) + ',' + str(a_y) + ',' + str(a_z) + '\n')
        if export_gyro:
            with open('gyro.txt', 'w') as outfile:
                outfile.write('#timestamp [ns],w_RS_S_x [rad s^-1],w_RS_S_y [rad s^-1],w_RS_S_z [rad s^-1]'+'\n')
                for inertial, t in zip(gyro, gyro_t):
                    
                    w_x = inertial.angular_velocity.x
                    w_y = inertial.angular_velocity.y
                    w_z = inertial.angular_velocity.z

                    outfile.write(str(t.to_nsec()) + ',' + str(w_x) + ',' + str(w_y) + ',' + str(w_z) + '\n')

        outfile.close()
        
if __name__ == '__main__':
    main()
