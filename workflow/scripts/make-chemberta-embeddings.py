from collections import defaultdict
import sys
import numpy as np
from damply import dirs
import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForMaskedLM
import tqdm 

pipe = pipeline("feature-extraction", model="seyonec/ChemBERTa-zinc-base-v1")

tokenizer = AutoTokenizer.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")
model = AutoModelForMaskedLM.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")

MOA_ONLY = True

mol_data = pd.read_csv(dirs.RAWDATA / "colData.csv")

# rop molecules w/o smiles or CIDs
mol_data = mol_data.dropna(subset=['SMILES','Pubchem.CID'])

if MOA_ONLY:
    mol_data = mol_data.dropna(subset=['Mechanism.of.Action'])


mol_df = defaultdict(list)

for idx, row in (pbar:= tqdm.tqdm(mol_data.iterrows(),total = mol_data.shape[0])):
    # pbar.set_description(f"Working on molecule {idx}")
    
    mol = row['SMILES']
    res = pipe(mol,return_tensors=True)
    
    res = res.numpy().squeeze()
    
    avg_emb = np.mean(res,axis=0)

    mol_df['HDD.Compound.ID'].append(row['HDD.Compound.ID'])
    mol_df['Molecule.Name'].append(row['Molecule.Name'])
    mol_df['Pubchem.CID'].append(int(row['Pubchem.CID']))
    mol_df['ChemBERTa.Embedding'].append(avg_emb)


mol_df = pd.DataFrame(mol_df)

if MOA_ONLY:
    mol_df.to_csv(dirs.RESULTS/"ChemBERTa_embeddings_MOA-ONLY.csv")
else:
    mol_df.to_csv(dirs.RESULTS/"ChemBERTa_embeddings.csv")




