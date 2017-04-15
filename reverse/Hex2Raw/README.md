<!-- This markdown file is writeup template. -->

## Hex2Raw 20pt

### Problem
> This program requires some unprintable characters as input... But how do you print unprintable characters? CLI yourself to /problems/9177bfe904b2fb486bf2063954b4b3cb and turn that Hex2Raw!
 

### Answer
Using `xxd` command, Hex strings convert to raw. 


```bash
$ echo '59c51289ace9cdd4004afa54d297d310' | xxd -r -p | ./hex2raw
Give me this in raw form (0x41 -> 'A'):
59c51289ace9cdd4004afa54d297d310

You gave me:
59c51289ace9cdd4004afa54d297d310
Yay! That's what I wanted! Here be the flag:
95fbb12ef65fbea5c746f262292dc3c7
```

### Flag
95fbb12ef65fbea5c746f262292dc3c7
