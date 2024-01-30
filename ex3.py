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
         5 function calls in 72.196 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    8.473    8.473   72.196   72.196 <string>:1(<module>)
        1    0.000    0.000   63.722   63.722 ex3.py:64(third_function)
        1   63.722   63.722   63.722   63.722 ex3.py:66(<listcomp>)
        1    0.000    0.000   72.196   72.196 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

        'test_function' runs too fast every time. So everything is 0. 
        tottime (total time spent in the function excluding time in subfunctions): 0.000 seconds.
        cumtime (total time spent in the function including time in subfunctions): 0.000 seconds.
       
        'third_function' 
        tottime: 8.473 seconds.
        cumtime: 72.196 seconds.
        Most of the time is spent in the list comprehension which takes 63.722 seconds.
        
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