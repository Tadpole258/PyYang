# -*- coding:utf-8 -*-
# load packages
from cache import *
import os
import pymssql
import pymysql
import warnings
import pandas as pd
import numpy as np
warnings.filterwarnings('ignore')
# pd.set_option('display.max_columns', None)

###############################################################
################### NO.1, get_file_path #######################
###############################################################
def get_file_path(arg_path, arg_format=''):
    """
    :keyword
        目标,筛选目标目录(arg_path)下的所有规定格式(arg_format)文件路径.

    :parameter
        arg_path, 目标目录的路径；
        arg_format, 需要筛选的格式文件,默认为空；

    :return
        list,返回所有路径列表.
    """
    file_paths = []
    for root, dirs, files in os.walk(arg_path):
        for file in files:
            # 获取文件所属目录
            if not file.startswith('.'):
                # 获取文件路径
                file_path = os.path.join(root, file)
                if file_path.endswith(arg_format):
                    file_paths.append(file_path)
                else:
                    continue
            else:
                continue
    return np.array(file_paths)


###############################################################
################### NO.2, Pymssql #############################
###############################################################
class Mssql(object):
    """
    Application for sql server
    """
    def __init__(self, host=database['host'], user=database['user'],
                 pwd=database['pwd'], db=database['db']):
        # 配置mysql连接
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def query(self, sql):
        """
        :param sql: 基本 sql 查询语句使用
        :return result: 查询结果
        """
        # 数据库配置连接
        conn = pymssql.connect(self.host, self.user, self.pwd, self.db)
        try:
            # 利用pandas直接获取数据
            result = pd.read_sql(sql, conn)
            return result
        except Exception as e:
            # 输出异常
            print(e)
        finally:
            # 关闭连接
            conn.close()

    def execut(self, sql):
        """
        :param sql: 基本sql增删改语句
        :return result: 执行结果
        """
        # 数据库配置连接
        conn = pymssql.connect(self.host, self.user, self.pwd, self.db)
        cursor = conn.cursor() # 连接创建游标
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            conn.rollback()
        finally:
            # 关闭连接
            conn.close()

    def executmany(self, sql, args):
        """
        :param sql: 基本sql数据插入语句
        :param args: 以元组存储数据
        :return result: 查询结果
        """
        # 数据库配置连接
        conn = pymssql.connect(self.host, self.user, self.pwd, self.db)
        cursor = conn.cursor() # 连接创建游标
        try:
            # 执行sql语句
            cursor.executemany(sql, args)
            # 提交到数据库执行
            conn.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            conn.rollback()
        finally:
            # 关闭连接
            conn.close()


###############################################################
################### NO.3, Pymysql #############################
###############################################################

class Mysql(object):
    """
    Application for sql server
    """
    def __init__(self, host=database['host'], user=database['user'], pwd=database['pwd'],
                 db=database['db'],port=int(database['port'])):
        # 配置mysql连接
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = port

    def query(self, sql):
        """
        :param sql: 基本 sql 查询语句使用
        :return result: 查询结果
        """
        # 数据库配置连接
        conn = pymysql.connect(host=self.host, user=self.user, password=self.pwd, db=self.db,
                               port=self.port, charset='utf8')
        try:
            # 利用pandas直接获取数据
            result = pd.read_sql(sql, conn)
            return result
        except Exception as e:
            # 输出异常
            print(e)
        finally:
            # 关闭连接
            conn.close()

    def execut(self, sql):
        """
        :param sql: 基本sql增删改语句
        :return result: 执行结果
        """
        # 数据库配置连接
        conn = pymysql.connect(host=self.host, user=self.user, password=self.pwd, db=self.db,
                               port=self.port, charset='utf8')
        cursor = conn.cursor() # 连接创建游标
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            conn.rollback()
        finally:
            # 关闭连接
            conn.close()

    def executmany(self, sql, args):
        """
        :param sql: 基本sql数据插入语句
        :param args: 已元组存储数据
        :return result: 查询结果
        """
        # 数据库配置连接
        conn = pymysql.connect(host=self.host, user=self.user, password=self.pwd, db=self.db,
                               port=self.port, charset='utf8')
        cursor = conn.cursor() # 连接创建游标
        try:
            # 执行sql语句
            cursor.executemany(sql, args)
            # 提交到数据库执行
            conn.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            conn.rollback()
        finally:
            # 关闭连接
            conn.close()




def bubble_sort(bs_list):
    """
    # 冒泡排序算法
    :param bs_list: 参数，list
    :return bs_list: 升序排序,list
    """
    n = len(bs_list)
    exchange = False
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if bs_list[j] > bs_list[j+1]:
                bs_list[j], bs_list[j+1] = bs_list[j+1], bs_list[j]
                exchange = True
        # 如果发现整个排序过程中没有交换，提前结束
        if not exchange:
            break
    return bs_list
