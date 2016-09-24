#coding=utf-8
#author@alingse
#2016.09.24

from __builtin__ import open as builtin_open

class fileHead(object):

    def __init__(self,fileno):

        pass

    def init(self,fileno):
        pass


class flexFile(object):
    def __init__(self,filehead):
        self.filehead = filehead
        pass


def open(fname,mode):
    fileno = builtin_open(fname,mode)
    head = fileHead(fileno)
    file = flexFile(head)

    return file


if __name__ == '__main__':
    file = open('../test/demofileA.txt','w')
    file = open('../test/demofileB.txt','r')
