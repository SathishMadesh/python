def count_holidays(N, festival_days):
    holidays = 0
    for day in festival_days:
        if day % 7 == 1 or day % 7 == 0:
            holidays += 1
    return holidays

def main():
    T = int(input("Enter the number of test cases: "))
    
    for a in range(T):
        N = int(input("Enter the number of festival days: "))
        festival_days = list(map(int, input("Enter festival days separated by space: ").split()))
        
        total_holidays = count_holidays(N, festival_days)
        print("Total number of holidays:", total_holidays)

if __name__ == "__main__":
    main()