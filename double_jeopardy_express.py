# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:05:15 2020

@author: bobth
"""

import random

rows = [200,400,600,800,1000]
column_count = 6
def game(guess_method):
    
    dj_location = random.randint(0,29)
    
    winnings_list = []
    
    if guess_method == "linear":
        winnings_list = rows*column_count
        winnings_list.sort()
    elif guess_method == "random":
        winnings_list = rows*column_count
        random.shuffle(winnings_list)
    else:
        print("error: use guess method = 'linear' or 'random' ")
        return None
    
    #sum contents of list before the element where double jeopardy is guessed
    
    winnings_list[dj_location] = sum(winnings_list[0:dj_location])
    
    return sum(winnings_list)


def run_test(runs):
    
    #linear test
    lin_results = []
    for i in range(0,runs):
        new_result = game("linear")
        lin_results.append(new_result)
    
    rand_results = []
    for i in range(0,runs):
        new_result = game("random")
        rand_results.append(new_result)
    
    lin_avg = sum(lin_results)/len(lin_results)
    rand_avg = sum(rand_results)/len(rand_results)
    
    print("results of linear guessing strategy: " + str(lin_avg))
    print("results of random guessing strategy: " + str(rand_avg))
    
run_test(1000000)