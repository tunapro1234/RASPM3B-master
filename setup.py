from setuptools import setup

def readme():
    with open("README.txt") as f:
        return f.read()


with open("nuke/VERSION") as f:
    __version__ = f.read()


setup(
    name="RASPI-MAINBOARD-3B",
    version=__version__,
    description="tunapro1",
    long_description=readme(),
    url="http://github.com/FRC7839/NightVision/",
    author="TUNAPRO1234",
    author_email="tunagul54@gmail.com",
    license="MIT",
    packages=["raspm3b"],
    entry_points={"console_scripts": ["nuke=nuke.main:main"],},
    include_package_data=True,
    install_requires=["colorama", "selenium", "pynput", "tk-tools"],
    zip_safe=False,
)
