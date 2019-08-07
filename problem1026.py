if __name__ == '__main__':
    size = int(input())
    A = list(map(int, input().split()))
    B = [int(x) for x in input().split()]

    A.sort()
    B.sort(reverse=True)

    print(sum([A[i] * B[i] for i in range(size)]))