# exiv2rename
Python script to rename given JPEG files to their EXIF-dates like YYYYMMDD[optional:_HHMMSS].[extension]

This is just a small script I wrote to rename lots of JPEGs after a sucessfull recovery through recoverjpeg - that named the JPEGs just with ascending numbers. As the files are carved out there is no information about the original filename.
To get some basic information about the pictures the date is extracted from 'Exif.Photo.DateTimeOriginal'. This information is then used to rename the corresponding picture file.

Not much checking included at the moment.
