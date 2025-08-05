import importlib.util
import os
import sys

from jinja2 import Environment, FileSystemLoader

from prototypes import Problem


def create_src_dir(problem: Problem, env: Environment):
    """Create the src directory for a LeetCode problem."""
    base_dir = os.path.join(os.getcwd(), f"problems/src/{problem.slug}")
    os.makedirs(base_dir, exist_ok=True)
    # Create README.md and solution.py using Jinja2 templates
    readme_template = env.get_template("README.md.j2")
    with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_template.render(problem=problem))
    solution_template = env.get_template("solution.py.j2")
    with open(os.path.join(base_dir, f"{problem.slug}.py"), "w", encoding="utf-8") as f:
        f.write(solution_template.render(problem=problem))


def create_test_dir(problem: Problem, env: Environment):
    """Create the test directory for a LeetCode problem."""
    test_dir = os.path.join(os.getcwd(), f"problems/tests/{problem.slug}")
    os.makedirs(test_dir, exist_ok=True)
    # Create test file using Jinja2 template
    test_template = env.get_template("test.py.j2")
    with open(os.path.join(test_dir, "test.py"), "w", encoding="utf-8") as f:
        f.write(test_template.render(problem=problem))


def create_problem_structure(problem: Problem):
    """Create the folder and files for a LeetCode problem using Jinja2 templates."""
    # Create src and test directory if it doesn't exist
    environment = Environment(
        loader=FileSystemLoader(os.path.join(os.getcwd(), "templates")),
        autoescape=False,
    )
    create_src_dir(problem, environment)
    create_test_dir(problem, environment)


def import_problem_module(slug):
    module_name = slug
    module_path = f"{os.path.sep}".join(
        [os.getcwd(), "problems", "src", module_name, f"{module_name}.py"]
    )
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    problem_module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = problem_module
    spec.loader.exec_module(problem_module)

    return problem_module
