import os
from setuptools import setup
from setuptools import find_packages


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='word_tornado',
    version="0.0.1",
    packages=find_packages(),
    python_modules=[],
    include_package_data=True,
    license='MIT',
    description='API for generating a word cloud for URLs you visit',
    author='Greg Lever',
    author_email='greglever@gmail.com',
    classifiers=[
        'Framework :: Tornado',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'tornado==5.1.1',
    ]
)
