#!/usr/bin/python3.8
import rospy
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo("Turtlesim position - x: %f, y: %f", data.x, data.y)

rospy.init_node('turtle_subscriber')

rospy.Subscriber('/turtle1/pose', Pose, callback)

rospy.spin()
