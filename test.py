import text
import getopt, sys

def main(argv):

    options = "f:"    
    try:
        opts, args = getopt.getopt(argv, options)
    except getopts.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == '-f': filename=a

    with open(filename,"r") as f:
        fulltxt = f.read()

    txt = text.Text(fulltxt, num_chunk=10)

    print 'unigrams: %s' % (len(txt.unigram))

    m = txt.matrix
    i = txt.index

    for x in m:
        print x

    for x in i:
        print i

if __name__ == '__main__':
    main(sys.argv[1:])




