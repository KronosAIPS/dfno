from setuptools import setup, find_packages

requirements = ['distdl @ git+https://github.com/KronosAIPS/distdl.git@cuda-aware-2', 'mat73', 'matplotlib', 'mpi4py', 'numpy', 'scipy', 'torch']

setup(
    name = 'dfno',
    version = '0.2',
    author = 'Thomas Grady',
    author_email = 'tgrady@gatech.edu',
    license = 'MIT',
    install_requires=requirements,
    packages = find_packages(),
    description = 'Distributed Fourier Neural Operator based on DistDL')
