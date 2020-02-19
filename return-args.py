import getopt
import sys


def main(argv):
    param_a = ''
    param_b = ''
    if len(argv) == 0:
        print('return-args.py -a <param_a> -b <param_b>')
    else:
        try:
            opts, args = getopt.getopt(argv, "ha:b:", ["param_a=", "param_b="])
        except getopt.GetoptError:
            print('return-args.py -a <param_a> -b <param_b>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('return-args.py -a <param_a> -b <param_b>')
                sys.exit()
            elif opt in ("-a", "--param_a"):
                param_a = arg
            elif opt in ("-b", "--param_b"):
                param_b = arg
        output = 'param_a is ' + param_a + 'param_b is ' + param_b
        print(output)


if __name__ == "__main__":
    main(sys.argv[1:])
