from distutils.core import setup

setup(
    name='social-media-count',
    version='0.1dev',
    author='Bram Driesen',
    author_email='bram.opensource@gmail.com',
    packages=['social-media-count'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Library to fetch likes/followers from multiple platforms.',
    long_description=open('README.txt').read(),
    install_requires=[
        'tweepy>=3.5.0',
    ],
)
