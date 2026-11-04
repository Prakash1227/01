from pathlib import Path
from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Reads requirements from a file, stripping whitespace and filtering out comments and '-e .'."""
    requirements: List[str] = []
    path = Path(file_path)

    if not path.is_file():
        return requirements

    with open(path, "r", encoding="utf-8") as file_obj:
        for line in file_obj:
            line = line.strip()
            # Ignore empty lines and comment lines
            if not line or line.startswith("#"):
                continue
            if line == HYPHEN_E_DOT:
                continue
            requirements.append(line)

    return requirements


setup(
    name="fault_detection",
    version="0.0.1",
    author="Prakash Verma",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)