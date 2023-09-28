#!/usr/bin/python3.8
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('turtle_publisher')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(1)  # 1 Hz publishing rate

linear_speed = 1  # Linear speed in 1 units per second #
duration = 10  # Duration of movement in seconds

vel_msg = Twist()
vel_msg.linear.x = linear_speed

start_time = rospy.Time.now().to_sec()

while not rospy.is_shutdown():
    current_time = rospy.Time.now().to_sec()
    elapsed_time = current_time - start_time

    if elapsed_time < duration:
        pub.publish(vel_msg)
        rospy.loginfo("Moving in a straight line")
    else:
        break

    rate.sleep()

# Stop the turtle after reaching the desired duration
vel_msg.linear.x = 0
pub.publish(vel_msg)
rospy.loginfo("Stopped moving")
