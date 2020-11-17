#! /usr/bin/env python

#原文地址 ： https://blog.csdn.net/qq_23981335/article/details/100335743
import rospy
import roslib
import actionlib
from beginner_tutorials.msg import *

class DishesServer(object):
    def __init__(self):
        self.server = actionlib.SimpleActionServer('do_dishes', DoDishesAction, self.excute_dishes, False)
        self.server.start()

    def excute_dishes(self, goal):
        i = 0
        #根据action文件的类型进行类初始化
        percent = DoDishesFeedback()
        res = DoDishesResult()

        rate = rospy.Rate(25)
        while i < goal.dishwasher_id :
            i += 1
            percent.percent_complete = i/float(goal.dishwasher_id)
            #处理过程即可向client发送数据
            self.server.publish_feedback(percent)
            rate.sleep()
        #全部处理完成后再次发送数据
        res.total_dishes_cleaned = i
        self.server.set_succeeded(res)

if __name__ == '__main__':
    rospy.init_node('dishes_server')
    server = DishesServer()
    rospy.spin()

