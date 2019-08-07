if __name__ == '__main__':
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        number = i
        gap = None
        previous = number % 10
        number = int(number / 10)
        answer = True
        while number > 0 and answer:
            current = number % 10
            if gap is None:
                gap = previous - current
            elif previous - current != gap:
                answer = False
            previous = current
            number = int(number / 10)

        if answer:
            count += 1
    print(count)
