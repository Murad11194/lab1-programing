# Task 3: Higher-order function & callback
parcels = [
    {"id": 1, "weight": 3.5},
    {"id": 2, "weight": 8.0},
    {"id": 3, "weight": 12.5},
    {"id": 4, "weight": -2.0},
    {"id": 5, "weight": 5.0},
    {"id": 6, "weight": 10.0},
    {"id": 7, "weight": 14.2},
]


def partition(items, predicate):
  true_list = []
  false_list = []
  for item in items:
    if predicate(item):
      true_list.append(item)
    else:
      false_list.append(item)
  return true_list, false_list


# Adlı funksiya (is_valid)
def is_valid(parcel):
  return parcel["weight"] > 0


print("--- Task 3: Higher-Order Function Solution ---")

# 1. Adlı funksiya ilə çağırış (Etibarlı və xətalı bağlamalar)
valid_ones, invalid_ones = partition(parcels, is_valid)
print(f"Etibarlı bağlamaların sayı: {len(valid_ones)}")
print(f"Xətalı bağlamalar: {[p['id'] for p in invalid_ones]}")

# 2. Lambda ilə çağırış (Yüngül və ağır bağlamalar: <=10 kg və >10 kg)
light_ones, heavy_ones = partition(valid_ones, lambda p: p["weight"] <= 10)
print(f"Yüngül bağlamalar (<=10 kg) ID-ləri: {[p['id'] for p in light_ones]}")
print(f"Ağır bağlamalar (>10 kg) ID-ləri: {[p['id'] for p in heavy_ones]}")