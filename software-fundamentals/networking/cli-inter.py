from argparse import ArgumentParser
    
def parse_arguments():
    parser = ArgumentParser(description="Displays basic argparse functionality")

    parser.add_argument("data", help="A required positional argument")
    parser.add_argument("--option1", help="A optional positional argument", default="This is how you add default")
    parser.add_argument("--option2", "-o", help="An optional keyword argument with a short version")
    parser.add_argument("--flag", "-f", action="store_true", help="An optional flag that requires no argument")

    return parser.parse_args()

if __name__ == "__main__":
    
    args = parse_arguments()

    print(args)

    print(args.option1)

    if args.flag:
        print("Do a thing")