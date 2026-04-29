import pandas as pd
from gensim.models.word2vec import Word2Vec
from damply import dirs
from itertools import combinations

sentences = pd.read_csv(dirs.RAWDATA / "colData.csv")
sentences = sentences.dropna(subset=['Mechanism.of.Action'])


smiles_corpus = []

for moa in pd.unique(sentences['Mechanism.of.Action']):
    sent = list(sentences[sentences['Mechanism.of.Action']==moa]['SMILES'])
    smiles_corpus.append(sent)

smiles_corpus = []
for mol in pd.unique(sentences['SMILES']):
    smiles_corpus.append([mol])

# sentences = [[a,b] for a,b in combinations(list(sentences['SMILES']),2)]

model = Word2Vec(smiles_corpus,vector_size=5,min_count=1)

for mol in sentences['SMILES']:
    print(f"{mol} has embedding {model.wv[mol]}")
    print("\n")
# model.train()
# print(model.wv.keys())
# print(vector)
