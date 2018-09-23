import random

def simulate_coin_toss(n):
    return [random.getrandbits(1) for i in range(n)]

if __name__ == '__main__':
    print("Simulating 100 coin tosses...")
    print(simulate_coin_toss(100))
