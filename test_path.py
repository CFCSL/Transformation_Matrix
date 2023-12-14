#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 00:38:12 2023

@author: namnguyen
"""

import pandas as pd
import os
file_path=os.path.abspath("Pylon-Deformations-Original.xlsx")
df=pd.read_excel(file_path)