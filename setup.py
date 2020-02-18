from setuptools import setup

setup(
    name="FTPm",
    version="0.1.0",
    description="Freelance Time and Project Management CLI",
    author="Ole Zierau",
    author_email="kontakt@olezierau.de",
    packages=["FTPm"],
    scripts=["bin/ftpm"],
    install_requires=[
        "appnope==0.1.0",
        "autopep8==1.5",
        "backcall==0.1.0",
        "certifi==2019.11.28",
        "chardet==3.0.4",
        "Click==7.0",
        "decorator==4.4.1",
        "idna==2.8",
        "ipykernel==5.1.4",
        "ipython==7.12.0",
        "ipython-genutils==0.2.0",
        "jedi==0.16.0",
        "Jinja2==2.11.1",
        "jupyter-client==5.3.4",
        "jupyter-core==4.6.2",
        "MarkupSafe==1.1.1",
        "numexpr==2.7.1",
        "numpy==1.18.1",
        "pandas==1.0.1",
        "parso==0.6.1",
        "pexpect==4.8.0",
        "pickleshare==0.7.5",
        "prompt-toolkit==3.0.3",
        "ptyprocess==0.6.0",
        "pycodestyle==2.5.0",
        "Pygments==2.5.2",
        "python-dateutil==2.8.1",
        "pytz==2019.3",
        "PyYAML==5.3",
        "pyzmq==18.1.1",
        "requests==2.22.0",
        "six==1.14.0",
        "tables==3.6.1",
        "tornado==6.0.3",
        "traitlets==4.3.3",
        "urllib3==1.25.8",
        "wcwidth==0.1.8",
    ],
)
