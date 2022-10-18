import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgk-demo",
    version="0.0.1",
    author="Spectrum75",
    # author_email="",
    description="Testing installation of Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spectrum75/pkg-demo",
    # project_urls = {
    #     "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    # },
    license="MIT",
    packages=["pkg-demo"],
    install_requires=["requests"],
)