# FUNCTION-2:-
# INPUT:- csv path
# OUTPUT:- a dataframe containing list of words + string
# WHY:- to get the headline from 'list of words' representation to string representation 

import pandas as pd
import requests
import ast
import os


# function for converting a headline list of words to a string in headlines array

def ltos(csv_path):
    with open(csv_path, "r", encoding="utf-8") as file:
        data = file.readlines()  # Read all lines from the file

    # Convert each line from string to list
    headlines = [ast.literal_eval(line.strip()) for line in data]  # Safely convert string list to actual list

    # Create a DataFrame
    df_true = pd.DataFrame({"headlines": headlines})

    # Print first 5 rows
    # print(df_true.head())
    df = df_true.copy(deep=True)
    df["headline_text"] = df["headlines"].apply(lambda x: " ".join(x))  # Join list elements with a space, i.e makes Full String
    # print(df.head())
    return df

    


base_dir = os.path.dirname(__file__)  
save_path = os.path.join(base_dir,"news_data_string_lists")
directory_path = os.path.join(base_dir, "data")

file_list = os.listdir(directory_path)

for file_name in file_list:
    
    file_path = os.path.join(directory_path, file_name)
    if os.path.isfile(file_path):
        df = ltos(file_path)
        # saving file
        output_file_path = os.path.join(save_path, f"{file_name}_ls.csv")  # Define full file path
        df.to_csv(output_file_path,index=False)

