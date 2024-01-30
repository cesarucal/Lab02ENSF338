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
         69 function calls (24 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    55/10    0.000    0.000    0.000    0.000 ex3.py:49(sub_function)
        1    0.000    0.000    0.000    0.000 ex3.py:57(test_function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}     
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


third_function():
         4 function calls in 7.764 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.787    0.787    7.764    7.764 <string>:1(<module>)
        1    6.977    6.977    6.977    6.977 ex3.py:64(third_function)
        1    0.000    0.000    7.764    7.764 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects
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