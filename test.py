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

    print len(txt.words)

if __name__ == '__main__':
    main(sys.argv[1:])




