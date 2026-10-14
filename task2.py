# Task 2: Functional Style (No loops, map, filter, reduce)
from functools import reduce

parcels = [
    {"id": 1, "weight": 3.5},
    {"id": 2, "weight": 8.0},
    {"id": 3, "weight": 12.5},
    {"id": 4, "weight": -2.0},
    {"id": 5, "weight": 5.0},
    {"id": 6, "weight": 10.0},
    {"id": 7, "weight": 14.2},
]


def shipping_cost(weight):
  if weight <= 5:
    return 5
  elif weight <= 10:
    return 10
  else:
    return 15


# 1. Etibarlı bağlamaları seçmək üçün filter()
valid_parcels = list(filter(lambda p: p["weight"] > 0, parcels))

# 2. Xərcləri hesablamaq üçün map()
costs = list(map(lambda p: shipping_cost(p["weight"]), valid_parcels))

# 3. Ümumi məbləği tapmaq üçün reduce()
total_cost = reduce(lambda x, y: x + y, costs, 0)

# 4. 10 kq-dan ağır bağlamaları seçmək üçün lambda ilə filter()
heavy_parcels = list(filter(lambda p: p["weight"] > 10, valid_parcels))

print("--- Task 2: Functional Solution ---")
print(f"Ümumi daşınma xərci: {total_cost} AZN")
print(
    "10 kq-dan ağır bağlamalar ID-ləri:"
    f" {[p['id'] for p in heavy_parcels]}"
)
print()