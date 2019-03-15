import time

print(time.strftime('%Y%m%d.%H%M',time.localtime(time.time())))
time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
print(time)