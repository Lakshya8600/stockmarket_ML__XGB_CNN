# ----CURRENT STATE OF IMPLEMENTATION FILE:------
# A logic made to make csv files per target headline containing date matched and stock probabilities



# ----------------------------------------------------------------------------------------------------
import pandas as pd
import os
import csv
import re
from datetime import datetime

# Function to check sentence similarity using BERT
def sent_sim(sent1, sent2, score=75):
    from sentence_transformers import SentenceTransformer, util
    model1 = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model1.encode([sent1, sent2], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    similarity_score = similarity.item()
    return 1 if similarity_score >= (score / 100) else 0

# Import CSV from today_headlines_csvs
def import_today(filename):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "today_headlines_csvs", f"{filename}_ls.csv")
    return pd.read_csv(path)

# Import CSV from news_data_string_lists
def import_news(filename):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "news_data_string_lists", f"{filename}.csv_ls.csv")
    return pd.read_csv(path)

# Function to get stock probabilities for given dates
def stp(stock, datelist):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "indicator_data_csvs", f"{stock}_indicator.csv")

    if not os.path.exists(path):
        return None  # Return None if file doesn't exist

    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df["date_only"] = pd.to_datetime(df["Date"], errors='coerce').dt.date
    df = df.dropna(subset=["date_only"])

    results = []
    for date_obj in datelist:
        filtered_row = df[df["date_only"] == date_obj]
        results.append(int(filtered_row["indicator"].values[0]) if not filtered_row.empty else None)

    if not any(results):  # If all values are None or empty
        return 0

    sum_results = sum(filter(None, results))
    nume = sum(1 for v in results if v == 1) if sum_results > 0 else sum(-1 for v in results if v == -1)

    return nume / len(results)
# --------------------------------------------------------------------------------------------------
# Implementation


# 1:- for comparing target headline with past news' headlines and storing a csv file per headline to stoc_prob_per_headline

today_headlines = import_today("20200313")

today = datetime.today()
date = int(today.strftime("%Y%m%d"))
base_dir = os.path.dirname(__file__)  
save_path = os.path.join(base_dir, "stock_prob_per_headline")

for i in range(len(today_headlines)):
    
    str1 = today_headlines.loc[i, "headline_text"]
    datelist = []

    for j in range(1096):  # Iterate through 3 years
        that_date = date - (j + 1)
        that_date = 20250312  # Hardcoded date for testing

        df = import_news(that_date)
        for k in range(len(df)):
            str2 = df.loc[k, "headline_text"]
            sim_bin = sent_sim(str1, str2)
            if sim_bin == 1 and that_date not in datelist:
                datelist.append(that_date)

    # Create DataFrame with date list
    final_df = pd.DataFrame(datelist, columns=["date"])

    # Efficiently store stock probabilities
    probabilities = []
    stock_names = []

    with open('CompanyNames.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            stock = re.sub(r'[^\w]', '_', row[0].strip().replace(".NS", ""))
            probabilities.append(stp(stock, datelist))
            stock_names.append(stock)

    # Combine probability data efficiently
    prob_df = pd.DataFrame([probabilities], columns=stock_names)
    final_df = pd.concat([final_df, prob_df], axis=1)

    # Save the final DataFrame
    output_file_path = os.path.join(save_path, f"{date}_{i}.csv")
    final_df.to_csv(output_file_path, index=False)

