#!/usr/bin/env python

import numpy as np
import rospy
from std_msgs.msg import Float32, Header

from sensor_msgs.msg import LaserScan

from beast_srvs.srv import *


def set_left_wheel_braking_mode(req):
    print "set_left_wheel_braking_mode:"
    print req
    return SetWheelBrakingModeResponse(True, "Dummy response")


def set_right_wheel_braking_mode(req):
    print "set_right_wheel_braking_mode:"
    print req
    return SetWheelBrakingModeResponse(True, "Dummy response")


def set_left_wheel_braking(req):
    print "set_left_wheel_braking:"
    print req
    return SetWheelBrakingResponse(True, "Dummy response")


def set_right_wheel_braking(req):
    print "set_right_wheel_braking:"
    print req
    return SetWheelBrakingResponse(True, "Dummy response")


def set_left_wheel_braking_lut(req):
    print "set_left_wheel_braking_lut:"
    print req
    return SetWheelBrakingLUTResponse(True, "Dummy response")


def reset_encoders(req):
    print "reset_encoders:"
    print req
    return ResetEncodersResponse(True, "Dummy response")


def set_right_wheel_braking_lut(req):
    print "set_right_wheel_braking_lut:"
    print req
    return SetWheelBrakingLUTResponse(True, "Dummy response")


def left_braking_sub(msg):
    print "left_braking_sub"
    print msg


def right_braking_sub(msg):
    print "right_braking_sub"
    print msg


def publish_scan(scan_pub):
    scan_msg = LaserScan()
    scan_msg.header = Header()
    scan_msg.header.frame_id = "world"
    scan_msg.header.stamp = rospy.Time.now()
    scan_msg.angle_min = -3.1400001049
    scan_msg.angle_max = 3.1400001049
    scan_msg.angle_increment = 0.0174930356443
    scan_msg.range_min = 0.20000000298
    scan_msg.range_max = 60.0
    scan_msg.ranges = np.random.rand(360)*(60.0 - 0.2) + 0.2

    scan_pub.publish(scan_msg)


def main():
    rospy.init_node('trolley')

    rospy.Service('left/set_wheel_braking_mode', SetWheelBrakingMode, set_left_wheel_braking_mode)
    rospy.Service('right/set_wheel_braking_mode', SetWheelBrakingMode, set_right_wheel_braking_mode)

    rospy.Service('left/set_wheel_braking', SetWheelBraking, set_left_wheel_braking)
    rospy.Service('right/set_wheel_braking', SetWheelBraking, set_right_wheel_braking)

    rospy.Service('left/set_wheel_braking_lut', SetWheelBrakingLUT, set_left_wheel_braking_lut)
    rospy.Service('right/set_wheel_braking_lut', SetWheelBrakingLUT, set_right_wheel_braking_lut)

    rospy.Service('reset_encoders', ResetEncoders, reset_encoders)

    rospy.Subscriber('left/braking', Float32, left_braking_sub)
    rospy.Subscriber('right/braking', Float32, right_braking_sub)

    scan_pub = rospy.Publisher('/scan', LaserScan, queue_size=1)

    rate = rospy.Rate(50)  # 50hz

    while not rospy.is_shutdown():
        publish_scan(scan_pub)
        rate.sleep()


if __name__ == "__main__":
    main()
