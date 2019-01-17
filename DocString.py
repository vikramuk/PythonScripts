class DocString():
    ''' Documentation test
    '''

    def Test():
        pass

    def __init__(self):
        self.test= '''Hi'''

print __doc__
help(__name__)
#help (Test)
print "DocString", DocString.__doc__
    
