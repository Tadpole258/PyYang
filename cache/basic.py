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


###############################################################
################### NO.4, Sort Algorithms #####################
###############################################################

class Sorts(object):
    @staticmethod
    def bubble_sort(args: list) -> list:
        """
        Pure implementation of bubble sort algorithm in Python
        :param args: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
        """
        sets = args.copy()
        length = len(sets)
        for i in range(length - 1):
            swapped = False
            for j in range(length - 1 - i):
                if sets[j] > sets[j + 1]:
                    swapped = True
                    sets[j], sets[j + 1] = sets[j + 1], sets[j]
            if not swapped:
                # Stop iteration if the collection is sorted.
                # 如果发现整个排序过程中没有交换，提前结束
                break
        return sets

    @staticmethod
    def quick_sort(args: list) -> list:
        """
        A pure Python implementation of quick sort algorithm
        :param args: a mutable collection of comparable items
        :return: the same collection ordered by ascending
        Examples:
        >>> quick_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> quick_sort([])
        []
        >>> quick_sort([-2, 5, 0, -45])
        [-45, -2, 0, 5]
        """
        if len(args) < 2:
            return args
        pivot = args.pop()  # Use the last element as the first pivot
        greater: list[int] = []  # All elements greater than pivot
        lesser: list[int] = []  # All elements less than or equal to pivot
        for element in args:
            (greater if element > pivot else lesser).append(element)
        return Sorts.quick_sort(lesser) + [pivot] + Sorts.quick_sort(greater)

    @staticmethod
    def select_sort(args: list) -> list:
        """Pure implementation of the selection sort algorithm in Python
        :param args: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
        Examples:
        >>> select_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> select_sort([])
        []
        >>> select_sort([-2, -5, -45])
        [-45, -5, -2]
        """
        sets = args.copy()
        length = len(sets)
        for i in range(length - 1):
            least = i
            for k in range(i + 1, length):
                if sets[k] < sets[least]:
                    least = k
            if least != i:
                sets[least], sets[i] = (sets[i], sets[least])
        return sets

    @staticmethod
    def insert_sort(args: list) -> list:
        """A pure Python implementation of the insertion sort algorithm
        :param args: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
        Examples:
        >>> insert_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> insert_sort([]) == sorted([])
        True
        >>> insert_sort([-2, -5, -45]) == sorted([-2, -5, -45])
        True
        >>> insert_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
        True
        >>> import random
        >>> collection = random.sample(range(-50, 50), 100)
        >>> insert_sort(collection) == sorted(collection)
        True
        >>> import string
        >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
        >>> insert_sort(collection) == sorted(collection)
        True
        """
        sets = args.copy()
        for insert_index, insert_value in enumerate(sets[1:]):
            temp_index = insert_index
            while insert_index >= 0 and insert_value < sets[insert_index]:
                sets[insert_index + 1] = sets[insert_index]
                insert_index -= 1
            if insert_index != temp_index:
                sets[insert_index + 1] = insert_value
        return sets

    @staticmethod
    def merge_sort(args: list) -> list:
        """Pure implementation of the merge sort algorithm in Python
        :param args: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
        Examples:
        >>> merge_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> merge_sort([])
        []
        >>> merge_sort([-2, -5, -45])
        [-45, -5, -2]
        """

        def merge(left: list, right: list) -> list:
            """merge left and right
            :param left: left collection
            :param right: right collection
            :return: merge result
            """

            def _merge():
                while left and right:
                    yield (left if left[0] <= right[0] else right).pop(0)
                yield from left
                yield from right

            return list(_merge())

        if len(args) <= 1:
            return args
        mid = len(args) // 2
        return merge(Sorts.merge_sort(args[:mid]), Sorts.merge_sort(args[mid:]))
