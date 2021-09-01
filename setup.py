#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='hansard',
    version='0.0.1',
    author='Telmo Menezes et al.',
    author_email='telmo@telmomenezes.net',
    description='Scraping the UK Parliament’s Official Report (Hansard).',
    url='https://github.com/cmb-css/hansard',
    license='MIT',
    keywords=['Data Science', 'Data Collection', 'Crawler', 'Extract Data',
              'Computational Social Science', 'Computational Sociology'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Topic :: Sociology'
    ],
    python_requires='>=3.4',
    packages=find_packages(),
    install_requires=[
        'bs4',
        'lxml',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        hansard=hansard.__main__:cli
    '''
)
