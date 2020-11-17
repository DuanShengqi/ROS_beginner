#! /usr/bin/env python
import rospy
import roslib
import actionlib
from beginner_tutorials.msg import DoDishesAction,DoDishesGoal

def active_callback():
    rospy.loginfo("goal active")

def done_callback(state, res):
    rospy.loginfo(state)
    rospy.loginfo("total dishes: %d", res.total_dishes_cleaned)

def feedback_callback(fb):
    rospy.loginfo('washing %d%%', int(fb.percent_complete*100))

if __name__ == "__main__":
    rospy.init_node('dishes_client')
    client = actionlib.SimpleActionClient('do_dishes', DoDishesAction)
    client.wait_for_server()
    #根据action文件的类型进行类初始化
    goal = DoDishesGoal()
    goal.dishwasher_id = 100
    #根据server的处理情况，可以进行不同的函数回调
    client.send_goal(goal, done_callback, active_callback, feedback_callback)

    #设置等待时间，发送请求后，如果超过该时间未返回最后的result，则取消这次的请求数据
    client.wait_for_result(rospy.Duration.from_sec(5.0)) #5s等待
#    rospy.loginfo("Do you finshed?")

