from setuptools import setup, find_packages

setup(
    name         = "bundler27",
    version      = "0.0.0",
    author       = "Daehyub Kim with Hajime Takase",
    author_email = "lateau@gmail.com",
    license      = "GPLv3",
    keywords     = "bundler",
    description  = "Ruby bundler liked package bundler",
    url          = "https://github.com/lateau/bundler27",
    packages     = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe     = True,
    install_requires = ['pip']
)
