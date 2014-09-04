import text
import getopt, sys

def usage():
    print 'python test.py -f <path/to/txtfile>'

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

    i = [str(x) for x in txt.index]
    col_width = len(max(i, key=lambda l: len(l)))
    i = [x.center(col_width) for x in i]

    print '%s' % (' '.join(i))
    for x in txt.matrix: 
            print ' '.join(str(x).center(col_width))


if __name__ == '__main__':
    main(sys.argv[1:])




