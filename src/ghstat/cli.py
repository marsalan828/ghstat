import argparse
from dataclasses import dataclass

def main():
    parser = argparse.ArgumentParser(description="Show a summary of a GitHub user's public repos")
    parser.add_argument("user", help="GitHub username, e.g. ghstat torvalds")
    args = parser.parse_args()
    print(args.user)

@dataclass
class experiment:
    n: int = "5"