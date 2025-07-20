# Analysis Grand Challenge of the PHYSLITE data format
The code in this repository was developed as a deliverable of the [IRIS-HEP fellow project](https://iris-hep.org/fellows/Denys-Klekots.html).
This code here heavily relies on [IRIS-HEP AGC demonstration in Binder](https://github.com/alexander-held/PyHEP-2022-AGC?tab=readme-ov-file) repository.

## Content of the repository

+ The primary files are the Jupyter notebooks named `main_code_virtual.ipynb` and `main_code_dask.ipynb`, which contain the code, its description and resulting outputs.
+ The only difference is that the "virtual" notebook is uses virtual arrays while the "dask" notebook uses `dask-awkward`.
+ The directory `utils` contains the pictures used in the markdown description of the main code notebooks.
+ The directory `index_files` contains text files with URLs by which code retrieves the data to do analysis.
+ The file `file_utils.py` contains a utility code for setting up the data retrieval from a remote server.
+ The file `metadata.csv` contains the metadata of the files that are retrieved from the server during analysis.
+ The file `cabinetry_config.yml` is the configuration of the [cabinetry](https://github.com/scikit-hep/cabinetry/) library used for the analysis.

## How to run?

The code was tested on the [coffea-opendata.casa](https://coffea-opendata.casa/) cluster with the coffea 2025 server option, it contains all necessary packages already installed. For code usage open the `main_code_virtual.ipynb` or `main_code_dask.ipynb` Jupyter notebook files and start running cells.

## Abstract

The [Analysis Grand Challenge (AGC)](https://iris-hep.org/projects/agc.html) stand for testing of the software toolkits on a path from the input data to the resulting plots and other types of output. This repository aims to benchmark the compatibility of the new version of the PHYSLITE data format with the existing infrastructure of the high-energy physics Python packages as well as to provide an example of analysis which one can do for the data stored in PHYSLITE format. For this analysis, the Monte Carlo generated open data of the ATLAS collaboration, released together with the [physical data](https://atlas.cern/Updates/News/Open-Data-Research), measured on the LHC during 2015 and 2016 was used.

## Acknowledgements

This work was supported by the Institute for Research and Innovation in Software for High Energy Physics ([IRIS-HEP](https://iris-hep.org/)) [![NSF-2323298](https://img.shields.io/badge/NSF-2323298-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=2323298)

The initial implementation of this project was the work of [Denys Klekots](https://github.com/Denys-Klekots)'s 2024 IRIS-HEP Fellow project: [Analysis Grand Challenge with ATLAS PHYSLITE data](https://iris-hep.org/fellows/Denys-Klekots.html).
