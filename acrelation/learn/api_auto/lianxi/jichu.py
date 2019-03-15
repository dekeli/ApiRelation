# code = utf-8

# python交换两个变量的值
# a = 3
# b = 4
# a,b=b,a
# print(a,b)
# d = 'asdf'
# e = 'zxcv'
# f = ''.join(d,e)
# list = [a,a,a,1,2,3,4,5,A,B,C]提取出”12345”
# list = [a,a,a,1,2,3,4,5,A,B,C]
# a,b,c,*middle, e,f,g = list, *middle = [1,2,3,4,5]
print()
# match和search的区别
# match和search都是测试正则表达式与字符串是否匹配，
# 不同的是，match要求字符串的第一个字符就能匹配上正则表达示，
# 而search则不同，如果字符串开头不能匹配，即会继续往后匹配，直接匹配成功或者到字符串结束

# 字符串的查询和替换
# string = 'i like passa'
# a = string.find('8')
# s = string.replace('i','I very',1)
# print(a,s)

# 洗牌函数 shuffle
# import random
# list = [1,2,3,4,5,6,7,8,9]
# random.shuffle(list)
# print(list)


# 16.给定一串字典(或列表),找出指定的（前N个）最大值？最小值？
# 这道题的考点是python内的heapq模块的nlargest() 和 nsmallest(), 而不是min()和max()。这两个函数都能接收关键字参数，用于复杂的结构数据中：
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# import heapq
# cheap = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
# max = heapq.nlargest(3,portfolio,key=lambda s:s['price'])
# print(max)
import os
import time

def main():
    content = 'python基础面试题'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()


# 20. 设计一个函数返回给定文件名的后缀?
# 这道题考了正则表达式的简单知识点。代码如下：

def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点

    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
