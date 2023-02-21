#!/usr/bin/env python3

import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
rospy.init_node('navigator')
b = rospy.get_param('b')
phi = rospy.get_param('phi')
xg = rospy.get_param('x')
yg = rospy.get_param('y')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
def navigator(data):
    x = data.x
    y = data.y
    theta = data.theta
    linVel= b * math.sqrt(math.pow((xg-x),2)+math.pow((yg-y),2))
    angVel= phi * (math.atan((yg-y)/(xg-x)) - theta)
    velocity = Twist()
    velocity.linear.x = linVel
    velocity.angular.z = angVel
    pub.publish(velocity)
sub = rospy.Subscriber('/turtle1/pose', Pose, navigator)
rospy.spin()
