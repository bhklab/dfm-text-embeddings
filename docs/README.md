# DFM - Text Embeddings

**Authors:** [James Bannon](https://github.com/jbannon)

**Contact:** [bhklab.jamesbannon@gmail.com](mailto:bhklab.jamesbannon@gmail.com)

**Description:** Embeddings from SMILES strings

--------------------------------------

[![pixi-badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json&style=flat-square)](https://github.com/prefix-dev/pixi)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square)](https://github.com/astral-sh/ruff)
[![Built with Material for MkDocs](https://img.shields.io/badge/mkdocs--material-gray?logo=materialformkdocs&style=flat-square)](https://github.com/squidfunk/mkdocs-material)

![GitHub last commit](https://img.shields.io/github/last-commit/bhklab/dfm-text-embeddings?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/bhklab/dfm-text-embeddings?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/bhklab/dfm-text-embeddings?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/bhklab/dfm-text-embeddings?style=flat-square)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/bhklab/dfm-text-embeddings?style=flat-square)

## Set Up

### Prerequisites

Pixi is required to run this project.
If you haven't installed it yet, [follow these instructions](https://pixi.sh/latest/)

### Installation

1. Clone this repository to your local machine
2. Navigate to the project directory
3. Set up the environment using Pixi:

```bash
pixi install
```


## Data Collection

Navigate to the [ORCESTRA site](https://www.orcestra.ca/annotations/69f4a753f9dd88b7003f0326) for the HDDv2 and download the  `colData.csv` to the `data/rawdata/` folder. 


## Understanding the Data
The data used is the collection of approx 500k compounds from the Harmonized Drug Dataset (HDD). The embeddings here are constructed using the pre-trained [SMILES](https://en.wikipedia.org/wiki/Simplified_Molecular_Input_Line_Entry_System)-based language model called [ChemBERTa](https://arxiv.org/pdf/2010.09885). 

ChemBERTA provides *token-level* embeddings, meaning a vector for each character in a SMILES strings. The final embeddings provided here are the average embeddings across the entire string and have 768 dimensions. 

## Running the Code

Once you have installed the repository and the pixi environment navigate to the scripts folder `workflow/scripts/` and execute the command

```pixi run 'python3 make-chemberta-embeddings.py'```

By default this will only generate embeddings for the ~2000 compounds for which we have MOA data. Go to the file and set `MOA_ONLY` to `False` to get embeddings for all compounds. 



