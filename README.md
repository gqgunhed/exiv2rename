# exiv2rename
Python script to rename given JPEG files to their EXIF-dates like YYYYMMDD[optional:_HHMMSS].[extension]

This is just a small script I wrote for myself to rename lots of JPEGs after a successful recovery through ```recoverjpeg``` - it names the JPEGs just with ascending numbers. 

As the files are carved out there is no information about the original filename.

To get some basic information about the pictures the date is extracted from 'Exif.Photo.DateTimeOriginal'. This information is then used to rename the corresponding picture file.

Not much checking included at the moment.

## Pre-requisites

FreeBSD:

    pkg install python27 py27-exiv2

Ubuntu:

    sudo apt-get install python2.7 python-pyexiv2

# Source
The public source for this script can be reached at:
- git@github.com:gqgunhed/py-exiv2rename.git
- https://github.com/gqgunhed/py-exiv2rename.git