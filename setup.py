import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="holidays-plus",
    version="0.0.2",
    author="Sam Tregar",
    author_email="sam@tregar.com",
    description="Enhanced add-on for the holidays library offering expanded functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samtregar/python-holidays-plus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'holidays',
    ],
)
