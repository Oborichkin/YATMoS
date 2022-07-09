import setuptools

from yatmos import __version__


setuptools.setup(
    name="yatmos",
    packages=setuptools.find_packages(),
    version=__version__,
    description="Yet Another Test Managment System",
    author="Pavel Oborin",
    author_email="oborin.p@gmail.com",
    url="https://github.com/Oborichkin/yatmos",
    python_requires=">=3.6",
    install_requires=[
        "fastapi",
        "uvicorn[standard]",
        "sqlalchemy",
    ],
)
