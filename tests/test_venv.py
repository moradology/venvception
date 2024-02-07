import os
import subprocess
from pathlib import Path

from venvception import venv

def test_subprocess_uses_venv_python():
    with venv(Path("tests/fixtures/requirements.txt")) as venv_path:
        # Execute Python within the subprocess to print its executable path
        output = subprocess.check_output([str(venv_path / 'bin' / 'python'), '-c', 'import sys; print(sys.executable)'], text=True)

        # Verify that the subprocess uses the Python interpreter from the virtual environment
        assert str(venv_path / 'bin' / 'python') in output.strip()

def test_venv_assumption():
    with venv(Path("tests/fixtures/requirements.txt")) as venv_path:
        # Import module in ./requirements.txt
        import ulid

        # Verify that it is being installed from the virtual environment we created
        assert Path(ulid.__file__).relative_to(venv_path)

def test_environment_reverted_after_context():
    original_path = os.environ['PATH']
    with venv(Path("tests/fixtures/requirements.txt")):
        pass  # Just enter and exit the context

    # Verify that the PATH environment variable is reverted to its original value after exiting the context
    assert os.environ['PATH'] == original_path