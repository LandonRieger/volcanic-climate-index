# -*- coding: utf-8 -*-

import versioneer
from setuptools import setup, find_packages

setup(
    name='volcanic-climate-index',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='volcanic climate index',
    author='Landon Rieger',
    author_email='landon.rieger@canada.ca',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['bokeh', 'numpy', 'pandas', 'xarray', 'netcdf4'],
)
