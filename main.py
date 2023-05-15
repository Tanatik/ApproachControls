# This is a sample Python tests for test task from Approach Controls.
import arrayUtils


if __name__ == '__main__':
    # functions accept any array
    arrayUtils.find_unique_pairs_optimized()
    for pair in arrayUtils.find_unique_pairs():
        print(pair)
