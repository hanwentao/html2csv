import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent
long_description = (here / 'README.md').read_text()
about = {}
exec((here / 'html2csv' / 'version.py').read_text(), about)

setup(
    name='html-to-csv',
    version=about['__version__'],
    description='A utility that extracts tables from HTML documents and converts them to CSV format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hanwentao/html2csv',
    author='Wentao Han',
    author_email='wentao.han@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='html table csv convert',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.6, <4',
    install_requires=['beautifulsoup4', 'lxml', 'requests'],
    extras_require={
        'dev': ['setuptools', 'wheel', 'twine'],
        'test': ['pytest', 'tox'],
    },
    entry_points={
        'console_scripts': [
            'html2csv=html2csv.__main__:main',
        ],
    },
)
