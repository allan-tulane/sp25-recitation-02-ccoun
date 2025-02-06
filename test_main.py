from main import *

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == 32
	assert work_calc(20, 3, 2) == 259
	assert work_calc(30, 4, 2) == 1430

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == #TODO
	assert work_calc(30, 3, 2, lambda n: n) == #TODO


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2

    res = compare_work(work_fn1, work_fn2)
	print(res)

	
def test_compare_span():
	# TODO
