<!-- This markdown file is writeup template. -->

## Mystery Box 60pt

### Problem
> You've found a mystery machine with a sticky [note](https://webshell2017.picoctf.com/static/65c2504106ce38d8c2971ebaada542c7/note.txt) attached to it! Oh, there's also this [picture](https://webshell2017.picoctf.com/static/65c2504106ce38d8c2971ebaada542c7/MysteryBox.png) of the machine you found.

### Answer
Read Hints...

> - It really gets your gears Turing.
> - I hear there's something Naval about it.

Uh, check `note.txt`&`MysteryBox`...

```bash
$ cat note.txt 
Geheimnis: PXQQ TAMY YDBC WGYE LVN
Umkehrwalze: B
Grundstellung: PPP
Ringstellung: LOG
Steckerbrett: G-L, H-F
```

![shot01](MysteryBox.png)  

Aha, `Geheimnis` is German. The box seems to be a Enigma machine.  
Let's decrypt it using [Enigma Machine Emulator](http://enigma.louisedade.co.uk/enigma.html).  


Input `PXQQ TAMY YDB WGYE LVN` to Geheimnis and do others in the same way. I got the flag.
### Flag
QUITEPUZZLINGINDEED
