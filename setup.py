# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from djangocms_accordion import __version__

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Framework :: Django',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

REQUIREMENTS = [
    'django>=1.8',
    'django-cms>=3.4',
]

setup(
    name="djangocms-simple-accordion",
    version=__version__,
    url='https://github.com/Blueshoe/djangocms-simple-accordion',
    license='MIT',
    description="Django-CMS Plugin for accordion tabs. It's easy to style and does not rely on big dependencies",
    long_description=open('README.rst').read(),
    author='Maximilian Muth',
    author_email='kontakt@maxi-muth.de',
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    keywords=['django', 'Django CMS', 'accordion', 'tab', 'accordion-tab'],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False,
)
