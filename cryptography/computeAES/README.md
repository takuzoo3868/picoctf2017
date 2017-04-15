<!-- This markdown file is writeup template. -->

## computeAES 50pt

### Problem
> You found this [clue](https://webshell2017.picoctf.com/static/2e78cf6a104dfa8e0c9220e987aaceb2/clue.txt) laying around. Can you decrypt it?

### Answer
Download and check `clue.txt`.

```bash
$ cat clue.txt 
Encrypted with AES in ECB mode. All values base64 encoded
ciphertext = rW4q3swEuIOEy8RTIp/DCMdNPtdYopSRXKSLYnX9NQe8z+LMsZ6Mx/x8pwGwofdZ
key = 6v3TyEgjUcQRnWuIhjdTBA== 
```

Using Python(pycrypto), I wrote simple code. 

```bash
$ ./decrypt.py 
flag{do_not_let_machines_win_983e8a2d}__________
```

### Flag
do_not_let_machines_win_983e8a2d
