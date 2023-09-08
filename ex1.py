import sys
if __name__ == '__main__':
    # Enter a tuple in one line.
    A = tuple(map(int, input().split()))
    # Check the number of elements in a tuple.
    if len(A) != 10:
        print("Invalid tuple size", file=sys.stderr)
        exit(1)
    # Find the required amount.
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item

    print(s)