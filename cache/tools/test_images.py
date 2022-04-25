import pymysql
import os
import traceback


def write_pic2mysql(path, config):
    """
    读取图片写入数据库
    :param path: 读取的图片的路径
    :param config: 数据库连接配置信息
    :return: None
    """
    filename = path.split('/')[-1]
    try:
        with open(path, 'rb') as f:
            img = f.read()
    except:
        print('读取失败')
        # sys.exit(1)
        return
    try:
        conn = pymysql.connect(host=config['host'],
                               port=config['port'],
                               user=config['user'],
                               passwd=config['password'],
                               db=config['db'],
                               charset='utf8',
                               use_unicode=True)
        cursor = conn.cursor()

        # 注意一下这里的 {0} 的引号，可以试一下去掉引号会提醒没有者找到该字段
        sql = "INSERT INTO test_images (data, name) VALUES (%s, '{0}')".format(filename)
        cursor.execute(sql, img)
        conn.commit()
        cursor.close()
        conn.close()
        print('写入 {} 成功'.format(filename))

    except Exception as e:
        print(e)
        print('写入失败')


def read_mysql2pic(path, filename, config):
    """
    从数据库中读取图片
    :param path: 你要保存的图片的路径
    :param filename:你要从数据库读取的名字，在本例子相当于数据库中的name字段
    :param config: 数据库连接配置信息
    :return: None
    """
    try:
        conn = pymysql.connect(host=config['host'],
                               port=config['port'],
                               user=config['user'],
                               passwd=config['password'],
                               db=config['db'],
                               charset='utf8',
                               use_unicode=True)
        cursor = conn.cursor()
        cursor.execute("select data from test_images where name = '{}'".format(filename))
        res = cursor.fetchone()[0]
        with open(path, 'wb') as f:
            f.write(res)
        print('从数据库中读取 {} 成功'.format(filename))
    except Exception as e:
        print(e)
        print('读取数据库中的图片失败')


if __name__ == '__main__':
    my_config = {'host': '192.168.221.202', 'port': 3305,
                 'user': 'root', 'password': 'admin2021', 'db': 'yqbackup'}
    # write_pic2mysql('./cmongraphy.jpeg', my_config)
    # print(' 写入后再读取 '.center(50, '*'))
    read_mysql2pic('/Users/evanhe/Downloads/read.jpeg', 'cmongraphy.jpeg', my_config)
