import pandas as pd 

df = pd.read_csv('data/Co2_data_canada.csv')
# only keep the variable we require
# Engine size, cylinders and combine milege per gallon
final_df = df[['ENGINE SIZE','CYLINDERS','COMB_mpg']]