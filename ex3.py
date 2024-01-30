import cProfile

"""
Answers:
1. What is a profiler, and what does it do?
Profiler is a program that provides a set of statistics that describes how often 
and for how long various parts of the program executed. 

2. How does profiling differs from benchmarking?
Benchmarking assesses the overall performance of the entire program, whereas profiling analyzes individual components or sections within the program.

3. Use a profiler to measure execution time of the program (skip function definitions)
Implemented in the code below.

4. Discuss a sample output. Where does execution time go?
Output: 
test_function():
         69 function calls (24 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    55/10    0.000    0.000    0.000    0.000 ex3.py:19(sub_function)
        1    0.000    0.000    0.000    0.000 ex3.py:27(test_function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


third_function():
         5 function calls in 62.646 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.407    1.407   11.268   11.268 <string>:1(<module>)
        1    0.000    0.000    9.861    9.861 ex3.py:34(third_function)
        1    9.861    9.861    9.861    9.861 ex3.py:36(<listcomp>)
        1    0.000    0.000   11.269   11.269 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
Discussion:
`test_function` runs too fast to be measured, so discussing `third_function` only.
The whole profiling took 11.269s.
The list comprehension in `third_function` took 9.861s.
The overhead of the function call is 1.407s.
"""

def sub_function(n):
    # sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n - 1)


def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data


def third_function():
    # third function that calculates the square of the numbers from 0 to 100000000
    return [i ** 2 for i in range(100000000)]


print('test_function():')
cProfile.run('test_function()')
print('third_function():')
cProfile.run('third_function()')
test_function()
third_function()