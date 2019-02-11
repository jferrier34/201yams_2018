#!/usr/bin/python3
import sys
from math import *

def pair(nb):
    tmp = 0
    proba = 0
    if (sys.argv[1] == nb):
        tmp += 1
    if (sys.argv[2] == nb):
        tmp += 1
    if (sys.argv[3] == nb):
        tmp += 1
    if (sys.argv[4] == nb):
        tmp += 1
    if (sys.argv[5] == nb):
        tmp += 1
    if (tmp >= 2):
        proba = 1
    else:
        for x in range(2 - tmp, 5 - tmp + 1):
            proba += (factorial(5 - tmp) / (factorial(x) * factorial((5 - tmp) - x))) * pow(1 / 6, x) * pow(5 / 6, (5 - tmp) - x)
    print("chances to ge t a" + nb + " pair" + ": %0.2f%%" % (proba * 100))
    exit(0)

def three(nb):
    tmp = 0
    proba = 0
    if (sys.argv[1] == nb):
        tmp += 1
    if (sys.argv[2] == nb):
        tmp += 1
    if (sys.argv[3] == nb):
        tmp += 1
    if (sys.argv[4] == nb):
        tmp += 1
    if (sys.argv[5] == nb):
        tmp += 1
    if (tmp >= 3):
        proba = 1
    else:
        for x in range(3 - tmp, 5 - tmp + 1):
            proba += (factorial(5 - tmp) / (factorial(x) * factorial((5 - tmp) - x))) * pow(1 / 6, x) * pow(5 / 6, (5 - tmp) - x)
    print("chances to ge t a" + nb + " three" + ": %0.2f%%" % (proba * 100))
    exit(0)

def four(nb):
    tmp = 0
    proba = 0
    if (sys.argv[1] == nb):
        tmp += 1
    if (sys.argv[2] == nb):
        tmp += 1
    if (sys.argv[3] == nb):
        tmp += 1
    if (sys.argv[4] == nb):
        tmp += 1
    if (sys.argv[5] == nb):
        tmp += 1
    if (tmp >= 4):
        proba = 1
    else:
        for x in range(4 - tmp, 5 - tmp + 1):
            proba += (factorial(5 - tmp) / (factorial(x) * factorial((5 - tmp) - x))) * pow(1 / 6, x) * pow(5 / 6, (5 - tmp) - x)
            print(proba)
    print("chances to ge t a" + nb + " four" + ": %0.2f%%" % (proba * 100))
    exit(0)

def yams(nb):
    tmp = 0
    proba = 0
    if (sys.argv[1] == nb):
        tmp += 1
    if (sys.argv[2] == nb):
        tmp += 1
    if (sys.argv[3] == nb):
        tmp += 1
    if (sys.argv[4] == nb):
        tmp += 1
    if (sys.argv[5] == nb):
        tmp += 1
    if (tmp >= 5):
        proba = 1
    else:
        for x in range(5 - tmp, 5 - tmp + 1):
            proba += (factorial(5 - tmp) / (factorial(x) * factorial((5 - tmp) - x))) * pow(1 / 6, x) * pow(5 / 6, (5 - tmp) - x)
    print("chances to ge t a" + nb + " yams" + ": %0.2f%%" % (proba * 100))
    exit(0)

def check(nb):
    ret = 0
    if (int(sys.argv[1]) == nb):
        ret += 1
    if (int(sys.argv[2]) == nb):
        ret += 1
    if (int(sys.argv[3]) == nb):
        ret += 1
    if (int(sys.argv[4]) == nb):
        ret += 1
    if (int(sys.argv[5]) == nb):
        ret += 1
    if (ret > 1):
        ret = 1
    return (ret)

def straight(nb):
    tmp = 0
    if (nb == '6'):
        test = check(2) + check(3) + check(4) + check(5) + check(6)
    else:
        test = check(1) + check(2) + check(3) + check(4) + check(5)
    if (test == 5):
        tmp = 1
    else:
        tmp = factorial(5 - test) / 6**(5 - test)
    print("chacnes to get a" + nb + " straight" + ": %0.2f%%" % (tmp * 100))
    exit(0)

def full(nb, nb2):
    tmp = 0
    check1 = 0
    check2 = 0
    if (int(sys.argv[1]) == nb):
        check1 += 1
    if (int(sys.argv[2]) == nb):
        check1 += 1
    if (int(sys.argv[3]) == nb):
        check1 += 1
    if (int(sys.argv[4]) == nb):
        check1 += 1
    if (int(sys.argv[5]) == nb):
        check1 += 1

    if (int(sys.argv[1]) == nb2):
        check2 += 1
    if (int(sys.argv[2]) == nb2):
        check2 += 1
    if (int(sys.argv[3]) == nb2):
        check2 += 1
    if (int(sys.argv[4]) == nb2):
        check2 += 1
    if (int(sys.argv[5]) == nb2):
        check2 += 1

    if (check1 == 3 and check2 == 2):
        tmp = 1
    else:
        if (check1 > 3):
            check1 = 3
        if (check2 > 2):
            check2 = 2
        pair = factorial(5 - check1 - check2) / (factorial(3 - check2) * factorial((5 - check2 - check1) - (3 - check1)))
        brelan = factorial(2 - check2) / (factorial(2 - check2) * factorial((2 - check2) - (2 - check2)))
        res = (pair * brelan) / 6**(5 - check1 - check2)
    print("chances to get a " + nb + " full of " + nb2 + ": %0.2f%%" % (res * 100))
    exit(0)

def check_split(list):
    try:
        try1 = int(list[1])
    except:
        exit(84)
    if (try1 > 6 or try1 < 1):
        exit(84)

def do_all():
    combination = sys.argv[6]
    list = []
    list = combination.split('_')
    check_split(list)
    if (list[0] == "pair"):
        pair(list[1])
    if (list[0] == "three"):
        three(list[1])
    if (list[0] == "four"):
        four(list[1])
    if (list[0] == "yams"):
        yams(list[1])
    if (list[0] == "straight"):
        straight(list[1])
    if (list[0] == "full"):
        full(list[1], list[2])

def check_error():
    if (len(sys.argv) == 2 and sys.argv[1 == "-h"]):
        help()
    if (len(sys.argv) != 7):
        exit(84)
    try:
        int(sys.argv[1])
        int(sys.argv[2])
        int(sys.argv[3])
        int(sys.argv[4])
        int(sys.argv[5])
    except:
            exit(84)

def main():
    check_error()
    do_all()

main()