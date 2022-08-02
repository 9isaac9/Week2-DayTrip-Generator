#DAY TRIP GENERATOR


reservation_list = ["destination", "restaurant", "transportation", "entertainment\n"]
print(reservation_list)


print()



destination = ["Paris", "Italy", "Germany", "Ireland"]
print(destination)
restaurant = ["Jaques Bistro", "Brunos Olive Garden", "Schnetzels Place", "Leprechauns Pot of Gold"]
print(restaurant)
transportation = ["vehicle rentals", "train", "plane", "cruise liner"]
print(transportation)
entertainment = ["dancing", "theater", "museum","excursion"]
print(entertainment)


print()

print("RANDOM SELECTIONS")

print()
#destitnation_list = ["Paris", "Italy", "Germany", "Ireland"]
import random
destination_list = ["Paris", "Italy", "Germany", "Ireland"]
print(random.choice(destination_list))

print()
#restaurant_list = ["Jaques Bistro", "Brunos Olive Garden", "Schnetzels Place", "Leprechauns GoldPot"]
import random
restaurant_list = ["Jaques Bistro", "Brunos Olive Garden", "Schnetzels Place", "Leprechauns GoldPot"]
print(random.choice(restaurant_list))

print()
#transportation_list = ["vehicle rentals", "train", "plane", "cruise liner"]
import random
transportation_list = ["vehicle rentals", "train", "plane", "cruise liner"]
print(random.choice(transportation_list))

print()
#entertainment = ["dancing", "theater", "museum","excursion"]
import random
entertainment_list = ["dancing", "theater", "museum","excursion"]
print(random.choice(entertainment_list))