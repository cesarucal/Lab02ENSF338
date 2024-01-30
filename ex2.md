Exercise 2
    1. 
    (a)Interpolation starts at a midpoint that is more likely to occur while Binary starts directly at the center. 
    (b) Interpolation reduces the number of comparions required which makes it a time-efficient alorightm

    2. When the data follows a different distribution, such as being skewed or clustered, the interpolation algorithm may lead to inaccurate estimations of the target's position. Thus, performance can be adversely affected, and in such cases, algorithms like binary search, which do not rely on specific distribution assumptions, may be more suitable.

    3. The part of the code that would be affected is the following: 
    pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

    4. Linear Search is the best and only option for unordered Data sets, meaning the numbers aren't in ascending order. Interpolation and Binary Search would fail in this case. 

    5. Linear search would be better for Small data sets or data sets tat are irregularly distributed (has outliers). Binary Search and Interpolation assume a certain data structure/ order and their efficiency diminishes when the data doesn't conform to these assumptions.

    6. To improve Binary search 
    
