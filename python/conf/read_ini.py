#coding:utf-8

import os
import configparser#导入配置文件包

def read_conf(option,section):
    cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前目录
    configPath = os.path.join(cur_path, "config.ini")  # 拼接目录跟文件名
    conf = configparser.ConfigParser()  # 新建实例
    conf.read(configPath)  # 读取config.ini文件
    peizhi=conf.get(option,section)#获取配置
    return peizhi

