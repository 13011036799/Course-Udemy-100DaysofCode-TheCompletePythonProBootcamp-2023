#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
total_money = input("How much do you need to pay? ")
people = input("How many people there are? ")
tip_percent = input("What percent of total fee do you want to pay as tips? (15/20/25) ")

tip = int(tip_percent) * float(total_money) / 100
total_money = float(total_money) + tip
personal_fee = float(total_money) / int(people)
# personal_fee = round(personal_fee,2)
# personal_fee ='{:.2f}'.format(personal_fee)
personal_fee = '%.2f' % personal_fee 
# 这里结果是string，但是如果用在计算里的话需要变成float

print(f"Each person should pay {personal_fee}$.")
