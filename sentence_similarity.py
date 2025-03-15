import spacy

nlp = spacy.load("en_core_web_lg")

# 2 string, score; -> if score>0.75 give 1 else 0

def string_sim(str1,str2,score=0.75):
    