#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

input_file = 'ws353.tsv'
output_file = "word_pairs.tsv"

def get_word_pairs():
    with open(input_file, "r") as source, open(output_file, "w") as sink:
        reader = csv.reader(source, delimiter="\t")
        writer = csv.writer(sink, delimiter = "\t")
        for row in reader:
            writer.writerow(row[:2])

get_word_pairs()
            