# YOM Prime Theorem - 6/7 Correction
# Tarih: 2026-09-24 Erzurum/Mus - Yazar: Erkan Tekin & YOM Theory
# GPL v3

import math
CORRECTION = 6/7  # (7-1)/7

def P_YOM(n):
    return 1 / (math.log(n) - CORRECTION)

def pi_YOM(x):
    return x / (math.log(x) - CORRECTION)

def pi_classic(x):
    return x / math.log(x)
