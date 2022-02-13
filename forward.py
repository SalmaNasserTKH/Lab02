import rospy

from geometry_msgs.msg import  Twist


rospy.init_node("speed_controller")


pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)

velocity = Twist()
velocity.linear.x = 0.2

r = rospy.Rate(4)


while not rospy.is_shutdown(): 
    pub.publish(velocity)
 
    


    r.sleep()    
