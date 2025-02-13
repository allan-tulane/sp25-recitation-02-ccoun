from main import *
import math

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(40, 5, 2) == 5390
	assert simple_work_calc(50, 6, 2) == 13592
	assert simple_work_calc(60, 7, 2) == 27416

def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(100, 2, 2, lambda n: 1) == 127
	assert work_calc(1000, 2, 2, lambda n: 1) == 1023
	assert work_calc(10000, 2, 2, lambda n: 1) == 16383
	assert work_calc(100000, 2, 2, lambda n: 1) == 131071

	assert work_calc(10, 2, 2, lambda n: n) == 36
	assert work_calc(100, 2, 2, lambda n: n) == 652
	assert work_calc(1000, 2, 2, lambda n: n) == 9120
	assert work_calc(10000, 2, 2, lambda n: n) == 133456
	assert work_calc(100000, 2, 2, lambda n: n) == 1656000

	assert work_calc(10, 2, 2, lambda n: int(math.log(n))) == 4
	assert work_calc(100, 2, 2, lambda n: int(math.log(n))) == 86
	assert work_calc(1000, 2, 2, lambda n: int(math.log(n))) == 742
	assert work_calc(10000, 2, 2, lambda n: int(math.log(n))) == 7085
	assert work_calc(100000, 2, 2, lambda n: int(math.log(n))) == 93647


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
	sizes = [10, 20, 50, 100, 1000, 5000, 10000]

	work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: int(n ** 0.5))

	work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n ** 2)

	work_fn3 = lambda n: work_calc(n, 2, 2, lambda n: n)

	results_1_2 = compare_work(work_fn1, work_fn2, sizes)
	results_2_3 = compare_work(work_fn2, work_fn3, sizes)
	results_1_3 = compare_work(work_fn1, work_fn3, sizes)

	print("Comparison of W1 (c < log_b a) and W2 (c > log_b a):")
	print_results(results_1_2)

	print("\nComparison of W2 (c > log_b a) and W3 (c = log_b a):")
	print_results(results_2_3)

	print("\nComparison of W1 (c < log_b a) and W3 (c = log_b a):")
	print_results(results_1_3)

	
def test_compare_span():
	sizes = [10, 20, 50, 100, 1000, 5000, 10000]

	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n)
	span_fn3 = lambda n: span_calc (n, 2, 2, lambda n: int(math.log(n)))

	results_1_2 = compare_span(span_fn1, span_fn2, sizes)
	results_1_3 = compare_span(span_fn1, span_fn3, sizes)
	results_2_3 = compare_span(span_fn2, span_fn3, sizes)

	print("Comparison of span_fn1 (f(n) = 1) vs span_fn2 (f(n) = n):")
	print_results(results_1_2)

	print("\nComparison of span_fn1 (f(n) = 1) vs span_fn3 (f(n) = log(n)):")
	print_results(results_1_3)

	print("\nComparison of span_fn2 (f(n) = n) vs span_fn3 (f(n) = log(n)):")
	print_results(results_2_3)
