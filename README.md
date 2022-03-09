# flight-fare-prediction

This repo is for a live-coding demo event organised by UKEC. 

## What is it?
It covers the typical process of building a machine learning model to predict flight fares.

Dataset is provided in the form of a CSV file. Please refer to `flight_dataset.csv` for the dataset.

<br>

## Notebooks
Please refer to `unfilled_demo.ipynb` during the session to learn and code along. 

You can always refer to `completed_demo.ipynb` for the complete solution and code covered in the session.

<br>

## Environmnet Setup
It's advisable to have a virtual environment to avoid any conflicts with other packages (in other projects)

<br>

### Conda Environment
If you are using `conda`, you can create the conda environment by running the commnand: 

```
conda env create -f environment.yml  
```

Then, activate the conda environment by executing

```
conda activate flight-fare
```

<br>


If you don't have `conda` (or `miniconda`, `conda-forge`) installed, you can still use `venv` and run 

```
python venv flight-fare
```

and run the following command to activate the environment:

```
source flight-fare/bin/activate
```

To install the packages: 

```
pip install -r requirements.txt
```