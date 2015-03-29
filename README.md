# Various-Programs

FileLoader.py contains an iterable class that loads files with an increasing number at the end of their filename. For example, if a directory contains the files: text1.txt, text2.txt and text3.txt, all those files can be opened and printed in the following way:

```Python

thefiles = FileLoader("text", "txt", 1, 3)
for file_object in thefiles:
    print file_object.read()
```

```       
FileLoader(filenames, extension, begin, finish)  
```

Maybe you will find it useful.
