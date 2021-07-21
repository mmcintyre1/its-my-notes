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