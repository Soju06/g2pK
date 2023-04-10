import setuptools

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'jamo',
    'nltk',
]

setuptools.setup(
    name="g2pK-msvc",
    version="0.9.3",
    author="Soju06",
    author_email="qlskssk@gmail.com",
    description="g2pK-msvc: MSVC Windows용 Mecab 한국어 g2p 모듈",
    install_requires=REQUIRED_PACKAGES,
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Soju06/g2pK-msvc",
    packages=setuptools.find_packages(),
    package_data={'g2pk-msvc': ['g2pk/idioms.txt', 'g2pk/rules.txt', 'g2pk/table.csv']},
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
