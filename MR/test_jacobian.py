import modern_robotics as mr
import numpy as np
import math

L1 = 0.29
L2 = 0.27
L3 = 0.07
L4 = 0.302
L5 = 0.072
L6 = 0    #may be add some offset for the gripper

initial_position = np.array([[1, 0, 0, L4 + L5], 
                             [0, 1, 0, 0], 
                             [0, 0, 1, L1 + L2 + L3], 
                             [0, 0, 0, 1]])

s_in_base_frame = np.array([[0, 0, 1, 0, 0, 0],
                            [0, 1, 0, -L1, 0, 0],
                            [0, 1, 0, -L1 - L2, 0, 0],
                            [1, 0, 0, 0, L1 + L2 + L3, 0],
                            [0, 1, 0, -(L1 + L2 + L3), 0, L4],
                            [1, 0, 0, 0, L1 + L2 + L3, 0]]).T

theta_list = np.array([0,0,0,0,0,0])

result = mr.JacobianSpace(s_in_base_frame, theta_list)

print(result)

