"""Calculator Cli"""
import argparse
from calculator import Calculator


def calculator_cli():
    """Set up for Calculator Cli"""
    parser = argparse.ArgumentParser(description="Calculator")
    parser.add_argument("-a","--add",action='store',type=int, nargs=2, help="adds two numbers")
    parser.add_argument("-s","--subtract",action='store',type=int, nargs=2, help="subtracts two numbers")
    parser.add_argument("-m","--multiplication",action='store',type=int, nargs=2, help="multiplies two numbers")
    parser.add_argument("-d","--division",action='store',type=int, nargs=2, help="divides two numbers")
    parser.add_argument("-r","--remainder",action='store',type=int, nargs=2, help="finds remainder")
    parser.add_argument("-si","--sine",action='store',type=int, nargs=1, help="finds sine")
    parser.add_argument("-co","--cosine",action='store',type=int, nargs=1, help="finds cosine")
    parser.add_argument("-t","--tangent",action='store',type=int, nargs=1, help="finds tangent")
    parser.add_argument("-p","--is_prime",action='store',type=int, nargs=1, help="This is a Prime Number Finder Function")
    parser.add_argument("-me","--median",action='store',type=int, nargs='+', help="finds median")
    parser.add_argument("-mn","--mean",action='store',type=int, nargs='+', help="finds mean")
    parser.add_argument("-mo","--mode",action='store',type=int, nargs='+', help="finds mode")
    parser.add_argument("-sq","--sqrt",action='store',type=int, nargs=1, help="finds square root")
    args = parser.parse_args()

    if args.add:
        calc = Calculator(args.add)
        print(calc.add())

    if args.subtract:
        calc = Calculator(args.subtract)
        print(calc.subtract())

    if args.multiplication:
        calc = Calculator(args.multiplication)
        print(calc.multiplication())

    if args.division:
        calc = Calculator(args.division)
        print(calc.division())

    if args.remainder:
        calc = Calculator(args.remainder)
        print(calc.remainder())

    if args.sine:
        calc = Calculator(args.sine)
        print(calc.sine())

    if args.cosine:
        calc = Calculator(args.cosine)
        print(calc.cosine())

    if args.tangent:
        calc = Calculator(args.tangent)
        print(calc.tangent())

    if args.is_prime:
        calc = Calculator(args.is_prime)
        print(calc.is_prime())

    if args.median:
        calc = Calculator(args.median)
        print(calc.median())

    if args.mean:
        calc = Calculator(args.mean)
        print(calc.mean())

    if args.mode:
        calc = Calculator(args.mode)
        print(calc.mode())

    if args.sqrt:
        calc = Calculator(args.sqrt)
        print(calc.sqrt())


def main():
    """
    Main
    """
    calculator_cli()

if __name__ == "__main__":
    main()