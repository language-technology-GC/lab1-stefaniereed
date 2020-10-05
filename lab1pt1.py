#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import csv
import scipy.stats
import numpy as np
import nltk
from nltk.corpus import wordnet
from nltk.corpus import wordnet_ic

df = pd.read_csv("ws353.tsv",sep='\t')
df.columns = ["word1","word2", "humans"]
df.head()

def get_lemma(word):
    syns = wordnet.synsets(word)
    synset = syns[0].name()
    return synset

def get_synset(word):
    lemma = get_lemma(word)
    synset = wordnet.synset(lemma)
    return synset

def path_sim(token1,token2):
    synset1 = get_synset(token1)
    synset2 = get_synset(token2)
    return round(synset1.path_similarity(synset2), 4)

def leacho_sim(token1,token2):
    synset1 = get_synset(token1)
    synset2 = get_synset(token2)
    return round(synset1.lch_similarity(synset2), 4)

def wupalm_sim(token1,token2):
    synset1 = get_synset(token1)
    synset2 = get_synset(token2)
    return round(synset1.wup_similarity(synset2), 4)

#the remaining similarity measures require information content(IC)

brown_ic = wordnet_ic.ic("ic-brown.dat")
semcor_ic = wordnet_ic.ic("ic-semcor.dat")
    
def res_sim(token1,token2,ic):
    synset1 = get_synset(token1)
    synset2 = get_synset(token2)
    return round(synset1.res_similarity(synset2, ic), 4)

def jiangcon_sim(token1,token2,ic):
    synset1 = get_synset(token1)
    synset2 = get_synset(token2)
    return round(synset1.jcn_similarity(synset2, ic), 4)

def lin_sim(token1,token2,ic):
    synset1 = get_synset(token1)
    synset2 = get_synset(token2)
    return round(synset1.lin_similarity(synset2,ic),4)


path_sim_scores = []
leacho_scores = []
wupalm_scores = []
res_scores = []
jiangcon_scores = []
lin_scores = []

for word in range(df.shape[0]): 
    w1 = df["word1"].iloc[word]
    w2 = df["word2"].iloc[word]
    
    path_sim_score = path_sim(w1, w2)
    path_sim_scores.append(path_sim_score)
    
    leacho_sim_score = leacho_sim(w1,w2)
    leacho_scores.append(leacho_sim_score)
    
    wupalm_sim_score = wupalm_sim(w1,w2)
    wupalm_scores.append(wupalm_sim_score)

    res_sim_score = res_sim(w1,w2,brown_ic)
    res_scores.append(res_sim_score)
    
    jiangcon_sim_score = jiangcon_sim(w1,w2,brown_ic)
    jiangcon_scores.append(jiangcon_sim_score)
    
    lin_sim_score = lin_sim(w1,w2,brown_ic)
    lin_scores.append(lin_sim_score)
    

df["path similarity"] = path_sim_scores
df["leacho"] = leacho_scores
df["wupalm"] = wupalm_scores
df["resnik"] = res_scores
df["jiangcon"] = jiangcon_scores
df["lin"] = lin_scores



human_scores = []
  
for score in range(df.shape[0]):
    human_score = df["humans"].iloc[word]
    human_scores.append(human_score)


generated_scores = df.columns[3:]

for score in generated_scores:
    spearman = scipy.stats.spearmanr(df["humans"], df[score])
    print(f"""Spearman's rho for human judgements and {score} similarity is {round(spearman[0],3)} 
    with p-value of {spearman[1]} \n""")
    

for score in generated_scores:
    coverage = np.sum(df[score].count())
    print(coverage)
    
    