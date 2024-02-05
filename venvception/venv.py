import contextlib
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional
from venv import EnvBuilder


@contextlib.contextmanager
def venv(requirements_file: Path, env_id: Optional[str] = None):
    """
    Context manager to create a temporary virtual environment and install specified packages.

    Args:
        requirements_file (Path): Path to the requirements.txt file with package dependencies.
        env_id (Optional[str], optional): An identifier for the virtual environment. If not
                                           provided, a hash of the requirements file will be used.

    Yields:
        Path: The path to the created virtual environment.

    Raises:
        FileNotFoundError: If the requirements_file does not exist.
    """
    if not requirements_file.exists():
        raise FileNotFoundError(f"{requirements_file} does not exist.")

    env_prefix = env_id or hash_file_id(requirements_file)
    with tempfile.TemporaryDirectory(prefix=env_prefix) as tempdir:
        env_path = Path(tempdir)

        builder = EnvBuilder(with_pip=True)
        builder.create(str(env_path))

        pip_install(env_path, requirements_file)

        original_sys_path = list(sys.path)
        activate_virtualenv(env_path)

        try:
            yield env_path
        finally:
            sys.path[:] = original_sys_path


def hash_file_id(filepath: Path) -> str:
    """
    Computes the SHA-256 hash of requirements file to enable reuse of virtualenv.

    Args:
        filepath (Path): Path to the file to be hashed.

    Returns:
        str: The hexadecimal digest of the file hash.
    """
    hash_sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            hash_sha256.update(chunk)

    return hash_sha256.hexdigest()


def get_pip_path(env_dir: Path) -> Path:
    """
    Determines the path to the pip executable within a given virtual environment.

    Args:
        env_dir (Path): The root directory of the virtual environment.

    Returns:
        Path: The path to the pip executable.
    """
    if sys.platform == "win32":
        return env_dir / "Scripts" / "pip.exe"
    else:
        return env_dir / "bin" / "pip"


def pip_install(env_dir: Path, requirements_file: Path) -> None:
    """
    Installs packages from a requirements file into the specified virtual environment.

    Args:
        env_dir (Path): The root directory of the virtual environment.
        requirements_file (Path): Path to the requirements.txt file with package dependencies.
    """
    pip_executable = get_pip_path(env_dir)
    subprocess.check_call([pip_executable, "install", "-r", requirements_file])


def activate_virtualenv(env_dir: Path) -> None:
    """
    Modifies sys.path to activate a given virtual environment.

    Args:
        env_dir (Path): The root directory of the virtual environment.
    """
    site_packages_path = (
        env_dir
        / "lib"
        / f"python{sys.version_info.major}.{sys.version_info.minor}"
        / "site-packages"
    )
    sys.path.insert(0, str(site_packages_path))
