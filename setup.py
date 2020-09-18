import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="usbmuxwrapper",
    version="0.0.3",
    author="Patrick Meenan",
    author_email="pmeenan@webpagetest.org",
    description="Python wrapper for usbmux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pmeenan/usbmux_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)