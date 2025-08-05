# LeetCode CLI

LeetCode CLI is a Python 3 command-line tool to download LeetCode problems, generate documentation, solution files, and test templates for each requested problem. Each problem is organized in its own folder structure for easy practice and testing.

## Features
- Download problem statements from LeetCode using the problem slug.
- Automatically generate a folder structure for each problem:
  - `README.md` with the problem description and sample cases.
  - Python solution file with function/class signature and type hints.
  - Pytest-compatible test file with sample cases ready to fill in.
- Supports Jinja2 templates for easy customization of generated files.
- Organizes problems in `problems/src/<slug>` and tests in `problems/tests/<slug>`.
- Imports and runs solution code dynamically for flexible testing.
- CLI interface to fetch problems or run tests by slug.

## Installation
1. Clone this repository.
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. (Optional) Create and activate a virtual environment.

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

### Run tests for a problem
Run the tests for a specific problem (e.g., `two-sum`):
```bash
python main.py test two-sum
```
This will execute pytest on `problems/tests/two-sum/test.py`.

### Example test file
The generated test file uses pytest and is ready for you to fill in expected values:
```python
import pytest
from utils.utils import import_problem_module

two_sum = import_problem_module("two-sum")

@pytest.mark.parametrize('args,expected', [
    (([2,7,11,15], 9), None),
    (([3,2,4], 6), None),
    (([3,3], 6), None),
])
def test_solution(args, expected):
    # result = two_sum.Solution().your_method(*args)
    assert 1 == 1  # Replace with your assertion
```

## Customization
- Edit the Jinja2 templates in the `templates/` folder to change the format of generated files.
- The CLI and code structure are extensible for new features.

## Requirements
- Python 3.8+
- requests
- pytest
- jinja2

## Troubleshooting
- If you want to debug with ipdb, run pytest with the `-s` flag: `python -m pytest -s problems/tests/two-sum/test.py`

## License
MIT
