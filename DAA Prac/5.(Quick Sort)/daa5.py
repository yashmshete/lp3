import random
import time

def deter(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return deter(left) + [pivot] + deter(right)

def ran(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
    left = [x for x in arr[1:] if x < arr[0]]
    right = [x for x in arr[1:] if x >= arr[0]]
    return ran(left) + [arr[0]] + ran(right)

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

    st = time.time()
    d = deter(arr.copy())
    et = time.time()
    print("Deterministic sort result:", d)
    print(f"Deterministic sort time: {et - st:.6f} seconds")

    st = time.time()
    r = ran(arr.copy())
    et = time.time()
    print("Randomized sort result:", r)
    print(f"Randomized sort time: {et - st:.6f} seconds")
