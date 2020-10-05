#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk

tokens = []

with open("news.2016.en.shuffled.deduped", "r") as source:
    for line in source:
        line = line.casefold()
        tokens.append(nltk.word_tokenize(line))

joined_tokens = " ".join(tokens)

print(len(joined_tokens))
        
with open('tokenized_news_data.txt', 'w') as f:
    for item in joined_tokens:
        f.write("%s\n" % item)
        
        

    
