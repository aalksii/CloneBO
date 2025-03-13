from setuptools import setup, find_packages

setup(
    name="CloneBO",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas==2.1.4",
        "numpy==1.26.1",
        "torch",
        "tqdm",
        "transformers",
        "huggingface_hub",
        "hydra-core",
        "omegaconf",
        "wandb",
        "biopython",
        "termcolor",
        "pytorch-lightning",
        "scipy==1.11.2",
        "matplotlib",
        "p_tqdm",
        "transformers",
        "simplejson",
        "pydantic<2",
        "sru",
        "iglm",
        "pyarrow",
        "scikit-learn"
    ],
    python_requires="==3.12",
)
