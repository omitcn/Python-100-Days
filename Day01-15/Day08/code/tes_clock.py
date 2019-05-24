'''
定义和使用时钟类
author:启萍
日期:2019/05/22
'''
import sys
import time
class Clock(object):
    def __init__(self, **kw):
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour, self._minute, self._second = kw['hour'], kw['minute'], kw['second']
        else:
            tm=time.localtime(time.time())

    