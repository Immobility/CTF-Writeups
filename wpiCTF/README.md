Source pt1
--------------
```
Challenge:
ssh source@source.wpictf.xyz -p 31337 (or 31338 or 31339). Password is sourcelocker

Here is your babybuff.
```

Never had any experience with pwn without having a binary file (Also my first successful pwn challenge), however, I figured it worked out the same way as most binary exploitation did.
When we write a couple of passwords to the file, it always seem to show "Pass auth failed.", and close out of the shell.
![](https://raw.githubusercontent.com/Immobility/CTF/master/wpiCTF/photos/Screenshot%20at%202019-04-16%2015-05-45.png)

However, when we type spam more characters, such as:
```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

The only output seems to be "Connection to source.wpictf.xyz closed." So that seemed suspicious because we want a ``` Pasword auth failed ```, which felt like an overflow error, which shouldn't be too possible if the program is secure.
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

Strings
-------------
```
Challenge:
A handy tool for your RE efforts!

    made by AWG

File from https://drive.google.com/open?id=1Hr30UBpwKEbt5UF4w2GzfXnVDXoCRVIs
```

When executing the program, it worked the same way as the ```strings``` command would do. But what if we strings the file? So I tried to take a look at the file's functions.
![](https://raw.githubusercontent.com/Immobility/CTF/master/wpiCTF/photos/Screenshot%20at%202019-04-16%2015-23-47.png)

Ooh!, so our flag is ```WPI{What_do_you_mean_I_SEE_AHH_SKI}```

-------------

Jocipher
-------------
```
Challenge:
Decrypt PIY{zsxh-sqrvufwh-nfgl} to get the flag!

made by Samantha Comeau

https://drive.google.com/open?id=1MKcNvHuFCo8vsHZgKOOT0vWddfIzRFk1
```

After getting the required file, we were supposed to decrypt ```PIY{zsxh-sqrvufwh-nfgl}``` to supposedly get out flag. I wrote a small bash script to retrieve the flag.

```
# !/bin/bash

for i in {1..100}
do
        ./jocipher.pyc --string "PIY{zsxh-sqrvufwh-nfgl}" --shift $i --decode | grep WPI
done
```

``` ./jocipher.pyc --string "PIY{zsxh-sqrvufwh-nfgl}" --shift 48 --decode```

Where our reasonable output is ```WPI{xkcd-keyboard-mash}```

------------

Webinspect
------------
```
Challenge:
Something is lurking at https://www.wpictf.xyz
```

They redirect you to the site. where if you open up the source code, you'll find
![](https://github.com/Immobility/CTF/blob/master/wpiCTF/photos/7e0251fa47ee79d28850a4a150bf3bbf.png?raw=true)

``` WPI{Inspect0r_Gadget} ```

------------

Getaflag
------------
```
Challenge:
Come on down and get your flag, all you have to do is enter the correct password ...

http://getaflag.wpictf.xyz:31337/ (or 31338 or 31339)

made by godeva
```

The site starts with 
![](https://raw.githubusercontent.com/Immobility/CTF/master/wpiCTF/photos/Screenshot%20at%202019-04-16%2023-10-39.png)

I started with some simple SQL injections such as ``` ' OR 1=1-- ``` or ``` ' OR 1=1# ```, but I didn't get anything out of that. However, after I inspected the source code, on the comments, it showed ```  SGV5IEdvdXRoYW0sIGRvbid0IGZvcmdldCB0byBibG9jayAvYXV0aC5waHAgYWZ0ZXIgeW91IHVwbG9hZCB0aGlzIGNoYWxsZW5nZSA7KQ== ```, which in base64, translates to
``` Hey Goutham, don't forget to block /auth.php after you upload this challenge ;) ```, aha! so when I went to http://getaflag.wpictf.xyz:31337/auth.php it gave me this psudocode
```

      // Pseudocode
      $passcode = '???';
      $flag = '????'

      extract($_GET);
      if (($input is detected)) {
        if ($input === get_contents($passcode)) {
          return $flag
        } else {
          echo "Invalid ... Please try again!"
        }
      }
```

Because I didn't know to much about PHP, but after reading some functions, I [stumbled](https://stackoverflow.com/questions/829407/what-is-so-wrong-with-extract) on how the extract function is very vulnerable due to how it can replace an element in an array. So after experimenting and having a small knowledge of address object exploits, I came up to an idea since ```$input === get_contents($passcode)```, and the address bar shows the query, I changed input to a null value and also wrote a passcode = null, resulting in 
```http://getaflag.wpictf.xyz:31337/?input=&passcode=null```. and our result should have given us 

![](https://raw.githubusercontent.com/Immobility/CTF/master/wpiCTF/photos/Screenshot%20at%202019-04-16%2023-31-16.png)

However, you get rick roll'd after seeing clicking on the link, so when I inspected the source code again, it gave me the flag!

```WPI{1_l0v3_PHP}```

------------
Chirp
------------
```
Challenge:
made by Justo and siege

file from https://drive.google.com/open?id=1lcdC9qVBKtSfxOPWLbWd8kAYnPEoSZQb
```

For this challenge, you had to look at a photo of this bird

![](https://raw.githubusercontent.com/Immobility/CTF/master/wpiCTF/photos/chal.jpg)

At first, I thought it was steganography, but I later realized that recon was not supposed to be a steg challenge. So after connecting the title of the challenge and the picture of the bird, I found that the image is depicting an image of Twitter. I went to the sponsor's Twitter page and got the flag.

``` WPI{sp0nsored_by_si3ge} ```

------------



