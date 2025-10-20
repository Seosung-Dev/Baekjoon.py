def main():
    N = int(input())
    dic = {}
    extent = 0
    max_left = 0
    for i in range(N):
        A, B = map(int, input().split())
        dic[A] = B
    for j in range(min(dic.keys()), max(dic.keys()) + 1):
        if j in dic and dic[j] > max_left:
            max_left = dic[j]
            extent += dic[j]
        elif j in dic and dic[j] <= max_left:
            extent += max_left
            count += 1
        elif j not in list(dic.keys()):
            extent += max_left
            count += 1
    print(extent)
    return 0
if __name__ == "__main__":
    main()