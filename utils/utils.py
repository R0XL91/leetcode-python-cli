import importlib.util
import os
import subprocess
import sys
from typing import List

from jinja2 import Environment, FileSystemLoader

from prototypes import Problem


def create_src_dir(problem: Problem, env: Environment, path: str = "problems"):
    """Create the src directory for a LeetCode problem."""
    base_dir = get_path([path, "src", problem.slug])
    os.makedirs(base_dir, exist_ok=True)
    # Create README.md and solution.py using Jinja2 templates
    readme_template = env.get_template("README.md.j2")
    with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_template.render(problem=problem))
    solution_template = env.get_template("solution.py.j2")
    with open(os.path.join(base_dir, f"{problem.slug}.py"), "w", encoding="utf-8") as f:
        f.write(solution_template.render(problem=problem))


def create_test_dir(problem: Problem, env: Environment, path: str = "problems"):
    """Create the test directory for a LeetCode problem."""
    test_dir = get_path([path, "tests", problem.slug])
    os.makedirs(test_dir, exist_ok=True)
    # Create test file using Jinja2 template
    test_template = env.get_template("test.py.j2")
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    with open(os.path.join(test_dir, "test.py"), "w", encoding="utf-8") as f:
        f.write(test_template.render(problem=problem, path=path, project_path=project_path))


def create_problem_structure(problem: Problem, path: str = "problems"):
    """Create the folder and files for a LeetCode problem using Jinja2 templates."""
    # Create src and test directory if it doesn't exist
    environment = Environment(
        loader=FileSystemLoader(os.path.join(os.getcwd(), "templates")),
        autoescape=False,
    )
    create_src_dir(problem, environment, path)
    create_test_dir(problem, environment, path)


def import_problem_module(slug: str, path: str = "problems"):
    """Import the problem module dynamically based on the slug."""
    module_name = slug
    module_path = get_path([path, "src", module_name, f"{module_name}.py"])
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    problem_module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = problem_module
    spec.loader.exec_module(problem_module)
    return problem_module


def run_problem_tests(slug: str, path: str = "problems"):
    path = get_path([path, "tests", slug, "test.py"])
    subprocess.run(['pytest', '-s', path], check=False)


def get_path(path: List[str]) -> str:
    """Get the absolute path for a given relative path."""
    path = f"{os.path.sep}".join(path)
    if not os.path.isabs(path):
        return os.path.join(os.getcwd(), path)
    return path
