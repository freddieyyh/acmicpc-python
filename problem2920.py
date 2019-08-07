if __name__ == '__main__':
    ascending = True
    descending = True
    for idx, val in enumerate(map(int, input().split())):
        if val != idx + 1:
            ascending = False
        if val != 8 - idx:
            descending = False
    print("ascending" if ascending else "descending" if descending else "mixed")