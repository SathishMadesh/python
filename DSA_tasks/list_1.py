# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,


list = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
extra = list[1]-list[0]
print("In Feb, dollars you spent extra compare to January :", extra)


# 2. Find out your total expense in first quarter (first three months) of the year.
three_month_exp = list[0]+list[1]+list[2]
print("Total expense in first quarter (first three months) of the year : ", three_month_exp)


# 3. Find out if you spent exactly 2000 dollars in any month
spent_2000 = False
for i in list:
    if i == 2000:
        spent_2000 = True
        print("Yes, you spent exactly 2000 dollars in one month")
        break
if not spent_2000:
    print("No, You didn't spent 2000 dollars in a month")


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
june = 1980
list.append(june)
print(list)


# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
index_of_april = 3
refund = 200
list[index_of_april] = list[index_of_april]-200
print("Your monthly expense list :", list) 