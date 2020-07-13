# Run a Jupyter Notebook without a Web Browser

## Description

Jupyter notebooks are great. But it can be difficult to run longer experiments due to connectivity issues. If your browser connection to th jupyter kernel is interrrupted you may losse some output.
This is why I made a little utlity around [nbconvert](https://nbconvert.readthedocs.io/en/latest/) that let's you execute a notebook in a browser independent way.

## How to use ?

1. Put the notebook you want to run in the `notebooks` folder.
2. Run `python run_notebook.py` 
3. Choose the notebook you want to execute from command line select menu
4. Find a executed version version of the notebook with a timestamp in the same directory

## TODO
[] Find a way to track the notebook progress while executing