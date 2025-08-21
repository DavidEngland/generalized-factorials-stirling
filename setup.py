from setuptools import setup, find_packages

setup(
    name="generalized_stirling",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.19.0",
    ],
    python_requires=">=3.6",
    author="David England",
    author_email="DavidEngland@HotMail.com",
    description="A library for computing generalized Stirling numbers and related combinatorial sequences",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/generalized-factorials-stirling",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
