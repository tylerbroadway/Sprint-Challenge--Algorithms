#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The while loop will run as long as a is less than n cubed. With each loop, a is incremented by n squared. Because we're not actually iterating through n, the size of n doesn't really play a huge role in runtime, so the complexity would be O(n) (because we're simply performing computations on n, which a computer can do in very little time (especially with Python, because there is no upper bound on an int)). 


b) The initial for loop is simply iterating through n in a linear fashion, so the complexity of that particular piece of code would be O(n). The while loop within the for loop runs while j is less than n, and with each loop, j is being doubled, which implies a logarithmic function. The complexity of this code is O(n log n), or Linearithmic. 


c) The complexity of this function is O(n), or linear, because a recursive function will always recurse n times.

## Exercise II

1. Find the base case. In which case do we want to return? 
    We want to return when we've found the value of floor f, or the floor that has the maximum height for safely dropping eggs.

2. Find the middle floor of the building by dividing the total floors by 2. 
    middle = n // 2

3. Drop the egg from the middle floor. If the egg breaks, find the next middle by halving the current middle. Repeat this process by calling the function on itself, passing in the halved number of floors each time.

4.  If the egg doesn't break, find the middle floor of the upper half of the building 
        ex: middle = n // middle

5. Drop the egg again from the new middle. Repeat this process (recursively) until the egg breaks.

This is essentially a binary search algorithm, which runs in the order of log n, or in Big O notation, O(log n), "log" b/c of the continuous halving of n. 
