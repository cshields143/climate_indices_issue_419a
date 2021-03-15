import pathlib
from setuptools import find_packages, setup

BASE_DIR = pathlib.Path(__file__).parent
README = (BASE_DIR / 'README').read_text()

setup(
    name="dostuff",
    version="1.4.3",
    url="https://192.168.0.1/",
    license="n/a",
    author="Chris Shields",
    author_email="christopher.shields143@gmail.com",
    description=(
        "this is not a description"
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "scipy",
        "numpy"
    ],
    keywords=[
        "not", "production", "ready"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers of climate_indices"
    ]
)
