# This code also contains a function to calculate indicator 1,0,-1 logic (function-1)

import os
import pandas as pd
import csv
import re

# Define paths
base_dir = os.path.dirname(__file__)  
f_path = os.path.join(base_dir, "stock_data_modified_csvs")

def indicator(stock,b=3):
        
    path = os.path.join(base_dir, "stock_data_csvs", f"{stock}.csv")

    # Read CSV
    df_true = pd.read_csv(path)
    df = df_true.copy(deep=True)

    b = 3

    # Calculate percentage change
    df["p_change"] = 100 * ((df["Close"] - df["Open"]) / df["Open"])



    # Create indicator column in df before copying
    df["indicator"] = df["p_change"].apply(lambda x: 1 if x > b else (-1 if x < -b else 0))

    # Now create df_change as a DataFrame with both columns
    df_change = df[["Date","p_change", "indicator"]].copy(deep=True)

    # print(df_change.head(20))

    file_path = os.path.join(f_path, f"{stock}_indicator.csv")
    df_change.to_csv(file_path,index=False)

stock_name_path = os.path.join(base_dir,"CompanyNames.csv")
with open(stock_name_path,mode='r',newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        company_name = row[0].strip()
        company_name_ = company_name.replace(".NS","")
        company_name_ = re.sub(r'[^\w]','_',company_name_)
        indicator(company_name_)
