def hotel_cost(nights): # Cost of hotel
  return 140 * nights # $140/night

def plane_ride_cost(city): # Cost of plane ride
  if city == "Charlotte":
    return 183 # $183 from Charlotte
  elif city == "Tampa":
    return 220 # $220 from Tampa
  elif city == "Pittsburgh":
    return 222 # $222 from Pittsburgh
  elif city == "Los Angeles":
    return 475 # $475 from Los Angeles

def rental_car_cost(days): # Cost of rental car
  cost = 40 * days
  if days >= 7:
    return cost - 50 # $50 off total cost after 7 or more days
  elif days >= 3:
    return cost - 20 # $20 off total cost after 3 or more days
  return cost

def trip_cost(city, days, spending_money): # Total cost of trip
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)
