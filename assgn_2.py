#!/usr/bin/python
from datetime import datetime
import abc

class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()

class LogFile(WriteFile):

    def write(self, text):
        dt = datetime.now()
        dt_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}     {1}'.format(dt_str, text))


class DelimFile(WriteFile):
    def __init__(self, file, delim):
        super(DelimFile, self).__init__(file)
        self.delim = delim

    def write(self, list):
        line = self.delim.join(list)
        self.write_line(line)



