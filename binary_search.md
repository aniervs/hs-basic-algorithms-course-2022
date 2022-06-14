<h1>Binary Search</h1>


<h2> Introduction </h2>

Binary search is a standard technique, and it helps to solve multiple problems. It can be very powerful, if it's combined with other techniques.

Let's introduce it by presenting a real life situation:

We're in a library, and we are trying to find a book in a specific row of a shelf, and we know the books are **sorted alphabetically**.
Instead of going from left to right (or from right to left), what we usually do is to pick some book from the middle, and check whether it's to the left or to the right of the book that we're searching.  Because the books are sorted alphabetically, we can discard one half of the list of books, and continue doing the same process with the remaining half, and so on until we have only one book.

Formally, the problem is: Given a sorted array, find a certain value $x$ on it.
And our algorithm is: pick the middle of the array, and if the picked valued is greater than $x$, move to the left half, otherwise move to the right half.

Clearly, the number of steps is much less than doing a simple linear search (i.e.: going from left to right until we find the desired element). But for how much?

Well, if the array has length $1024$, in the first step we discard $512$ elements and we're left with $512$. In the second step we discard $256$ and we're left with $256$ elements. In the 3rd step we discard $128$ elements, and after the 4th step we're left with $64$ elements, and after the 5th step, we're left with $32$ elements, and after the 6th step with $16$, and $8$ after the 7th step, and $4$ after the 8th step, and $2$ after the 9th step, and finally a single element after the 10th steps. So, it took only 10 steps to find a number in a list of $1000$ elements.

Formally speaking, the time-complexity of this algorithm is $\mathcal{O}(\log n)$, which, roughly speaking, means that the number of operations grows very slowly with respect to $n$.

**Sample code:**

```Python
l, r = 0, n - 1
while l < r:
    mid = (l + r)//2
    if a[mid] < x:
        l = mid + 1
    else:
        r = mid 

if a[l] == x:
    print(x, "exists")
else:
    print(x, "does not exist")
```

 Notice that even if the number is not present in the list, the search stills converges to certain element. Due to this specific implementation, this code finds the first position with an element greater than or equal to $x$. Then we just ask if this number is exactly equal to $x$. This is convenient, because it helps to optimize functions, but more on that later.

Notice that can also use it to find the first element strictly greater than $x$, or the last element less than $x$, or the last element less than or equal to $x$. In short, we can use binary search to find lower and upper bounds.

And if we can find bounds, then we can count numbers in a range. For example, if we want to count the amount of numbers that are greater than or equal to $5$, and less than or equal to $10$, we can find the first position with an element that is greater than or equal to $5$ (let's call it $l$), and also the first position with an element strictly greater than $10$ (let's call it $r$), and then the number of values between $5$ and $10$ is $r - l$.

<h2>The final recipe</h2>

Formally speaking, if we have some predicate $P: \mathbb{R} \rightarrow \{0, 1\}$ holding that $P(x) \implies P(y)\ \forall y > x$, then we can use the binary search to find the first $x$ such that $P(x) = 1$.

Ok. What does this mean?
If we have a boolean sequence (true and false values), that consiy search to prefix of `False` values and then a suffix of `True` values, then we can use binary search to find the first time the sequence is `True`.

```
F F F F F T T T T T T T T 
```

And thus, we can use this template code in every binary search,

```Python

left = 0, right = N-1
while left < right:
    mid = (l + r)// 2
    if property(mid) == False:
        left = mid + 1
    else:
        right = mid

if property(left) == True:
    return left
else:
    return None

```

Notice that the same is applicable if the sequence consists of a prefix of `True` values and then a suffix of `False` values.

```
T T T T T F F F F F F F F
```


<h2> Some Examples </h2>

<h3>Is it a perfect square?</h2>

Given some integer $x$, say if it is a perfect square or not. The perfect squares are $0, 1, 4, 9, 16, 25, \dots$.

**Hint:** Consider the sequence of squares, consider in particular $k = \lfloor\sqrt x\rfloor$ (the squared root of $x$ rounded down to the nearest integer). Then every number $d \le k$ holds that $d^2 \le x$, and every $d > k$ holds that $d^2 > x$.

<h3> Rotated Sorted array</h3>

There was a sorted array, and somebody rotated it, cut a prefix and appended it to the end. Find the smallest element.

For ```6 7 9 15 19 2 3``` the answer is `2`.

For ```90 5 9 15 19 50 80``` the answer is `5`.

**Hint:** Let's $p$ the position where the minimum value is. We can notice that the suffix starting at $p$ is increasing, and the prefix finishing at $p-1$ is also increasing, and also the first element of the sequence is smaller than the last element of the sequence. Then, every number after $p$ is clearly smaller than the last element of the sequence, and every number before $p$ is clearly greater than the last element of the sequence.

<h3> Find the peak</h3>

There's an array that increases and then decreases: Find the maximum value of the array. For the array ``` 2 3 4 6 9 12 11 8 6 4 1``` the answer is `12`.

**Hint:** Let's denote the position where the peak is as $p$. Every position $i < p$ holds that $A_i < A_{i + 1}$, and every position $i \ge p $holds that $A_i \ge A_{i + 1}$.


<h2> Binary search over real numbers </h2>

Given some real number $x$, find the squared root of $x$. Your answer is considered correctly if is at most $10^{-9}$ away from the real answer.


<h2> Finding roots of continuous functions</h2>

There's a continuous function $f(x)$. Given some $a, b: a \le b$, it holds that $f(a) < 0$ and $f(b) > 0$. 

Then, by the *Mean Value Theorem*, there exists some $c \in (a, b): f(c) = 0$.

We can use Binary Search to find one of those roots. We pick the middle of the range $[a, b]$, (let's call it $x$).

- If $f(x) > 0$, then there exists a root in the range $[a, x]$.
- If $f(x) \le 0$, then there exists a root in the range $[x, b]$ 

We can continue doing so, until the length of the interval that we're looking at is small enough (less thatn the requested precision), because in such case, any number between $l$ and $r$ is close enough to the real solution.

**Sample Code**
```Python
l = 0
r = 1000
eps = 10**-9
while r - l > eps
    m = (l + r) / 2 # Notice that here we're taking the actual half, and not just the rounded division

    if f(m) > 0:
        l = m
    else:
        r = m

print(l)

```



<h2> Bonus problem I (a hard one)</h2>

There are $n$ ships. The $i$-th ship is in the position $x_i$ and has constant velocity $v_i > 0$. We need to say the first time in which a ship intersects with another one.


**Hint**: Let's say $P(t)$ is `True` if there is an intersection withint the first $t$ units of time, and `False` otherwise. Then, it's obvious that $P(t) \implies P(t + 1)$. Then we can use binary search over the time. So, given certa¡n point in time $t$, we need to see if there was an intersection at any point before $t$. Because the ships are moving at a constant speed, once a ship intersects another one, they won't intersect again. Because the ships move with positive velocity, the only way a ship $A$ intersect another ship $B$ is if $A$ is located before $B$ and $A$ has higher speed. The position of the ship $i$ at time $t$ is $y_i(t) = x_i + v_i \cdot t$. During the binary search, we go asking for certain points in time, and for each of them, we need to check if the ships intersected, and this means if they changed their relative order; therefore, we can just sort all ships according to their positions in the current time, and check if their order changed.


<h2> Bonus problem II (requires some calculus)</h2>

Given a polynomial of degree at most 8, and coefficients at most 100, find all its roots.

**Hint**: Derivatives, Recursion, Binary Search.
