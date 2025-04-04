from setuptools import setup, find_packages

setup(
    name="pushinpay",
    version="0.1.0",
    description="Wrapper para a API PushinPay",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ricardo Santos",
    author_email="ricardotenv@gmail.com",
    url="",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
