import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("user")
    args = parser.parse_args()
    print(args.user)