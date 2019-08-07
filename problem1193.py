if __name__ == '__main__':
    N = int(input())
    sum = 0
    num = 0
    while sum < N:
        num = num + 1
        sum = sum + num

    partSeq = N - (sum - num)
    targetSum = num + 1
    print("%d/%d" % ((partSeq, (targetSum - partSeq)) if partSeq % 2 != 0 else ((targetSum - partSeq), partSeq)))