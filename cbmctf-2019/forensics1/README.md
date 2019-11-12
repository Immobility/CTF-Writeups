When first unzipping the file, you get 2 files: readme.txt and secret.jpg. Readme.txt outputs "base64 is old fashion encoding...".

Likely a sign that base64 might be used for this sooner or later. However that isn't the case since there is nothing to decode base64.

However, when ``` strings ``` 'ing the secret.jpg, this outputs a very interesting string at the third line and at the end of the file: ``` d0ntTr! ```
I then used ``` steghide extract -sf secret.jpg ``` to try to see if ``` d0ntTr! ``` was the password. 

![](https://raw.githubusercontent.com/Immobility/CTF/master/cbmctf-2019/forensics1/images/steghide.png)

Nice! After ```cat``` or ```strings```'ing the file will print out ```Y2JtY3Rme2ghZGRpbmdfQF9wMWEhbl8zaWdodH0=``` where base64 decoding will print out:

``` cbmctf{h!dding_@_p1a!n_3ight} ```
