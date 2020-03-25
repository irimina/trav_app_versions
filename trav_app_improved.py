# travel app with functions

# using functions ( basic) and if-else statements
# taking a vacation using making decisions with if-elif. 
#Make you own scenario and create a program that display the cost of travel.
import time


def hotel_cost(nights):
    return (140 * nights)


def plane_ride_cost(city):
    if city == 'Charlotte':
        return (183)
    elif city == 'Tampa':
        return (220)
    elif city == 'Pittsburgh':
        return (222)
    elif city == "Los Angeles":
        return (475)


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3 and days < 7:
        cost -= 20
    return cost


def trip_cost(city, days, nights,spending_money):
    return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(nights) + spending_money
###################################


print("Welcome to the travel app caculator")
time.sleep(1)

city=str(input("Where would you like to fly: "))
print("Cost: $",plane_ride_cost(city))

nights=int(input("How many nights at the hotel : "))
print("Cost: $",hotel_cost(nights))

days= int(input("How many days do you need a rental car: "))
print("Rental Car Cost: $: ",rental_car_cost(days))

spending_money=float(input("Spending money amount: "))
print("Spending budget: $",spending_money)

print("The total cost of your trip is $",trip_cost(city, days,nights, spending_money))
time.sleep(1)
print("Thank you for your this app")
