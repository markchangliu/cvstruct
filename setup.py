from setuptools import setup, find_packages

setup(
    name = "cvstruct",
    python_requires = ">=3.8",
    install_requires = [
        "numpy",
        "pycocotools"
    ],
    extras_require = {
        "gui": ["opencv-python"],
        "no_gui": ["opencv-python-headless"]
    },
    packages = find_packages(),
    setup_requires = ['setuptools_scm'],
)