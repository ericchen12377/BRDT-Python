import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brdt",
    version="0.1.0",
    author="Suiyao Chen",
    author_email="csycsy12377@gmail.com",
    description="Binomial Reliability Demonstration Tests Design",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericchen12377/BRDT-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)