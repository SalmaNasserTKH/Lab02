import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2,sqrt, pow , pi 

x = 0.0
y = 0.0 
theta = 0.0


def newOdom(msg):
    global x
    global y
    global theta
    

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([ rot_q.x, rot_q.y, rot_q.z, rot_q.w ])
   
rospy.init_node("speed_controller")

sub = rospy.Subscriber("/odom", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)

velocity = Twist()
r = rospy.Rate(4)

goal = Point()
goal.x = 3
goal.y = 3

while not rospy.is_shutdown(): 
    


    pub.publish(velocity)
    r.sleep()    
