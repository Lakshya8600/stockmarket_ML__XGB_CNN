# FUNCTION-3:-
# INPUT:- headline1,headline2 and score(which is by default set to 75; this score is similarity score)
# OUTPUT:- binary 1 or 0: 1 for  similarity score greater than 75%

# function-3:- tells if the sentences are similar or not, function inputs 2 strings and one optional score which is 75% by default. function returns binary that it matches or not


# import spacy
# from sentence_transformers import SentenceTransformer,util

# TO BE USED:-
# implementing bert

# model1 = SentenceTransformer('all-MiniLM-L6-v2')

def bert_similarity(sent1,sent2,score=75):
    from sentence_transformers import SentenceTransformer,util
    import torch

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model1 = SentenceTransformer('all-MiniLM-L6-v2', device=device) #load model on gpu if available
    embeddings = model1.encode([sent1,sent2],convert_to_tensor=True).to(device) #move to gpu
    similarity = util.pytorch_cos_sim(embeddings[0],embeddings[1])

    similarity_score = similarity.item()
    score = score/100
    
    # print(torch.cuda.is_available())
    # print(torch.version.cuda)
    # print(torch.cuda.device_name(0))

    if similarity_score>=score:
        return 1
    return 0







#OUTPUT TRIAL:-
s1 = "mahindra starts developing semiconductors"
s2 = "mahindra stops developing semiconductors"
output = bert_similarity(s1,s2)
print(output)
s1 = "mahindra starts developing semiconductors"
s2 = "mahindra stops developing semiconductors"
output = bert_similarity(s1,s2)
print(output)



# #NOT TO BE USED, SPACY;
# nlp = spacy.load("en_core_web_lg")

# # 2 string, score; -> if score>0.75 give 1 else 0

# def string_sim(str1,str2,score=0.75):
#     doc1 = nlp(str1)
#     doc2 = nlp(str2)

#     return doc1.similarity(doc2)
# print(output)