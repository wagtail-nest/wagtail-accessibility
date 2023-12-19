#!/usr/bin/env python

from setuptools import find_packages, setup  # type: ignore

with open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()


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
    version='1.0.0',
    description="A plugin to assist with accessibility when developing in Wagtail.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Wagtail Nest contributors',
    author_email='hello@wagtail.org',
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
