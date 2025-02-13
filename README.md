# CMPS 2200  Recitation 02

**Name (Team Member 1):**_________________________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**

***After deriving the asymptotic behavior for these values of f(n), we found that when f(n) = 1 and when f(n) = log(n), there is linear growth with W(n) = O(n), while f(n) = n shows a growth slightly faster than linear, with W(n) = O(nlog(n)). These are supported through our test cases increasing n from 10-100000 and graphing them, which we have linked here: https://drive.google.com/file/d/1bHyWVkYUw0Kr3afPk2k2ivZPufCj3Lc_/view?usp=sharing***

- [ ] 5. (4 points) Now that you have a nice way to empirically generate values of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**TODO: your answer goes here**

***After generating the different values of work for each of the test cases for values of c, we can see using our tables that the work increases the fastest when c > log_b a, and increases the slowest when c < log_b a, with c = log_b a inbetween these two. This shows that when the work is dominated by the root level of the recurrence tree, there will be more work needed for an equal value of n than if the recurrence tree's work was dominated by the leaves or if it was balanced. For W(10000), root dominated (c > log_b a) = 199915760, balanced (c = log_b a) = 133456, and leaf dominated (c < log_b a) = 26496.***

Comparison of W1 (c < log_b a) and W2 (c > log_b a):

|     n |   W_1 |       W_2 |
|-------|-------|-----------|
|    10 |    19 |       174 |
|    20 |    42 |       748 |
|    50 |    93 |      4790 |
|   100 |   196 |     19580 |
|  1000 |  1711 |   1990744 |
|  5000 | 13198 |  49957880 |
| 10000 | 26496 | 199915760 |

Comparison of W2 (c > log_b a) and W3 (c = log_b a):

|     n |       W_1 |    W_2 |
|-------|-----------|--------|
|    10 |       174 |     36 |
|    20 |       748 |     92 |
|    50 |      4790 |    276 |
|   100 |     19580 |    652 |
|  1000 |   1990744 |   9120 |
|  5000 |  49957880 |  61728 |
| 10000 | 199915760 | 133456 |

Comparison of W1 (c < log_b a) and W3 (c = log_b a):

|     n |   W_1 |    W_2 |
|-------|-------|--------|
|    10 |    19 |     36 |
|    20 |    42 |     92 |
|    50 |    93 |    276 |
|   100 |   196 |    652 |
|  1000 |  1711 |   9120 |
|  5000 | 13198 |  61728 |
| 10000 | 26496 | 133456 |


- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**

***After deriving the asymptotic expressions for the spans of the recurrences and using the table from our test function, we found span for f(n) = 1 grows logarithmically: S(n) = O(log(n)) with very slow growth, shown through S(10000) = 14. f(n) = n grows linearly: S(n) = O(n) with almost perfect linear growth, shown through S(10000) = 19995. Finally f(n) = log(n) grows faster than logarithmically but sublinearly: S(n) = O(log^2(n)), as it has low growth while staying above logarithmically, shown through S(10000) = 59. These are all expected as they correlate to the functions that the spans are being taken of.***

Comparison of span_fn1 (f(n) = 1) vs span_fn2 (f(n) = n):

|     n |   W_1 |   W_2 |
|-------|-------|-------|
|    10 |     4 |    18 |
|    20 |     5 |    38 |
|    50 |     6 |    97 |
|   100 |     7 |   197 |
|  1000 |    10 |  1994 |
|  5000 |    13 |  9995 |
| 10000 |    14 | 19995 |

Comparison of span_fn1 (f(n) = 1) vs span_fn3 (f(n) = log(n)):

|     n |   W_1 |   W_2 |
|-------|-------|-------|
|    10 |     4 |     3 |
|    20 |     5 |     5 |
|    50 |     6 |    10 |
|   100 |     7 |    14 |
|  1000 |    10 |    32 |
|  5000 |    13 |    50 |
| 10000 |    14 |    59 |

Comparison of span_fn2 (f(n) = n) vs span_fn3 (f(n) = log(n)):

|     n |   W_1 |   W_2 |
|-------|-------|-------|
|    10 |    18 |     3 |
|    20 |    38 |     5 |
|    50 |    97 |    10 |
|   100 |   197 |    14 |
|  1000 |  1994 |    32 |
|  5000 |  9995 |    50 |
| 10000 | 19995 |    59 |

