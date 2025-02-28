import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="irawatch",
    version="0.1.0",
    author="Daryl Correa (Epicode)",
    author_email="daryl.correa@epicode.in",
    description="IraWatch Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darylac/irawatch",
    project_urls = {
        "Bug Tracker": "https://github.com/darylac/irawatch/issues"
    },
    license="MIT",
    packages=["irawatch"],
    install_requires=[
        "nats-py >= 2.9.0", 
        "protobuf >= 5.29.3",
    ]
)