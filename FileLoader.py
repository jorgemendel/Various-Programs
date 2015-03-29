class FileLoader():
    """Iterator that loads successive files with the same name and an increasing number at their end."""
    def __init__(self, filenames, extension, begin, finish):
        self.fnames = filenames
        self.ext = extension
        self.finish = finish
        self.cpos = begin
        self.cwfn = None  # self.cwfn is the name of the file that will be opened in the following next() call.
        self.update_filename()

    def __iter__(self):
        return self

    def next(self):
        if self.cpos <= self.finish:
            cfile = open(self.cwfn)
            self.cpos += 1
            self.update_filename()
            return cfile
        else:
            raise StopIteration()

    def update_filename(self):
        self.cwfn = self.fnames + str(self.cpos) + self.ext
