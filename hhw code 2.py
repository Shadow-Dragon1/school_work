#To find sale price of an item with given cost and discount (%)
cost=int(input("cost of item: "))
discount=int(input("discount percentage: "))
saved=(discount/100)*cost
final=cost-saved
print("you saved ",saved)
print("your final prize is ",final)