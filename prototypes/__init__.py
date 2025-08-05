import re
from dataclasses import dataclass


@dataclass
class Problem:
    id: str
    frontend_id: str
    title: str
    slug: str
    difficulty: str
    content: str
    code: str
    example_test_cases: str
    sample_test_case: str
    num_args: int = 0

    def get_num_args(self):
        """Get the number of arguments for the solution function."""
        match = re.search(r'def\s+\w+\s*\(([^)]*)\)', self.code, re.DOTALL)
        if not match:
            return 0
        args = [p.strip() for p in match.group(1).split(',') if p.strip()]
        num_args = len(args)
        if args and args[0] == 'self':
            return num_args - 1
        return num_args

    def extract_example_cases(self):
        """Extract example test cases from the problem's example_test_cases."""
        example_args = self.example_test_cases.strip().split('\n')
        num_args = self.get_num_args()
        return [
            example_args[i:i + num_args] for i in range(0, len(example_args) - len(example_args) % num_args, num_args)
        ]

    def get_slug_underscored(self):
        """Get the slug with underscores instead of hyphens."""
        return self.slug.replace('-', '_')

    def get_method_name(self):
        """Get the last method name defined in the Solution class."""
        # Find the Solution class block
        class_match = re.search(r'class\s+Solution\s*:\s*(.*?)(^class\s|\Z)', self.code, re.DOTALL | re.MULTILINE)
        if not class_match:
            return None
        class_body = class_match.group(1)
        # Find all method definitions inside the class
        methods = re.findall(r'def\s+(\w+)\s*\(', class_body)
        if not methods:
            return None
        return methods[-1]
