# -*- coding: utf-8 -*-
"""
Deck Drawing Simulator
"""

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pandas as pd
import string


### Draw function ###
def drawDeck(deck, record, drawNo, turn, qty=1):

    cardsDrawn = rd.choices(deck, k=qty)    
    for card in cardsDrawn:
        drawNo += 1
        latestRecord = pd.DataFrame({'Card Name': str(card)
                                ,'Draw No': drawNo
                                ,'Turn': turn}
                                   ,index=[0] )
        record = pd.concat([record,latestRecord],ignore_index=True)
        deck.remove(card) 
    turn += 1
    return record, drawNo, turn


### Reset ###
record = pd.DataFrame(columns=['Card Name', 'Draw No', 'Turn'])
turn = 0
drawNo = 0

    
### Deck Creation
deck = list(range(0,40))
ab =list(string.ascii_uppercase)

n = 0
for i in range(0,6):
    deck[n:n+i+1] = [ab[i]*3]*(i+1)
    n = n+i+1


###Initiate Draw Quest###


###Mulligan Phase###
drawStart = 3
record, drawNo, turn = drawDeck(deck, record, drawNo, turn, drawStart)

while len(deck) > 0 and turn <= 40:    
    record, drawNo, turn = drawDeck(deck, record, drawNo, turn)
    