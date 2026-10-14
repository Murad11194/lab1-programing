# Task 1: Imperative Style (Loops and conditions)
parcels = [
    {"id": 1, "weight": 3.5},
    {"id": 2, "weight": 8.0},
    {"id": 3, "weight": 12.5},
    {"id": 4, "weight": -2.0},  # Xətalı çəki (invalid weight)
    {"id": 5, "weight": 5.0},
    {"id": 6, "weight": 10.0},
    {"id": 7, "weight": 14.2},
]

total_shipping_cost = 0
print("--- Task 1: Imperative Solution ---")

for parcel in parcels:
  weight = parcel["weight"]
  if weight <= 0:
    print(
        f"Bağlama ID {parcel['id']}: Xətalı çəki ({weight} kg) qəbul edilmədi."
    )
    continue

  if weight <= 5:
    cost = 5
  elif weight <= 10:
    cost = 10
  else:
    cost = 15

  total_shipping_cost += cost
  print(f"Bağlama ID {parcel['id']}, Çəki: {weight} kg -> Qiymət: {cost} AZN")

print(f"Ümumi daşınma xərci: {total_shipping_cost} AZN\n")