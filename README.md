# LeetCode Python CLI

LeetCode CLI is a Python 3 command-line tool to download LeetCode problems, generate documentation, solution files, and test templates for each requested problem. Each problem is organized in its own folder structure for easy practice and testing.

## Features
- Download problem statements from LeetCode using the problem slug.
- Automatically generate a folder structure for each problem:
  - `README.md` with the problem description and sample cases.
  - Python solution file with function/class signature and type hints.
  - Pytest-compatible test file with sample cases ready to fill in.
- Supports Jinja2 templates for easy customization of generated files.
- Organizes problems in `src/<slug>` and tests in `tests/<slug>` under a configurable base directory.
- Imports and runs solution code dynamically for flexible testing.
- CLI interface to fetch problems or run tests by slug.
- **Custom directory support:** Use `--path` to specify where to save problems and tests.

## Installation
1. Clone this repository.
2. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage

### Fetch a LeetCode problem
Download and generate the structure for a problem (e.g., `two-sum`):
```bash
python main.py fetch two-sum
```
This will create:
- `problems/src/two-sum/README.md`
- `problems/src/two-sum/two-sum.py`
- `problems/tests/two-sum/test.py`

### Fetch a problem to a custom directory
You can specify a custom base directory for problems and tests:
```bash
python main.py fetch two-sum --path /tmp/problems/
```
This will create:
- `/tmp/problems/src/two-sum/README.md`
- `/tmp/problems/src/two-sum/two-sum.py`
- `/tmp/problems/tests/two-sum/test.py`

### Run tests for a problem
Run the tests for a specific problem (e.g., `two-sum`):
```bash
python main.py test two-sum
```
This will execute pytest on `problems/tests/two-sum/test.py`.

### Run tests for a problem in a custom directory
```bash
python main.py test two-sum --path /tmp/problems/
```
This will execute pytest on `/tmp/problems/tests/two-sum/test.py`.

### Example test file
The generated test file uses pytest and is ready for you to fill in expected values and method names.
Replace `your_method` with the actual method name from the solution class and update `expected` values.

```python
import pytest
from utils.utils import import_problem_module

# Import the solution module dynamically
two_sum = import_problem_module("two-sum", "/tmp/problems/")  # Use your path if needed

@pytest.mark.parametrize('args,expected', [
    # Fill in the expected output for each test case
    (([2,7,11,15], 9), None),
    (([3,2,4], 6), None),
    (([3,3], 6), None),
])
def test_solution(args, expected):
    # Replace 'twoSum' with the actual method name if different
    assert two_sum.Solution().twoSum(*args) == expected
```

**Tips:**
- The method name (`twoSum`) should match the one in your solution file.
- Update the `expected` values according to the problem statement.
- You can add more test cases in the `parametrize` decorator.

## Customization
- Edit the Jinja2 templates in the `templates/` folder to change the format of generated files.
- The CLI and code structure are extensible for new features.

## Requirements
- Python 3.8+
- requests
- pytest
- jinja2

Install dependencies:
```bash
pip install -r requirements.txt
```

## Troubleshooting
- The CLI automatically adjusts imports so tests work regardless of the chosen directory.

## Project Structure Example

```
problems/
├── src/
│   └── two-sum/
│       ├── README.md
│       └── two-sum.py
└── tests/
    └── two-sum/
        └── test.py
```
