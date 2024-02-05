# Venvception

[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/moradology/venvception/cicd.yml?style=for-the-badge)](https://github.com/moradology/venvception/actions/workflows/cicd.yml)

Venvception is a Python library designed to simplify the process of creating and using temporary virtual environments within your Python applications. It provides a convenient context manager that automates the setup of a virtual environment, installs specified packages from a `requirements.txt` file, and ensures that the environment is used for the duration of the context.

![venvception in action](venvception.png)

## Features

- **Easy Virtual Environment Creation**: Automatically creates a temporary virtual environment.
- **Dependency Management**: Installs packages from a given `requirements.txt` file into the virtual environment.
- **Context Manager**: Ensures that the virtual environment is activated within the context and properly cleaned up afterwards.
- **Path Access**: Provides access to the path of the temporary virtual environment for further manipulation or inspection.

## Installation

To install Venvception, run the following command:

```bash
pip install venvception
```

## Quick Start

Here's a simple example to get started with Venvception:

```python
from venvception import venv

# Specify the path to your requirements file
requirements_path = "path/to/your/requirements.txt"

# Use the venv context manager to create and activate the virtual environment
with venv(requirements_path) as venv_path:
    # Import a module from the requirements.txt
    import your_module

    # You can also access the path to the virtual environment via `venv_path`
    print(f"Virtual environment created at: {venv_path}")
```

Ensure your `requirements.txt` file is properly formatted and accessible at the specified path.

## Usage

### Creating a Temporary Virtual Environment

Venvception uses a context manager to handle the creation, activation, and deletion of the temporary virtual environment. To use it, simply call `venv` with the path to your `requirements.txt`:

```python
with venv(Path("requirements.txt")) as venv_path:
    # Your code here
```

### Installing Packages

Specify the packages you need in a `requirements.txt` file, and Venvception will install them into the temporary virtual environment upon entering the context.

### Accessing the Virtual Environment

The context manager yields the path to the temporary virtual environment, allowing you to interact with it directly:

```python
with venv(Path("requirements.txt")) as venv_path:
    print(venv_path)
```

## Contributing

Contributions to Venvception are welcome! Please feel free to submit pull requests, report bugs, or suggest features through the issue tracker.

## License

Venvception is released under the [MIT License](LICENSE).
