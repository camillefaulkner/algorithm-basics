Sorting Data

- most modern languages have sorting built in
- bubble sort
- merge sort
- quicksort


The Bubble Sort
- very simple to understand and implement
- performance: O(n^2) <- quadratic
    - for loops inside of for loops are usually n^2
- other sorting algorithms are generally much better
- not considered to be a practical solution

The Merge Sort
- divide and conquer algorithm
- breaks a dataset into individual pieces and merges them
- uses recursion to operate on datasets
- performs well on large sets of data
- in general has a performance of O(n log n) time complexity - loglinear

The Quicksort
- divide and conquer algorithm
- also uses recursion to perform sorting
- generally performs better than merge sort, O(n log n)
- operates in place on the data
- worst case is O(n^2) when data is mostly sorted already
- Pivot Point Selection