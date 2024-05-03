from ctypes import *
import numpy as np
dll = CDLL('test.so')

x = np.array(range(2, 10), dtype=float)
print('x: ', x)
res = dll.sum_test(x.ctypes.data_as(c_void_p), int(10))

print('Result: ', res)


