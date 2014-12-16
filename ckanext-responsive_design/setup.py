from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-responsive_design',
    version=version,
    description="responsive design for ckan 2.2.2b (css from ckan 2.3)",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='JanosFarkas',
    author_email='farkas48@uniba.sk',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.responsive_design'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        responsive_design =ckanext.responsive_design.plugin:ResponsiveDesign
    ''',
)
