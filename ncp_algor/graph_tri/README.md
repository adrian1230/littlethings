# rules 

```bash
1st input => n : 2 <= n <= 2000
2nd input => d1 ... dn : 1 <= di <= n - 1
n = len of array
d1 ... dn = vertex i with degree di
find if there is any cactus?
parallel edges and loops are prohibited

if no cactus => -1
else:
  output a set of edge-distinct paths

each path should start with ki and ki => 2
```