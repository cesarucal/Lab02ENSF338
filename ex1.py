def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
""" 

    1. What does this code do?

    A. It is a recursive function that calculates the nth Fibonacci number until n reaches the value of 0 or 1. 

    
    2. Is this an example of a divide-and-conquer algorithm (think carefully about this one)?

    A. Yes it is a divide-and-conquer algorithm. The function is divided into two subproblems: calculating func(n-1) and func(n-2). 
       These subproblems are essentially smaller instances of the same problem, and their solutions are combined to find the solution 
       to the original problem. 

    
    3. Give an expression for the time complexity of the algorithm [0.2 pts]

    A. An expression for its time complexity is O(2^n) due to its exponential growth in the number of function calls.

    4.
"""
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
        result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = result
        return result

# 5. The time complexity of the optimized algoritm is O(n).
    
import time
import matplotlib.pyplot as plt

def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
        result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = result
        return result
    
def time_fibonacci_functions(max_n):
    times_recursive = []
    times_memoized = []

    for n in range(max_n +1 ):
        start_time = time.time()
        fibonacci_recursive(n)
        end_time = time.time()
        times_recursive.append(end_time - start_time)

        start_time = time.time()
        fibonacci_memo(n)
        end_time = time.time()
        times_memoized.append(end_time - start_time)

    return times_recursive, times_memoized

max_n = 35

times_recursive, times_memoized = time_fibonacci_functions(max_n)

plt.figure(figsize=(10, 6))
plt.plot(range(max_n + 1), times_recursive, marker='o', color='red', label='Recursive')
plt.title('Execution Time of Recursive Fibonacci Function')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.savefig('ex1.6.1.jpg')

plt.figure(figsize=(10, 6))
plt.plot(range(max_n + 1), times_memoized, marker='o', color='blue', label='Memoized')
plt.title('Execution Time of Memoized Fibonacci Function')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.savefig('ex1.6.2.jpg')