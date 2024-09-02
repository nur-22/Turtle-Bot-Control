#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist

def move_rectangular_path():
    # Starts a new node
    rospy.init_node('robot_mover', anonymous=True)
    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Set a default speed
    robot_speed = 1.0

    # Receive user input for height and width of the rectangle
    print("Let's move your robot in a perfect rectangular path")
    rect_height = input("Enter the height of the rectangle: ")
    rect_width = input("Enter the width of the rectangle: ")

    rect_height = float(rect_height)
    rect_width = float(rect_width)

    # Move right
    vel_msg.linear.x = abs(robot_speed)
    vel_msg.linear.y = 0
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)
    rospy.sleep(rect_width / robot_speed)

    # Stop the turtle
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)

    # Move up
    vel_msg.linear.x = 0
    vel_msg.linear.y = abs(robot_speed)
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)
    rospy.sleep(rect_height / robot_speed)

    # Stop the turtle
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)

    # Move left
    vel_msg.linear.x = -abs(robot_speed)
    vel_msg.linear.y = 0
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)
    rospy.sleep(rect_width / robot_speed)

    # Stop the turtle
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)

    # Move down
    vel_msg.linear.x = 0
    vel_msg.linear.y = -abs(robot_speed)
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)
    rospy.sleep(rect_height / robot_speed)

    # Stop the turtle
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)

if __name__ == '__main__':
    try:
        # Testing our function
        move_rectangular_path()
    except rospy.ROSInterruptException:
        pass
