# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:14:52 2020

@author: OAdeoye
"""

import pandas as pd
import sklearn.datasets

def get_iris():
    ds = sklearn.datasets.load_iris()
    df = pd.DataFrame(ds['data'], columns = ds['feature_names'])
    code_species_map = dict(zip(range(3), ds['target_names']))
    df['species'] = [code_species_map[c] for c in ds['target']]
    return df