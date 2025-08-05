import argparse
import subprocess

from utils.api import fetch_problem
from utils.utils import create_problem_structure


def main():
    parser = argparse.ArgumentParser(
        description="CLI to download LeetCode problems, generate structure, or run tests."
    )
    parser.add_argument(
        'action', choices=['fetch', 'test'], help='Action to perform: fetch or test'
    )
    parser.add_argument(
        'name', type=str, help='Problem slug (for fetch) or test name (for test)'
    )
    args = parser.parse_args()

    if args.action == 'fetch':
        try:
            problem = fetch_problem(args.name)
            create_problem_structure(problem)
        except (RuntimeError, ValueError) as e:
            print(f"Error: {e}")
    elif args.action == 'test':
        # Run pytest for the specified test
        test_path = f"problems/tests/{args.name}/test.py"
        subprocess.run(['pytest', '-s', test_path], check=False)


if __name__ == "__main__":
    main()
