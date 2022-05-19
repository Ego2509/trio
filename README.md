# Trio: Python library to compare 3 different sets of data/dataframes/exomes and get the matching variants (regions of a Venn diagram)
![Group of Primmary Immunodeficiencies](https://ibb.co/f0ZqXJ2)

This set of functions allows to export the matching Venn spaces onto a dataframe and visualize the result on a Venn diagram.

## Features
- Customizable column filtering (props_)
- Export the obtained region using the pandas.DataFrame object
- Draw the Venn Diagram with the given filters with the Venn3 python library and customize it with Vtags

## Installation
Start by downloading the folling libraries to your virtual environment
```sh
(your-venv)$ pip install pandas matplotlib_venn
```
On your working directory, download the functions
```sh
cd my_project
wget https://raw.githubusercontent.com/Ego2509/trio/main/trio.py
```
Import the libraries on your python script or notebook
```py
import numpy as np
import pandas as pd 
from matplotlib_venn import venn3_unweighted as venn3
import trio
```
And there we go! If you want to see some examples and cases, please refer to the following [python notebook](https://ego2509.github.io/trio/).


## License

MIT
