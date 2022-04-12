import random

FIRST = 500
SECOND = 200
THIRD = 100
FORTH = 50
FIFTH = 20
SIXTH = 10

pool = [FIRST,SECOND,THIRD,FORTH,FIFTH,SIXTH]
pool_cum_weight = [1,4,10,25,60,110]


def lottery():
    return random.choices(pool,cum_weights=pool_cum_weight)[0]

if __name__ == "__main__":
    print(lottery())