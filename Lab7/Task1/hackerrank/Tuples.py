if __name__ == "__main__":
    n = int(input().strip())
    t = tuple(map(int, input().split()))
    print(hash(t))