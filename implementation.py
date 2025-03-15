import pandas as pd

# functions:-
# sentence similarity check using bert sim (fnc.3)
def sent_sim(sent1,sent2,score=75):
    from sentence_transformers import SentenceTransformer,util
    model1 = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model1.encode([sent1,sent2],convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0],embeddings[1])
    similarity_score = similarity.item()
    score = score/100
    if similarity_score>=score:
        return 1
    return 0

# for importing csv from today_headlines_csvs
def import_csv(filename):
    import os
    import pandas as pd
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "today_headlines_csvs", f"{filename}_ls.csv")
    df = pd.read_csv(path)
    return df


# implementation:-

# aim1:- make datelist , containing dates when headline score is greater than given score for a current headline
# expecting :- today_headlines.csv

today_headlines = import_csv("20200313")

# print(today_headlines.head())
# print(today_headlines.columns)
datelist = []
for i in range(len(today_headlines)):
    str1 = today_headlines.loc[i,"headline_text"]
    str2 = "to be imported" #to be imported #make function to fetch csv files from data folder
    filename = "12341212" #file name of the csv file of data folder - just want the date part of the filename
    filename_ = int(filename)
    sim_bin = sent_sim(str1,str2) #if similar then binary 1 else binary 0
    if sim_bin==1 and filename_ not in datelist:
        datelist.append(filename_)

# to be continued.....





