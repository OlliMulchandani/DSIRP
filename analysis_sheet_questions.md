<h1>Analysis Sheet Questions</h1>

<h2>Big-O Notation</h2>

1.  What is the order of growth of $n^3 + n^2$? What about
    $1000000 n^3 + n^2$? What about $n^3 + 1000000 n^2$?

All three of these expressions have an order of growth of $O(n^3)$

2.  What is the order of growth of $(n^2 + n) \cdot (n + 1)$? Before you
    start multiplying, remember that you only need the leading term.

$O(n^3)$

3.  If $f$ is in $O(g)$, for some unspecified function $g$, what can we
    say about $af+b$, where $a$ and $b$ are constants?

We can say that the order of growth will still be $O(g)$

4.  If $f_1$ and $f_2$ are in $O(g)$, what can we say about $f_1 + f_2$?

We can say that the order of growth will still be $O(g)$

5.  If $f_1$ is in $O(g)$ and $f_2$ is in $O(h)$, what can we say about
    $f_1 + f_2$?

We can say that the order of growth will either be $O(g)$ or $O(h)$, depending on whether the leading term of function $g$ or $h$ is greater

6.  If $f_1$ is in $O(g)$ and $f_2$ is in $O(h)$, what can we say about
    $f_1 \cdot f_2$?6.

 We can say that the order of growth will be $O(g•h)$

<h2>Sorting</h2>

1.  What is a "comparison sort?" What is the best worst-case order of growth for a comparison sort? What is the best worst-case order of growth for any sort algorithm?

A comparison sort examines data by comparing two elements at a time with a comparison operator. The best worst-case order of growth for a comparison sort is $O(n \log n)$. The best worst-case order of groth for any sort algorithm is $O(n^2)$.

2.  What is the order of growth of bubble sort, and why does Barack Obama think it is "the wrong way to go?"

The order of growth of a bubble sort is $O(n^2)$. Obama believes it is the wrong way to go because it would take far too long when sorting a large number of items.

3.  What is the order of growth of radix sort? What preconditions do we need to use it?

The order of growth of a radix sort is $O(n•k)$. To use it, all numbers must have the same number of digits.

4.  What is a stable sort and why might it matter in practice?

Stable algorithms sort equal elements in the order they are when they are input, although there are multiple theoretically correct orders that the list could be sorted. It could be important when a data set is being sorted multiple times to ensure that the output is what the programmer is expecting and would not vary.

5.  What is the worst sorting algorithm (that has a name)?

The worst sorting algorithm is a Bogosort.

6.  What sort algorithm does the C library use? What sort algorithm does Python use? Are these algorithms stable? You might have to Google around to find these answers.

The C library uses Quicksort, which is not stable. Python uses Timsort, which is stable.

7.  Many of the non-comparison sorts are linear, so why does Python use an $O(n \log n)$ comparison sort?

Python uses $O(n \log n)$ sort because it is fast and it has $n$ memory storage in the worst-case.
