import sys
from math import *

def normal_distrib(mean, deviation, x):
    return (1 / (float(deviation) * sqrt(2 * pi))) * exp(-1 * (pow(x - float(mean), 2) / (2 * pow(float(deviation), 2))))

def calc_no_iq_args(args):
    for i in range(0, 201):
        print("%d %.5f" % (i, normal_distrib(args[0], args[1], i)))
    
def calc_1_iq_args(args):
    res = 0.0
    i = 0.0
    while (i < args[2]):
        res += normal_distrib(args[0], args[1], i)
        i += 0.01
    res *= 0.01
    print("%.1f%% of people have an IQ inferior to %d" % (res * 100, args[2]))

def calc_2_iq_args(args):
    if (args[2] > args[3]):
        sys.exit(84)
    res = 0.0
    i = float(args[2])
    while (i < args[3]):
        res += normal_distrib(args[0], args[1], i)
        i += 0.01
    res *= 0.01
    print("%.1f%% of people have an IQ between %d and %d" % (res * 100, args[2], args[3]))
