import time
import ctypes
import numpy as np
from numpy.random import normal

# import C/C++ modules and set arg/res types

libfile_c = 'build/lib.macosx-10.9-x86_64-3.7/mysum_c.cpython-37m-darwin.so'
mylib_c = ctypes.CDLL(libfile_c)

mylib_c.mysum_int.restype = ctypes.c_longlong
mylib_c.mysum_int.argtypes = [ctypes.c_int,
                              np.ctypeslib.ndpointer(
                                dtype=np.int
                              )]

mylib_c.mysum_double.restype = ctypes.c_double
mylib_c.mysum_double.argtypes = [ctypes.c_int,
                                 np.ctypeslib.ndpointer(
                                    dtype=np.float64
                                 )]


libfile_cpp = 'build/lib.macosx-10.9-x86_64-3.7/mysum_cpp.cpython-37m-darwin.so'
mylib_cpp = ctypes.CDLL(libfile_cpp)

mylib_cpp.mysum_int.restype = ctypes.c_longlong
mylib_cpp.mysum_int.argtypes = [ctypes.c_int,
                                np.ctypeslib.ndpointer(
                                 dtype=np.int
                                )]

mylib_cpp.mysum_double.restype = ctypes.c_double
mylib_cpp.mysum_double.argtypes = [ctypes.c_int,
                                   np.ctypeslib.ndpointer(
                                      dtype=np.float64
                                   )]

# extract functions
cfunc_int = mylib_c.mysum_int
cfunc_double = mylib_c.mysum_double
cppfunc_int = mylib_cpp.mysum_int
cppfunc_double = mylib_cpp.mysum_double

# Simulation parameters
n_sim = 1000
n_data = 1000000

# Generate some big data
array_int = np.arange(n_data).astype(np.int)
array_double = normal(0, 1, n_data).astype(np.float64)

# Int functions
# C solution
start = time.time()
for i in range(n_sim):
    cfunc_int(n_sim, array_int)
t_c = time.time()-start

# C++ solution
start = time.time()
for i in range(n_sim):
    cppfunc_int(n_sim, array_int)
t_cpp = time.time()-start

# Numpy solution 1
start = time.time()
for i in range(n_sim):
    (array_int**2).sum()
t_p1 = time.time()-start

# Numpy solution 2 (using listcomp)
start = time.time()
res = 0
for x in array_int:
    res += x**2
t_p2 = time.time()-start

# Print results
print("Comparing C/C++ to Numpy in case of Int type arithmetics.")
print(f'C: {t_c:.2f} second(s).')
print(f'C++: {t_cpp:.2f} second(s).')
print(f'Numpy_method: {t_p1:.2f} second(s).')
print(f'Numpy_listcomp: {t_p2:.2f} second(s).')

# How fast are C/C++ compared to Numpy?
print(f"In case of doubles, C is about {round(t_p1/t_c, 2)} times faster than Numpy.")
print(f"In case of doubles, C++ is about {round(t_p1/t_cpp, 2)} times faster than Numpy.")

# Double functions
# C solution
start = time.time()
for i in range(n_sim):
    cfunc_double(n_sim, array_double)
t_c = time.time()-start

# C++ solution
start = time.time()
for i in range(n_sim):
    cppfunc_double(n_sim, array_double)
t_cpp = time.time()-start

# Numpy solution 1
start = time.time()
for i in range(n_sim):
    (array_double**2).sum()
t_p1 = time.time()-start

# Numpy solution 2 (using listcomp)
start = time.time()
res = 0
for x in array_double:
    res += x**2
t_p2 = time.time()-start

# Print results
print("Comparing C/C++ to Numpy in case of Double type arithmetics.")
print(f'C: {t_c:.2f} second(s).')
print(f'C++: {t_cpp:.2f} second(s).')
print(f'Numpy_method: {t_p1:.2f} second(s).')
print(f'Numpy_listcomp: {t_p2:.2f} second(s).')

# How fast are C/C++ compared to Numpy?
print(f"In case of doubles, C is about {round(t_p1/t_c, 2)} times faster than Numpy.")
print(f"In case of doubles, C++ is about {round(t_p1/t_cpp, 2)} times faster than Numpy.")
