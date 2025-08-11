from setuptools import setup, find_packages

setup(
    name="pylibsrcml",
    version="1.1.0",
    description="A Pythonic binding of the libsrcml C library",
    long_description = open('README.md').read(),
    url = 'https://www.srcml.org/',
    author="srcML, LLC",
    author_email="srcmldev@gmail.com",
    license="GPL-3.0-or-later",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "pylibsrcml": ["testsuite/*"],
    },
    python_requires=">=3.7",
)