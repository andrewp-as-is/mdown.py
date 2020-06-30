import setuptools

setuptools.setup(
    name='mdown',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
