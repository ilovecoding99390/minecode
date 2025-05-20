from setuptools import setup, find_packages
setup(  
    name="minecode",  
    version="0.1.0",  
    author="Ezekiel Nogle",  
    description="A Python module that uses bed_apy",  
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",  
    packages=find_packages(),  
    install_requires=[
        bed_apy,
        asyncio,
        math,
        json,
        pillow,
        random
        
    ],  # Add dependencies here  
    classifiers=[  
        "Programming Language :: Python :: 3",  
        "License :: OSI Approved :: GNU General Public License v3 (GPL-3.0)",  
        "Operating System :: OS Independent",  
    ],  
    python_requires=">=3.8",  
)  
