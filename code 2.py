#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

def pose_callback(data):
    # Callback function to get the turtle's current position
    global turtle_x
    turtle_x = data.x

def perform_archimedean_spiral():
    # Initialize a new ROS node
    rospy.init_node('cleaning_robot', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    vel_msg = Twist()

    # Wait for the first pose message to get the initial turtle position
    rospy.wait_for_message('/turtle1/pose', Pose)

    # Collect user input for robot movement parameters
    print("Initiating Archimedean spiral movement")
    speed = input("Enter the speed of the robot: ")
    constant = input("Enter the constant for the Archimedean spiral: ")
    max_distance = input("Enter the maximum distance to travel before stopping: ")

    # Convert input values to float
    speed = float(speed)
    constant = float(constant)
    max_distance = float(max_distance)

    # Move the robot in an Archimedean spiral path
    rate = rospy.Rate(10)  # 10 Hz

    initial_x = turtle_x
    counter = 0

    while abs(turtle_x - initial_x) < max_distance:
        angle = math.radians(counter / 10.0)
        radius = constant * angle

        vel_msg.linear.x = speed
        vel_msg.angular.z = speed / radius if radius > 0.01 else 0

        velocity_publisher.publish(vel_msg)
        rate.sleep()

        counter += 1

    # Stop the robot after reaching the specified distance
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        # Test the Archimedean spiral movement function
        perform_archimedean_spiral()
    except rospy.ROSInterruptException:
        pass
