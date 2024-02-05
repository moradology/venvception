# Venvception

[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/moradology/venvception/cicd.yaml?style=for-the-badge)](https://github.com/moradology/venvception/actions/workflows/cicd.yaml)

Venvception is a Python library designed to simplify the process of creating and using temporary virtual environments when you have good reason to stay in the same process. It provides a context manager that automates the setup of a virtual environment, installs specified packages from a `requirements.txt` file, and ensures that the environment is used for the duration of the context.

![venvception in action](venvception.png)

## Why?

In distributed contexts, it can be convenient to ship a requirements specification rather than pre-baking containers. This library is quick and dirty.

## Installation

To install Venvception, run the following command:

```bash
pip install venvception
```

## Quick Start / Usage

Here's a simple example to get started with Venvception:

```python
from venvception import venv
from pathlib import Path

# Specify the path to your requirements file
requirements_path = Path("path/to/your/requirements.txt")

# Use the venv context manager to create and activate the virtual environment
with venv(requirements_path) as venv_path:
    # Import a module from the requirements.txt
    import your_module

    # You can also access the path to the virtual environment via `venv_path`
    print(f"Virtual environment created at: {venv_path}")
```

Ensure your `requirements.txt` file is properly formatted and accessible at the specified path.

### Accessing the Virtual Environment's Path

The context manager yields the path to the temporary virtual environment, allowing you to interact with it directly:

```python
with venv(Path("requirements.txt")) as venv_path:
    print(venv_path)
```

## Contributing

Contributions to Venvception are welcome! Please feel free to submit pull requests, report bugs, or suggest features through the issue tracker.

## License

Venvception is released under the [MIT License](LICENSE).
