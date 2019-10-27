import pandas as pd 

#import data from csv

data = pd.read_csv("resources/Random_Results.csv")

df = pd.DataFrame(data)

df = df.drop(columns=['Unnamed: 0'])

df.to_html("resources/html_df.html")
