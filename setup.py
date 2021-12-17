"""Package setup"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythonds3",
    version="3.1.0",
    author="Roman Yasinovskyy",
    author_email="yasinovskyy@gmail.com",
    description="Data Structures package for Problem Solving with Algorithms and Data Structures using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/psads/pythonds3",
    packages=setuptools.find_packages(),
    license="GPLv3+",
    platforms=["OS Independent"],
    keywords=[
        "Education",
        "Algorithms",
        "Data Structures",
        "Python",
        "Stack",
        "Queue",
        "Tree",
        "Graph",
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
    ),
)
