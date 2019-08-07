class CallCounter:
    callCounts = [(1, 0), (0, 1)]

    def getCallCount(self, number):
        if len(self.callCounts) > number:
            return self.callCounts[number]

        callCount1 = self.getCallCount(number - 1)
        callCount2 = self.getCallCount(number - 2)

        callCount = (callCount1[0] + callCount2[0], callCount1[1] + callCount2[1])
        self.callCounts.append(callCount)

        return callCount

if __name__ == '__main__':
    n = int(input())
    callCounter = CallCounter()
    for i in range(n):
        inputNumer = int(input())
        count0, count1 = callCounter.getCallCount(inputNumer)
        print(count0, count1)
