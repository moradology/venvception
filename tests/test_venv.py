from pathlib import Path

from venvception import venv


def test_venv_assumption():
    with venv(Path("tests/fixtures/requirements.txt")) as venv_path:
        # Import module in ./requirements.txt
        import ulid

        # Verify that it is being installed from the virtual environment we created
        assert Path(ulid.__file__).relative_to(venv_path)
