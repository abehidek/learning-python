print('This program calculates how much you should pay for renting a car')
km_covered = float(input('How many km did you travel while renting the car: '))
days_covered = int(input('How many days did you rent the car?: '))
price = (km_covered * 0.15) + (days_covered * 60)
print('For {} days and {}km traveled, you should pay: ${}'.format(km_covered, days_covered, price))
