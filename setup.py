from setuptools import setup, find_packages

long_desc = """
Wraps the Zoopla API.
"""
# See https://pypi.python.org/pypi?%3Aaction=list_classifiers for classifiers

setup(
    name='zoopla',
    version='0.0.1',
    description="Wraps the Zoopla API.",
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Paul Furley',
    author_email='paul@paulfurley.com',
    url='http://paulfurley.com',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'requests',
        'requests-cache'
    ],
    tests_require=[],
    entry_points=\
    """
    """,
)
