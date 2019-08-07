def sigma(number):
    return number * (number + 1) / 2

if __name__ == '__main__':
    n = int(input())
    i = 1
    while sigma(i) <= n:
        i = i + 1

    print(i - 1)