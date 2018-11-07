import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ticket_universe',
    version='0.1.3',
    description='Toolset to generate ticket universes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/lotify/ticket_universe',
    author='Eelke van den Bos',
    author_email='eelke@moddix.com',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False
)
