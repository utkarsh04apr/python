if __name__ == "__main__":
    
    t = int(input())
    for i in range(t):
        
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        
        sum = 0
        for arrElem in arr:
            sum = sum + arrElem
            
        print(sum)
