from setuptools import setup, find_namespace_packages

setup(
    name='Clean folder',
    version='0.0.1',
    description='HW 7. Clean folder',
    author='OSmit',
    author_email='oleg.smit@gmail.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean_folder=clean_folder.clean:start']}
)