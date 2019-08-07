if __name__ == '__main__':
     A, B, C = map(int, input().split())
     income = C - B
     if income <= 0:
         print(-1)
     else:
        print(int(A / income) + 1)
