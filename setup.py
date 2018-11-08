import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ticket_universe',
    version='0.2',
    description='Toolset to generate ticket universes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/lotify/ticket_universe',
    author='Eelke van den Bos',
    author_email='eelke@moddix.com',
    license='MIT',
    packages=setuptools.find_packages(),
    scripts=['bin/ticket-universe'],
    zip_safe=False
)
