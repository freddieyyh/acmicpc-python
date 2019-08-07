def contains(list, val, start, end):
    size = end - start

    if size <= 0:
        return False
    if size == 1:
        return list[start] == val

    half = start + int(size / 2)
    return contains(list, val, start, half) if val < list[half] else contains(list, val, half, end)

if __name__ == '__main__':
    target_size = int(input())
    target = list(map(int, input().split()))

    q_size = int(input())
    q = [int(a) for a in input().split()]

    target.sort()

    for val in q:
        print(1 if contains(target, val, 0, len(target)) else 0)