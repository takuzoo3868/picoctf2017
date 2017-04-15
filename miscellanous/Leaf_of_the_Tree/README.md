<!-- This markdown file is writeup template. -->

## Leaf of the tree 20pt

### Problem
> We found this annoyingly named directory tree starting at /problems/b70fe815d84b75004f724241458ea9cc. It would be pretty lame to type out all of those directory names but maybe there is something in there worth finding? And maybe we dont need to type out all those names...? Follow the trunk, using cat and ls!

### Answer
Let's search the file because the directory structure is complicated.


```bash
$ find -name "flag"
./trunk/trunk575b/trunk5181/trunk9560/trunkd252/trunk8768/trunke25a/trunk92ac/flag
$ cat trunk/trunk575b/trunk5181/trunk9560/trunkd252/trunk8768/trunke25a/trunk92ac/flag
dbda9f51c858f5ed97b80a9c5a536015
```

### Flag
dbda9f51c858f5ed97b80a9c5a536015
