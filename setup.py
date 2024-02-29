#!/usr/bin/env python

from setuptools import find_packages, setup  # type: ignore

with open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()


install_requires = [
    'wagtail>=5.2',
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
    version='2.0.0',
    description="Accessibility content checks for Wagtail websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Wagtail Nest contributors',
    author_email='hello@wagtail.org',
    url='https://github.com/wagtail-nest/wagtail-accessibility',

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
        'Development Status :: 5 - Production/Stable',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 5",
        "Framework :: Wagtail :: 6",
        'License :: OSI Approved :: BSD License',
    ],
)
