from setuptools import setup, find_packages


setup(
    name='markdown-prism',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/necan/markdown-prism',
    license='MIT',
    install_requires=['markdown'],
    author='necan',
    author_email='necan@qq.com',
    description='prism extension for Python Markdown'
)
