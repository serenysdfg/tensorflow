# -*- coding: utf-8 -*-

##tensorflow第一课
##测试入门hello world

#coding=utf-8
import tensorflow as tf

hello=tf.constant("htllo world")
sess=tf.Session()
print(sess.run(hello))
sess.close()


#####基础运算

#coding=utf-8
import tensorflow as tf

sess=tf.Session()
a=tf.constant(2)#常量
b=tf.constant(3)
c=tf.add(a,b)
e=tf.placeholder(tf.int16)
f=tf.placeholder(tf.int16)
add=tf.add(e,f)
print(sess.run(c))
print (sess.run(a*b))
print (sess.run(add,feed_dict={e:20,f:30}))#注意feed大括号
sess.close()
#placeholder一般用于输入数据，是不变的。而Varible一般作为权重W，偏置b，值是改变的
