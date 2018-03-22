from setuptools import setup, find_packages

setup(
    name = 'pycli',
    version = '0.1.0',
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
        'Click==6.6'
        # other libs go here
    ],
    entry_points = {
        'console_scripts': [
            'pycli = pycli.__main__:main'
            'quicktest = pycli.tests.quicktest:quicktest'
        ]
    })