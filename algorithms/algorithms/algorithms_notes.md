Algorithm complexity:

    Space complexity - how much memory does it require?

    Time complexity - how much time does it take to complete?



Common algorithms:
- Search algorithms - find specific data in a structure
- Sorting algorithms - take a dataset and apply a sort order to it
- Computational algorithms - given one set of data, calculate another (is a given number prime?)
- Collection algorithms - work with collections of data (count specific items, navigate among data elements, filter out unwanted data, etc.)


- Euclid’s Algorithm - find the greatest common denominator (GCD) of two integers
    - for two integers a and b, where a > b, divide a by b
    - if the remainder, r, is 0, then stop: GCD is b
    - otherwise, set a to b, b to r, and repeat at step 1 until r is 0
    

Understanding Algorithm Performance:
- measure how an algorithm responds to dataset size
- Big-O notation
    - classifies performance as the input size grows
    - “O” indicates the order of operation: time scale to perform an operation
- many algorithms and data structure have more than one O
    - inserting data, searching for data, deleting data, etc


Notation - Description - Example
 - O(1) - Constant time - looking up a single element in an array
 - O(log n) - Logarithmic - finding an item in a sorted aray with a binary search
 - O(n) - Linear time - searching an unsorted array for a specific value
 - O (n log n) - Log-linear - complex sorting algorithms like heap sort and merge sort
 - O(n^2) - Quadratic - simple sorting algorithms, such a bubble sort, selection sort, and insertion sort
