import setuptools
with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read
setuptools.setup(
    name="ScrewPY",
    version="0.0.1",
    author="Murillo Mario Alberto,Rodríguez González José Adrián",
    author_email="ja.rodriguez.g@ugto.mx, correoMurillo",
    description="A library that enhances and makes easier the use of screws on robotics",
    long_description_content_type="text/markdown",
    url="package URL",
    python_requires=">=3.9",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)