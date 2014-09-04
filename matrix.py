
#
# stores NGrams in a matrix using a distinct list of 
# tokens as an index
class Matrix:
    def __init__(self, incList):
        self.matrix=[]

        # set create a unique collection from incList
        # we turn it back into a list in order to be able to use
        # indexes and other list functions
        self.index = list(set(incList)) 


        # the first axis 
        for index1,key in enumerate(self.index): 
            # add a list to the matrix for our new word
            self.matrix.append([0 for x in self.index])
#            print 'x: %s' % (index1)
            # the second axis
            for index2,token in enumerate(self.index):
                # now go through the text and see if we have a pattern
                for position, word in enumerate(incList):
                    # increment the value of the combo
                    if word == key and position+1 < len(incList) and incList[position + 1] == token:
#                        print 'combo: %s %s' % (key, token)
                        self.matrix[index1][index2] += 1


    def get_index(self):  return self.index
    def get_matrix(self): return self.matrix


if __name__ == '__main__':

    l = ['a','b','c','d','a','c','d','s','e','a','b'] 
    a = Matrix(l)
    m = a.get_matrix()
    i = a.get_index()

    print l
    print '%s%s' % (' '*4, '  '.join(i))
    for c, x in enumerate(m): 
        print '%s: %s' % (i[c], x)


 
