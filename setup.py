#!/usr/bin/env python
"""
Install wagtail-accessibility using setuptools
"""

with open('README.rst', 'r') as f:
    readme = f.read()

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires = [
    'wagtail>=4.1',
]

tests_require = [
    "pytest==6.2.5",
    "pytest-cov==3.0.0",
    "pytest-django==4.5.0",
    "pytest-pythonpath==0.7.3",
    "coverage==6.0",
]

setup(
    name='wagtail-accessibility',
    version='0.2.1',
    description="A plugin to assist with accessibility when developing in Wagtail.",
    long_description=readme,
    author='Liam Brenner',
    author_email='liam@takeflight.com.au',
    url='https://github.com/takeflight/wagtail-accessibility',

    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
    },
    zip_safe=False,
    license='BSD License',

    packages=find_packages(),

    include_package_data=True,
    package_data={},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
)
