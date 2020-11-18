# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:05:15 2020
"""

import random

rows = [200.0,400.0,600.0,800.0,1000.0]
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


def test(mode, runs):
    avg = 0.0
    for i in range(1,runs):
        new_result = game(mode)
        avg = avg*(i-1)/i + new_result/i
    return avg

def run_tests(runs):
    
    #linear order test
    lin_avg = test("linear", runs)
    #random order test    
    rand_avg = test("random", runs)

    
    print("results of linear guessing strategy: " + str(lin_avg))
    print("results of random guessing strategy: " + str(rand_avg))
    
run_tests(1000000)
