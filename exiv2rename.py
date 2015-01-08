#!/usr/bin/env python
"""script to rename files after their original EXIF date
"""

import os
import sys
import shutil
import pyexiv2


class Exiv2Renamer(object):
    """extension of pyexiv2"""

    def __init__(self, fname):
        self.error = False
        self.debug = False
        self.verbose = True
        self.filename = fname
        self.metadata = self._load()

    def _load(self):
        """tries to load metadata from given file"""
        try:
            metadata = pyexiv2.ImageMetadata(self.filename)
            metadata.read()
            if self.debug:
                print metadata.exif_keys
            return metadata
        except:
            print "No EXIF metadata found in %s" % self.filename
            sys.exit(1)

    def _origdate(self):
        """returns: EXIF original date in form YYYYMMDD[optional:_HHMMSS]"""
        try:
            tag = self.metadata['Exif.Photo.DateTimeOriginal']
        except KeyError:
            print "No Exif.Photo.DateTimeOriginal found in file %s" % self.filename
            sys.exit(1)
        try:
            date = tag.value.strftime('%Y%m%d')
        except AttributeError:
            print "No tag.value.strftime found in file %s" % self.filename
            print "found string (%s) instead" % tag.value
            sys.exit(1)
        time = tag.value.strftime('%H%M%S')
        if time:
            return "%s_%s" % (date, time)
        else:
            return date

    def _newname(self):
        """try to save the file
        if exists, append _[counter] to filename until non-existent
        """
        ext = "jpg"         # or get original file extension
        filename = self._origdate()
        counter = 0
        if os.path.exists("%s.%s" % (filename, ext)):
            while os.path.exists(filename + "_" + str(counter) + "." + ext):
                if self.debug:
                    print "%s_%s.%s exists, counting" % (filename, counter, ext)
                counter += 1
            filename = filename + "_" + str(counter)
        filename += "." + ext
        return filename

    def copy(self):
        filename = self._newname()
        try:
            if self.verbose:
                print "Copying %s --> %s" % (self.filename, filename)
            shutil.copy(self.filename, filename)
        except:
            print "ERROR while copying %s to %s" % (self.filename, filename)

    def rename(self):
        filename = self._newname()
        try:
            if self.verbose:
                print "Moving %s --> %s" % (self.filename, filename)
            shutil.move(self.filename, filename)
        except:
            print "ERROR while renaming %s to %s" % (self.filename, filename)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ern = Exiv2Renamer(sys.argv[1])
        ern.copy()
        #ern.rename()
    else:
        print "Must give at least one JPEG to process as parameter."
        sys.exit(1)
