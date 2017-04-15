[](
  This markdown file is writeup template.
)
## Bash Loop 40pt

### Problem
> We found a program that is hiding a flag but requires you to guess the number it is thinking of. Chances are Linux has an easy way to try all the numbers... Go to /problems/de905332a1594a49f78931c233b0eb2b and try it out!

### Answer
Check file structure and executable file.

```bash
$ ll
total 60
drwxr-xr-x   2 root       root         4096 Mar 31 08:01 ./
drwxr-x--x 573 root       root        36864 Apr  1 23:13 ../
-rwxr-sr-x   1 hacksports bash-loop_9  8216 Mar 31 08:01 bashloop*
-r--r-----   1 hacksports bash-loop_9    33 Mar 31 08:01 flag
$ ./bashloop 
What number am I thinking of? It is between 0 and 4096 
```

Run `for loop` on the terminal.

```bash
$ for i in {0..4096}; do ./bashloop $i | grep flag ; done ;
Yay! That's the number! Here be the flag: c5d35a85c2c2ea7c69a84f6756f57bb1
```

### Flag
c5d35a85c2c2ea7c69a84f6756f57bb1

