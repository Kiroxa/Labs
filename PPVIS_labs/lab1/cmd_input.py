import argparse


VERSION = "0.1.0"


def parse_args(args: list):
    ''' Adds settings and returns these parameters '''
    
    parser = argparse.ArgumentParser(prog="ATM", description="Simulation between user and bank.")
    parser.add_argument("--version", action='version', version=f'%(prog)s version {VERSION}', help="Print version info")
    parser.add_argument("-l", "--load", action='store', help="Load a program session from saving file")

    return parser.parse_args(args)


def set_args(args) -> dict:
    ''' Sets the settings for the program to work and returns a dictionary with settings '''
    
    return {
        "version": VERSION,
        "load": args.load if args.load else False,
    }


def main():
    pass


if __name__ == "__main__":
    main()