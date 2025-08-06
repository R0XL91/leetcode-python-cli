import argparse

from utils.api import fetch_problem
from utils.utils import create_problem_structure, run_problem_tests


def main():
    parser = argparse.ArgumentParser(
        description="CLI to download LeetCode problems, generate structure, or run tests."
    )
    parser.add_argument(
        'action', choices=['fetch', 'test'],
        help='Action to perform: fetch or test'
    )
    parser.add_argument(
        'name', type=str,
        help='Problem slug (for fetch) or test name (for test)'
    )
    parser.add_argument(
        '--path', type=str, default='problems',
        help='Path to the problems directory (default: problems)'
    )
    args = parser.parse_args()

    if args.action == 'fetch':
        try:
            problem = fetch_problem(slug=args.name)
            create_problem_structure(problem=problem, path=args.path)
        except (RuntimeError, ValueError) as e:
            print(f"Error: {e}")
    elif args.action == 'test':
        run_problem_tests(slug=args.name, path=args.path)


if __name__ == "__main__":
    main()
