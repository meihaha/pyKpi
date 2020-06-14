import pandas as pd
import numpy as np
import chardet
path1 = r'data/gongcan.csv'

with open(path1,'rb') as f:
    data = f.read()
    print(chardet.detect(data))


# gongcan  = pd.read_csv('data/gongcan.csv',encoding='utf-8',sep=',')