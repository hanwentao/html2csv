import setuptools

with open('README.md') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='html2csv',
    version='0.0.1',
    author='Wentao Han',
    author_email='wentao.han@gmail.com',
    description='A utility that extracts tables from html documents and converts them to csv format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hanwentao/html2csv',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
