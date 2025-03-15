import pandas as pd
import requests
import ast


# function for converting a headline list of words to a string in headlines array

# Importing the dataset as pandas dataframe:-

# __make fnc

def ltos(url):
    response = requests.get(url)
    data = response.text.splitlines()  # Split into lines

    # Convert each line from string to list
    headlines = [ast.literal_eval(line) for line in data]  # Safely convert string list to actual list

    # Create a DataFrame
    df_true = pd.DataFrame({"headlines": headlines})
    df = df_true.copy(deep=True)

    df["headline_text"] = df["headlines"].apply(lambda x: " ".join(x))  # Join list elements with a space, i.e makes Full String
    print(df.head())

ltos("https://raw.githubusercontent.com/Lakshya8600/stockmarket_ML__XGB_CNN/refs/heads/main/data/20200315.csv")