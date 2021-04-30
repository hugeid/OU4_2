""" Python interface to the C++ Integer class """
import ctypes
from time import perf_counter as pc
from functools import cache
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

lib = ctypes.cdll.LoadLibrary('./libheltal.so')

class Heltal(object):
	def __init__(self, val):
		lib.Heltal_new.argtypes = [ctypes.c_int]
		lib.Heltal_new.restype = ctypes.c_void_p
		lib.Heltal_get.argtypes = [ctypes.c_void_p]
		lib.Heltal_fib.argtypes = [ctypes.c_void_p]
		lib.Heltal_fib.restype = ctypes.c_longlong # fib
		lib.Heltal_get.restype = ctypes.c_int
		lib.Heltal_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Heltal_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Heltal_new(val)

	def get(self):
		return lib.Heltal_get(self.obj)

	def set(self, val):
		lib.Heltal_set(self.obj, val)
        
	def __del__(self):
		return lib.Heltal_delete(self.obj)
	
	def fib_py(self, n=None):
		if n is None:
			n = self.get()
		if n <= 1:
			return n
		else:
			return self.fib_py(n-1) + self.fib_py(n-2)
	
	def fib(self):
		return lib.Heltal_fib(self.obj)

def fib_py(n):
	if n <= 1:
		return n
	return fib_py(n-1) + fib_py(n-2)
def display_fib_comp():	
	py_times = []
	c_times = []
	_range = range(30, 45)
	
	plt.figure(figsize=(10, 3))
	plt.title("Comparing C++ and Python3 for fib(n)")
	plt.ylabel("n")
	plt.xlabel("Time (seconds)")
	plt.yticks(_range)
	plt.ylim(min(_range)-1, max(_range)+1, 1)
	
	for i in _range:
		py_time, c_time = compare_fib(i)
		py_times.append(py_time)
		c_times.append(c_time)
	
	
	plt.plot(py_times, _range, "-o", c="blue",label= "Python3")
	plt.plot(c_times, _range, "-o", c="orange", label="c++")
	plt.legend()

	
	
	plt.savefig("fib_times_comparison.png")
	plt.show()
def compare_fib(n):
	start = pc()
	fib_py(n)
	end = pc()
	py_time = end-start
	
	start = pc()
	h = Heltal(n)
	h.fib()
	end = pc()
	c_time = end-start
	return py_time, c_time
def print_47th():
	h = Heltal(47)
	print(h.fib())
def main():
	pass

if __name__ == '__main__':
	main()
