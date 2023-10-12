# Credit-Default-Prediction

## Overview

This repository contains jupyter notebook code and a flask application developed for a project focused on credit default prediction which is a critical task in the financial industry, where the goal is to predict whether a borrower will default on a loan.

## Project Description

In this project, we aim to develop a machine learning model for credit default prediction. The project includes the following key components:

- Data cleaning
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature selection
- Model selection and training
- Evaluation and validation

The project focuses on using various machine learning algorithms to build and evaluate credit default prediction models. The goal is to achieve a high level of f1-score, thus, robustness in predicting whether a loan applicant is likely to default.

## Data

The data used in this project can be found [here](https://data.world/jaypeedevlin/lending-club-loan-data-2007-11).

## Project Structure

The project structure is organized as follows:

- `notebook.ipynb`: Jupyter notebook code for data exploration, preprocessing, model development, and evaluation.
- `LCDataDictionary.csv`: the file that contains the description of each variable.
- `pipeline.pkl`: pkl file where the retained model is saved.
- `flask_app/` : directory containing a simple flask application used for prediction of loan default.
- `requirements.txt` : text file that contains the libraries and packages required to run the project.
