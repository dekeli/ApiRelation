import random
random.random()
# random.uniform()
# random.randint()
# random.randrange()
list=[1,2,3,4,5,6,7]
print(random.sample(list,2))

a = 'songyaqi'
# b = a[::-1]
# r = a.split("a")
# r.reverse()d
# c = ''.join(r)
# d =a[::-1]
aa = a[:]

# 随机生成100个数，然后写入文件
# with open('10.txt','w')as f:
#     for i in range(100):
#         n = random.randint(1,100)
#         f.write(str(n)+'\n')

# 对列表进行去重
# a = [1,1,2,2,3,4,5,6,6,7,8,8,9]
# b=list(set(a))

# 有UTF-8编码的文件a.txt。文件路径在E盘根目录，写一段程序逐行读入文本文件。并在屏幕（gbk编码）打印出来
# fp = open('','r')
# content=fp.read()
# fp.close()

# 冒泡排序
# num = [5,31,6548,256,63,64,1,4,6,9,8,4,56]
#
# for i in range(len(num)-1):
#     for j in range(len(num)-i-1):
#         if num[j] > num[j+1]:
#             num[j],num[j+1] = num[j+1],num[j]
#
# print(num)
def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,2,45,6,8,2,1]

print(bubbleSort(nums))