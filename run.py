"""
run this module
data: download data 
eda: ...
train: ...
test: ...
"""

# load packages
import os 
import sys 
import numpy as np
from numpy.lib.npyio import load
import pandas as pd

# load files 
# data 
from src.data.data_downloader import download_drug_reviews
from src.data.data_loader import load_data, partition_data
# eda 
from src.eda.visualize import (
    plot_basic_stats, 
    plot_condition_distribution,
    plot_useful_counts_distribution,
    plot_useful_counts_groupby_condition,
    plot_useful_counts_groupby_rating,
    plot_word_cloud,

)
# preprocessing 
from src.preprocess.construct_features import (
    tokenize_reviews
)
# models 

# ==================
# ----- main -------
# ==================

def main(targets):
    """
    TODO: explain targets variable
    """
    # download data 
    if 'download' in targets:
        print('Downloading Data ...')
        download_drug_reviews()
        print('Download Complete')
    
    if 'partition' in targets:
        print('Partitioning Data')
        partition_data()
        print('Partition Complete')
    
    if 'eda' in targets:
        print("EDA ...")
        # plots on original dataset 
        # train_df = load_data(train=True, dev=False)  
        # test_df = load_data(train=False, dev=False)
        # full_df = pd.concat([train_df, test_df])
        # plot_basic_stats(full_df)
        # plot_useful_counts_distribution(full_df)
        # plot_condition_distribution(full_df)
        # plot_useful_counts_groupby_condition(full_df)
        # plot_useful_counts_groupby_rating(full_df)

        # plots on preprocessed data
        plot_word_cloud()
        print('EDA Complete')

    if 'preprocess' in targets:
        print('Preprocessing ...')
        train_df = load_data(train=True, dev=False)
        test_df = load_data(train=False, dev=False)
        # tokenize_reviews(train_df)
        # tokenize_reviews(test_df, train=False)
        
        print('Preprocessing Complete')

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
