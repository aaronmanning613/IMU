# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:04:01 2020

@author: Aaron
"""
import numpy as np
from quatern_tools import quaternion_tools

angle1 = [1,0,0]
angle1_quat = quaternion_tools().axisAngle2quatern(angle1,-np.pi)

print(angle1_quat)
