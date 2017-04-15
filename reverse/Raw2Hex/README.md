<!-- This markdown file is writeup template. -->

## Raw2Hex 20pt

### Problem
> This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/45f3b0abcf176b7cf7c1536b28d05d72 and turn that Raw2Hex!

### Answer
Check files...

```bash
$ ll /problems/45f3b0abcf176b7cf7c1536b28d05d72 
total 56
drwxr-xr-x   2 root       root       4096 Mar 31 07:41 ./
drwxr-x--x 573 root       root      36864 Apr  1 23:13 ../
-r--r-----   1 hacksports raw2hex_5    33 Mar 31 07:41 flag
-rwxr-sr-x   1 hacksports raw2hex_5  7848 Mar 31 07:41 raw2hex*
$ /problems/45f3b0abcf176b7cf7c1536b28d05d72/raw2hex 
The flag is:�v�\�h�3�-��
                          �
```
Using `cut`&`xxd` command, Extracts the string (remove `The flag is:`) and converts it to a hex.  


```bash
$ /problems/45f3b0abcf176b7cf7c1536b28d05d72/raw2hex  | cut -d ':' -f2 | xxd -plain
cc76ae5c1b19d06897338d2deaa50bf00a
```

### Flag
cc76ae5c1b19d06897338d2deaa50bf00a
