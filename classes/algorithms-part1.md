# Algorithms - Part 1
{: .no_toc }

- Princeton's Algorithms, Part 1 course from [Coursera](https://www.coursera.org/learn/algorithms-part1/home/welcome)
- [GitHub Repository for class exercises](https://github.com/mmcintyre1/algorithms-part1)

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>


Steps to develop a usable algorithm (scientific method)
1. model the problem
2. find an algorithm to solve it
3. fast enough? fits in memory?
4. if not, figure out why
5. find a way to address the problem
6. iterate until satisfied

## Dynamic Connectivity
### Union Find
Given a set of N objects
- union command: connect two objects
- find/connected query: is there a path connecting the two objects

Larger example: is there a path connecting `p` and `q` in a larger path-finding exercise

Some applications of this algorithm:
- pixels in a digital photo
- computers in a network
- friends in a social network
- transistors in a computer chip
- elements in a math set
- variable names in a Fortran program
- metallic sites in a composite system

Modeling the connection:
We assume "is connected to" is an equivalence relation
- reflexic: p is connected to q
- symmetric: if p is connect to q then q is connected to p
- transitive: if p is connect to q and q is connected to r, then p is connect to r

Connected Components: Maximal set of ojbects that are mutually connected

To implement:
find query: check if two objects are in same component
union command: replace components containing two objects with their union


Union-find data type (API)
Goal: design efficient data structure for union-find
- number of objects N can be huge
- number of operations can be huge
- find queries and union commands may be intermixed

```java
public class UF {
  UF(int N) {};
  void union(int p, int q) {};
  boolean connected(int p, int q) {};
  int find(int p) {};
  int count() {};
}
```

### Quick Find
eager approach (compute before call)

each index in array stores reference to its group, so union(1, 2) is rendered like [0, 2, 2], and connected(1, 2) is 2 == 2.

```java
public class QuickFindUF {
    private int[] id;

    public QuickFindUF(int N) {
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    public boolean connected(int p, int q) {
        return id[p] == id[q];
    }

    public void union(int p, int q) {
        int pid = id[p];
        int qid = id[q];
        for (int i = 0; i < id.length; i++) {
            if (id[i] == pid) {
                id[i] = qid;
            }
        }
    }
}
```

quick find is too slow -- union is n<sup>2</sup>
n<sup>2</sup> (quadratic) operations are too slow. As computers get larger, these quadratic algorithms don't scale with new computers.

**Rough standard (for now)**
- 109 operations per second
- 109 words of main memory
- Touch all words in approximately 1 second

**Huge problem for quick-find**
109 union commands on 109 objects
Quick-find takes more than 1018 operations
30+ years of computer time!

**Quadratic algorithms don't scale with technology**
- New computer may be 10x as fast
- But, has 10x as much memory ⇒want to solve a problem that is 10x as big
- With quadratic algorithm, takes 10x as long!

### Quick Union
lazy approach (compute as needed)
integer array, but instead of storing a reference to its tree node

```java
public class QuickUnionUF {
    private int[] id;

    public QuickUnionUF(int N) {
        // same constructor as QuickFind
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    private int root(int i) {
        while (i != id[i]) {
            i = id[i];
        }
        return i;
    }

    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    public void union(int p, int q) {
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }
}
```

cost model: initialize, union, find all linear
defect: trees can get tall, and find is too expensive

### Quick Union Improvements
**weighted quick union**
- modify quick union to avoid tall trees
- keep track of size of each tree (number of objects)
- balance by linking root of smaller tree to root of larger tree


```java
// initialize a sz array
public void union(int p, int q) {
      int i = root(p);
      int j = root(q);
      if (i == j) {
          return;
      }
      if (sz[i] < sz[j]) {
          id[i] = j;
          sz[j] += sz[i];
      } else {
          id[j] = i;
          sz[i] += sz[j];
      }
  }
```

running time for weighted quick union is at most lg _N_ (log base 2)

**weighted quick union with path compression**

after computer the root of p, set the id of each examined node to the root

We might use a two pass variant, which is to add a second loop to `root()` to set `id[]` to node, or we can do single pass like this:

```java
private int root(int i) {
  while (i != id[i]) {
    id[i] = id[id[i]];
    i = id[i];
  }
  return i;
}
```
this halves path length, but in practice it works just as well

in theory, weight quick union with path compression is not quite linear, but in practice it is. In fact no linear-time algorithm exists for quick union.

|  algorithm | worst-case time  |
|---|---|
| quick find | n |
| quick union | n |
| weighted quick union | log(n) |
| quick union with path compression | log(n) |
| weighted quick union with path compression| log * n |

### Union Find Applications
Percolation
- _n_ X _n_ grid of sites
- each site is open with probability _p_ or blocked with probability _p_ - 1
- system percolates iff (if and only if) top and bottom are connected by open sites

percolates

| x | x |   |   | x |
|---|---|---|---|---|
|   | x |   | x |   |
|   | x |   |   |   |
|   |   | x |   | x |

doesn't percolate

| x | x |   |   | x |
|---|---|---|---|---|
|   | x |   | x |   |
|   | x |   |   |   |
|   |   | x | x | x |

many models for physical systems:

| model              | system     | open      | closed    | percolates   |
|--------------------|------------|-----------|-----------|--------------|
| electricity        | material   | conductor | insulated | conducts     |
| fluid flow         | material   | empty     | blocked   | porous       |
| social interaction | population | person    | empty     | communicates |

likelihood of percolation depends on probability, and we cannot figure this out mathematically, but we can computationally (by running millions of simulations)

monte carlo simulations (relies on repeated random siumlation to get numerical results) can be used to add random open sites (increasing p) until top connects to bottom. One way to check is to check all top against all bottom, but this is n<sup>2</sup>. A more performant way would be to create a simulated 'top' spot and a simulated bottom, and check only those two (top could be 0, bottom is _n_ * _n_ + 1)

percolation threshold ends up being 0.592746 for large lattices.

## Analysis of Algorithms
[more information](https://algs4.cs.princeton.edu/14analysis/)

Why do we analyze algorithms?
- predict performance
- compare algorithms
- provide guarantees
- understand theoretical basis
- **primary practical purpose** - avoidance of performance bugs

### Some algorithmic successes
{: .no_toc }
#### Discrete Fournier transforms
{: .no_toc }
- break down waveform of _N_ samples into periodic components
- brute force is n<sup>2</sup>
- FFT algorithm is _N_ _log_ _N_
- works for DVD, JPEG, MRI, astrophysics

#### n-body simulation
{: .no_toc }
- simulate gravitational interactions among _N_ bodies
- brute force is n<sup>2</sup>
- Barnes-Hut algorithm _N_ _log_ _N_

### Scientific Method
{: .no_toc }
- **Observe** some feature of the natural world
- **Hypothesize** a model that is consistent with the observations
- **Predict** events using the hypothesis
- **Verify** the predictions by making further observations
- **Validate** by repeating until the hypothesis and observations agree

Principles:
- Experiments must be **reproducible**
- Hypotheses must be **falsifiable**

### 3-Sum
Given _N_ distinct integers, how many triples sum to exactly zero?

brute force method:
```java
public class ThreeSum {
    public static int count(int[] a) {
        int N = a.length;
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    if (a[i] + a[j] + a[k] == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] a = In.readInts(args[0]);
        StdOut.println(count(a));
    }
}
```

How to time a program?
- manually
- automatically - `StopWatch()` in Java standard library

You can plot on a log-log plot, then run a regression (fit a straight line through data points)

### Mathematical Model
total running time is sum of cost X frequency for all operations

we can test cost of operations, which varies by computer, but more interesting to the study of algorithms is frequency of operations.

Simplifications
cost model
Turing recommended only counting the number of multiplications and recordings (the operations that are most expensive)

tilde notation
ignore lower order terms
- when N is large, terms are negligible
- when N is small, we don't care

### Common Order of Growth Classifications

| order of growth | name | typical code framework | description  | example  | T(2N) / T(N) |
|---|---|-|------|---------|-----|
| 1  | constant  | `a = b + c` | statement   | add two numbers   | 1   |
| logN   | logarithmic  | while (N  > 1)<br>   { N = N / 2; ...  }| divide in half     | binary search     | ~1 |
| N  | linear       | for (int i = 0; i < N; i++)<br>&nbsp;{ ... } | loop  | find the maximum  | 2            |
| N log N | linearithmic | mergesort  | divide and conquer | mergesort         | ~2           |
| N<sup>2</sup>   | quadratic    | for (int i = 0; i < N; i++)<br>&nbsp;for (int j = 0; j < N; j++) <br>&nbsp;{ ... } | double loop    | check all pairs   | 4   |
| N<sup>3</sup>   | cubic  | for (int i = 0; i < N; i++)<br>&nbsp;for (int j = 0; j < N; j++)<br>&nbsp;&nbsp;for (int k = 0; k < N; k++)<br>&nbsp;&nbsp;&nbsp;{ ... } | triple loop  | check all triples | 8  |
| 2<supN</sup>    | exponential  | combinatorial search  | exhaustive search  | check all subsets | T(N)  |

For practical implications, we need linear or linearithmic algorithms to keep pace with Moore's Law.

We can look at binary search for an example.

### Binary Search
Given a sorted aray and a key, find the index of the key in the array.

Interesting tidbit, but there was a bug discovered in Java's implementation of binary search in 2006.

recursive implementation:
```java
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x) return mid;
        if (arr[mid] > x) return binarySearch(arr, l, mid - 1, x);
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}
```

We can also use binary search to speed up the 3 sum problem to n<sup>2</sup> log _n_ speed, as so:

```java
    public static int count(int[] a) {
        int n = a.length;
        Arrays.sort(a);
        if (containsDuplicates(a)) throw new IllegalArgumentException("array contains duplicate integers");
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                int k = Arrays.binarySearch(a, -(a[i] + a[j]));
                if (k > j) count++;
            }
        }
        return count;
    }
```

### types of analyses
{: .no_toc }
- **best case** lower bound on cost
- **worst case** upper bound on cost
- **average case** expected cost for random input

how to choose input model?
- design for worst case
- OR randomize input

goals: establish difficulty of problem and develop optimal algorithms
approach: suppress details in analysis and eliminate variability in input model by focusing on worst case

### algorithm models
{: .no_toc }

- **Tilde** -- provide approximate model
- **Big Theta** -- classify algorithms
- **Big Oh**-- develop upper bounds
- **Big Omega** -- develop lower bounds

### memory usage
{: .no_toc }

**primitives**

| type | bytes |
| - | - |
| boolean | 1 |
| byte | 1 |
| char | 2 |
| int | 4 |
| float | 4 |
| long | 8 |
| double | 8 |

**one-dimensional arrays**

| type | bytes |
| - | - |
| char[] | 2N +  24 |
| int[] | 4N +  24 |
| double[] | 8N +  24 |

**two-dimensional arrays**

| type | bytes |
| - | - |
| char[][] | ~2 M N |
| int[][] | ~4 M N |
| double[][] | ~8 M N |

objects take up 16 bytes, references 8 bytes, and each object has padding so it is a multiple of 8 bytes.

e.g., a Date object uses 32 bytes (4 x 3 for int, 16 object, rounded up to 32)
e.g., a String uses 2N + 64 (16 for object, 8 for reference to array, 2N + 24 for char array, 12 for offset, count, and hash, and 4 for padding)

### questions

1. **3-SUM in quadratic time** Design an algorithm for the 3-SUM problem that takes time proportional to n<sup>2</sup> 2 in the worst case. You may assume that you can sort the nn integers in time proportional to n<sup>2</sup> or better.

2. **Search in a bitonic array.** An array is bitonic if it is comprised of an increasing sequence of integers followed immediately by a decreasing sequence of integers. Write a program that, given a bitonic array of nn distinct integer values, determines whether a given integer is in the array.

- Standard version: Use ~ 3 lg _n_ compares in the worst case.
- Signing bonus: Use ~ 2 lg _n_compares in the worst case (and prove that no algorithm can guarantee to perform fewer than ~ 2 lg _n_ compares in the worst case).

3. **Egg drop.** Suppose that you have an nn-story building (with floors 1 through _n_) and plenty of eggs. An egg breaks if it is dropped from floor _T_ or higher and does not break otherwise. Your goal is to devise a strategy to determine the value of  _T_ given the following limitations on the number of eggs and tosses:

- Version 0: 1 egg, $ T \le T $ tosses.
- Version 1:  $ \sim 1 \lg n $ eggs and $ \sim 1 \lg $ tosses.
- Version 2: $ \sim \lg T $ eggs and  $$\sim 2 \lg T $ tosses.
- Version 3: 22 eggs and $ \sim 2 \sqrt n $ tosses.
- Version 4: 22 eggs and  $ \le c \sqrt T $ tosses for some fixed constant c.

## Bags, Stacks & Queues
fundamental data types, operations of *insert*, *remove*, *iterate*.

Stack - last in, first out (push, pop)
Queue - first in,  first out (enqueue, dequeue)

### Stacks

```java
public class LinkedStack<Item> {
  private Node first = null;

  private class Node {
    Item item;
    Node next;
  }

  public boolean isEmpty() {
    return first == null;
  }

  public void push(Item item) {
    Node oldfirst = first;
    first = new Node();
    first.item = item;
    first.next = oldfirst;
  }

  public Item pop() {
    Item item = first.item;
    first = first.next;
    return item;
  }
}
```

```java
pulbic class FixedCapacityStackOfStrings {
  private String[] s;
  private int N = 0;

  public FixedCapacityStackOfStrings(int capacity) {
    s = new String[capacity];
  }

  public boolean isEmpty() {
    return N == 0;
  }

  public void push(String item) {
    s[N++] = item;
  }

  // prevents loitering
  public String pop() {
    String item = s[--N];
    s[N] = null;
    return item;
  }
}
```

how do you prevent array capacity overflow?

**repeated doubling** -- when array hits capacity, create a new one of twice the length. You can add a custom `resize()` function when the original stack is full.

If array is 1/4 full, you can shrink to half the size.

For stacks, should we use linked list or resizing array?

linked list: every operation takes constant time in the worst case but uses extra time and space to deal with the links

resizing array: every operation takes constant amortized time and less wasted space

### Queues
```java
public class LinkedQueueOfStrings {
  private Node first, last;

  private class Node {
    String item;
    Node next;
  }

  public boolean isEmpty() {
    return first == null;
  }

  public void enqueue(String item) {
    Node oldlast = last;
    last = new Node();
    last.item = item;
    last.next = null;
    if (isEmpty()) first = last;
    else           oldlast.next = last;
  }

  public String dequeue() {
    String item = first.item;
    first = first.next;
    if isEmpty() last = null;
    return item;
  }
}
```

### Bags
Like queue and stack, but no `pop()` or `dequeue()` methods, as order doesn't matter.

### Implementations of Stacks

### Questions
1. Question 1
Queue with two stacks. Implement a queue with two stacks so that each queue operations takes a constant amortized number of stack operations.

2. Question 2
Stack with max. Create a data structure that efficiently supports the stack operations (push and pop) and also a return-the-maximum operation. Assume the elements are real numbers so that you can compare them.

3. Question 3
Java generics. Explain why Java prohibits generic array creation.
