from setuptools import setup, find_packages

with open('README.md') as readme_file:
    long_description = readme_file.read()

setup(
    name='html-to-csv',
    version='0.0.2',
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
        'Programming Language :: Python :: 3.7',
    ],
    keywords='html table csv convert',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.7',
    install_requires=['beautifulsoup4', 'lxml'],
    entry_points={
        'console_scripts': [
            'html2csv=html2csv.__main__:main',
        ],
    },
)
