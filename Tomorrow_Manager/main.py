'''

'''
import time


ct = time.localtime()

print('Hi! Im your Tomorrow Manager.')
print('today is {}-{}-{} ,current time is {}:{}:{} '.format(ct.tm_year,ct.tm_mon,ct.tm_mday,ct.tm_hour,ct.tm_min,ct.tm_sec))
print('when do you like to wake up?')
