import setuptools


setuptools.setup(
    name="yatmos",
    packages=setuptools.find_packages(),
    version="0.1.0",
    description="Yet Another Test Managment System",
    author="Pavel Oborin",
    author_email="oborin.p@gmail.com",
    url="https://github.com/Oborichkin/yatmos",
    python_requires=">=3.6",
    install_requires=[
        "fastapi",
        "uvicorn[standard]",
        "sqlalchemy",
        "psycopg2",
        "junitparser"
    ],
    entry_points={
        "console_scripts": [
            # ржунит, read junit
            'rjunit = yatmos.plugins.junit:main'
        ]
    }
)
