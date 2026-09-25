# YOM Prime Theorem - Erkan Tekin 2026-09-24
import math
CORRECTION = 6/7
def pi_yom(x):
    return x / (math.log(x) - CORRECTION)
def p_yom(n):
    return 1 / (math.log(n) - CORRECTION)
