#!/usr/bin/env python
import random
import rospy

from beast_msgs.msg import *
from beast_srvs.srv import *


def main(): 
    rospy.init_node('handle')

    force_pub = rospy.Publisher('/handle', Handle, queue_size=1)

    rate = rospy.Rate(50)

    while not rospy.is_shutdown():
        msg = Handle()
        msg.header.stamp = rospy.Time.now()
        msg.force = random.random() * 20
        force_pub.publish(msg)
        rate.sleep()


if __name__ == "__main__":
    main()
