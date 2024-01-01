def carlsen_prize(x, results):
    carlsen_points = results.count('C') * 2 + results.count('D')  # Calculate Carlsen's total points
    chef_points = results.count('N') * 2 + results.count('D')  # Calculate Chef's total points

    if carlsen_points > chef_points:
        return 60 * x  # Carlsen wins, gets 60*X
    elif carlsen_points < chef_points:
        return 40 * x  # Chef wins, gets 40*X
    else:
        return 55 * x  # Tie, Carlsen declared winner, gets 55*X

# Main function to process input and output
# def main():
t = int(input("Enter the number of test cases (T): "))
for a in range(t):
    x = int(input())  # Total prize pool 100*X
    results = input().strip()  # Results of the 14 games
    carlsen_money = carlsen_prize(x, results)
    print(carlsen_money)

# Run the main function
# if __name__ == "__main__":
#     main()