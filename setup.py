from setuptools import setup, find_packages

setup(
    name='pypkg',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/joehinmoro/pypkg',
    author='Joshua Ehinmoro',
    author_email='joehinmoro@gmail.com'
)