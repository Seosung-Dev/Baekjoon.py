def main():
    H, M = map(int, input().split())
    if M < 45:
        H -= 1
        M += 60
    if H < 0:
        H = 23
    M -= 45
    print(H, M)
if __name__ == "__main__":
    main()