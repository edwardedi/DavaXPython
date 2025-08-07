import argparse
from services import MathService
from db import Database
from models import RequestModel


def main():
    parser = argparse.ArgumentParser(description="Math CLI Tool")
    subparsers = parser.add_subparsers(dest="operation", required=True)

    # Power
    pow_parser = subparsers.add_parser("pow")
    pow_parser.add_argument("base", type=int)
    pow_parser.add_argument("exp", type=int)

    # Fibonacci
    fib_parser = subparsers.add_parser("fibonacci")
    fib_parser.add_argument("n", type=int)

    # Factorial
    fact_parser = subparsers.add_parser("factorial")
    fact_parser.add_argument("n", type=int)

    args = parser.parse_args()
    service = MathService()
    db = Database()

    if args.operation == "pow":
        result = service.pow(args.base, args.exp)
        request = RequestModel(operation="pow",
                               input=str(args.base) + " " + str(args.exp),
                               output=result)
    elif args.operation == "fibonacci":
        result = service.fibonacci(args.n)
        request = RequestModel(operation="fibonacci",
                               input=str(args.n),
                               output=result)
    elif args.operation == "factorial":
        result = service.factorial(args.n)
        request = RequestModel(operation="factorial",
                               input=str(args.n),
                               output=result)
    else:
        parser.print_help()
        return

    db.save_request(request)
    print(f"Result: {result}")
