<!-- This markdown file is writeup template. -->

## Meta Find Me 70pt

### Problem
> Find the location of the flag in the image: [image.jpg](https://webshell2017.picoctf.com/static/386dfa784c0cd5041a6cb5b870bfdaa8/image.jpg). Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!

### Answer
Look at a hint.

> How can images store location data? Perhaps search for GPS info on photos.

Therefore, we extract meta information of the photo using `exiftool`.

```bash
$ exiftool image.jpg | grep -i gps
GPS Version ID                  : 2.3.0.0
GPS Latitude                    : 7 deg 0' 0.00"
GPS Longitude                   : 96 deg 0' 0.00"
Comment                         : "Your flag is flag_2_meta_4_me_<lat>_<lon>_1c1f. Now find the GPS coordinates of this image! (Degrees only please)"
GPS Position                    : 7 deg 0' 0.00", 96 deg 0' 0.00"
```

Yay! Replace `<lat>` to GPS Latitude value and `<lon>` to GPS Longitude one. 

### Flag
flag_2_meta_4_me_7_96_1c1f
