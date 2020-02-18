#!/usr/bin/env python
import random
import rospy

from beast_msgs.msg import *
from beast_srvs.srv import *

def set_stiffness(req):
    print "SetStiffnessRequest(stiffness: {})".format(req.stiffness)
    return SetStiffnessResponse(True, "Dummy response")

def main(): 
    rospy.init_node('trolley')

    rospy.Service('~set_stiffness', SetStiffness, set_stiffness)

    rate = rospy.Rate(50) # 10hz

    while not rospy.is_shutdown():

        rate.sleep()

if __name__ == "__main__":
    main()
