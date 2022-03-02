import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="summertime",
    version="1.2.1",
    author="Ansong Ni, Murori Mutuma, Troy Feng, Zhangir Azerbayev, Nick Schoelkopf, Yusen Zhang, Tao Yu, Dragomir Radev",
    author_email="ansong.ni@yale.edu, dragomir.radev@yale.edu",
    description="Text summarization toolkit for non-experts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yale-LILY/SummerTime",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    # package_dir={"": ""},
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    install_requires=[
        "cython",
        "numpy",  # installing summEval requires numpy to be install first, we put numpy first as a workaround
        "click==7.1.2",  # a workaround for resolving a dependency conflict
        "transformers~=4.5.1",
        "torch~=1.8",
        "lexrank~=0.1.0",
        "nltk==3.6.2",
        "spacy==3.0.6",
        "pytextrank",
        "datasets~=1.6.2",
        "sentencepiece~=0.1.95",
        "summ_eval==0.70",
        "jupyter",
        "gdown~=4.2.0",
        "readability-lxml",
        "beautifulsoup4",
        "orjson",
        "gensim~=3.8.3",
        "sklearn",
        "py7zr~=0.16.1",
        "tqdm~=4.49.0",
        "tensorboard~=2.4.1",
        "fasttext~=0.9.2",
        "black~=21.12b0",
        "easynmt~=2.0.1",
        "flake8",
        "progressbar",
        "prettytable",
    ],
)
