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


"""
