import random
class CreatPhone(object):

    def mobole_phone(self):
        #第二位数字
        second = [3,4,5,7,8][random.randint(0,4)]

        #第三位数字
        third = {
            3: random.randint(0,9),
            4: [5,7,9][random.randint(0,2)],
            5: [i for i in range(10) if i!= 4][random.randint(0,8)],
            7: [i for i in range(10) if i not in [4,9]][random.randint(0,7)],
            8: random.randint(0,9)
        }[second]

        #最后八位数字
        suffix = random.randint(9999999,100000000)


        #拼接手机号
        phone = "1{}{}{}".format(second,third,suffix)
        print('生成随机手机号: %s' % phone)
        return phone

# CreatPhone().mobole_phone()