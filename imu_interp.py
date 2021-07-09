#!/urs/bin/env python2

import numpy as np
import matplotlib.pyplot as plt

d400_gyro_x = []
d400_gyro_y = []
d400_gyro_z = []
d400_gyro_t = []

d400_accel_x = []
d400_accel_y = []
d400_accel_z = []
d400_accel_t = []

with open('accel.txt', 'r') as accel_in:
    for line in accel_in:
        if line[0] == '#':
            continue
        contents = line.split(',')
        d400_accel_t.append(np.int_(contents[0]))
        d400_accel_x.append(np.float64(contents[1]))
        d400_accel_y.append(np.float64(contents[2]))
        d400_accel_z.append(np.float64(contents[3]))

with open('gyro.txt', 'r') as gyro_in:
    for line in gyro_in:
        if line[0] == '#':
            continue
        contents = line.split(',')
        d400_gyro_t.append(np.int_(contents[0]))
        d400_gyro_x.append(np.float64(contents[1]))
        d400_gyro_y.append(np.float64(contents[2]))
        d400_gyro_z.append(np.float64(contents[3]))
    
# linear interpolate    

d400_accel_x_interp = np.interp(d400_gyro_t, d400_accel_t, d400_accel_x)
d400_accel_y_interp = np.interp(d400_gyro_t, d400_accel_t, d400_accel_y)
d400_accel_z_interp = np.interp(d400_gyro_t, d400_accel_t, d400_accel_z)

d400_gyro_x_interp = np.interp(d400_accel_t, d400_gyro_t, d400_gyro_x)
d400_gyro_y_interp = np.interp(d400_accel_t, d400_gyro_t, d400_gyro_y)
d400_gyro_z_interp = np.interp(d400_accel_t, d400_gyro_t, d400_gyro_z)
with open('imu.txt', 'w') as outfile:
    outfile.write('#timestamp [s],w_RS_S_x [rad s^-1],w_RS_S_y [rad s^-1],w_RS_S_z [rad s^-1],a_RS_S_x [m s^-2],a_RS_S_y [m s^-2],a_RS_S_z [m s^-2]\n')
    for i, time in enumerate(d400_gyro_t):
        outfile.write(str(time) + ',' + str(d400_gyro_x[i]) + ',' + str(d400_gyro_y[i]) + ',' + str(d400_gyro_z[i]) + ',' + str(d400_accel_x_interp[i]) + ',' + str(d400_accel_y_interp[i])+ ',' + str(d400_accel_z_interp[i]) + '\n')
outfile.close()
# with open('gyro_interp.txt', 'w') as out_file:
#     out_file.write('#timestamp [s],w_RS_S_x [rad s^-1],w_RS_S_y [rad s^-1],w_RS_S_z [rad s^-1],a_RS_S_x [m s^-2],a_RS_S_y [m s^-2],a_RS_S_z [m s^-2]\n')
#     for i, time in enumerate(d400_accel_t):
#         out_file.write(str(time) + ',' + str(d400_gyro_x_interp[i]) + ',' + str(d400_gyro_y_interp[i]) + ',' + str(d400_gyro_z_interp[i]) + '\n')
# out_file.close()
# with open('accel_interp.txt','w') as outfile:
#     for i, time in enumerate(d400_gyro_t):
#         outfile.write(str(time) + ',' + str(d400_accel_x_interp[i]) + ',' + str(d400_accel_y_interp[i])+ ',' + str(d400_accel_z_interp[i]) + '\n')

plot1 = plt.figure(1)
plt.plot(d400_accel_t, d400_accel_x, '.', label = 'd400_accel_x')
plt.plot(d400_gyro_t, d400_accel_x_interp, '-', label ='d400_accel_x_interp')
plt.title("d400_accel_x")
plt.legend() 

plot2 = plt.figure(2)
plt.plot(d400_accel_t, d400_accel_y, '.', label = 'd400_accel_y')
plt.plot(d400_gyro_t, d400_accel_y_interp, '-', label ='d400_accel_y_interp')
plt.title("d400_accel_y")
plt.legend() 

plot3 = plt.figure(3)
plt.plot(d400_accel_t, d400_accel_z, '.', label = 'd400_gyro_z')
plt.plot(d400_gyro_t, d400_accel_z_interp, '-', label ='d400_accel_z_interp')
plt.title("d400_accel_z")
plt.legend() 

plt.show()