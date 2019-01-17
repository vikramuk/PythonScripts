'''Test String '''
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
#             This File is for Document in Comments 
''' __Doc__ Strings are here '''
class Simple():
    ''' Simple-Class __Doc__String'''

    def __init__(self, value):
        '''Return Initial value'''
        self.value = value

    def double(self):
        ''' Double Initial Value'''
        return 2* self.value

    def __mul__(self, value):
        ''' Multiplier Method'''
        return self.value * value

def triple(value):
    ''' triple Value '''
    return value*3

simple = Simple(10)
print "Double" , simple.double()
print "Triple", triple(simple)
help(__name__)
help( simple.double)


    
