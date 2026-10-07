import numpy as np

harvest_data = np.array([
    [50, 55, 60, 52, 58, 65, 70],
    [30, 32, 28, 35, 33, 40, 42],
    [100, 95, 105, 110, 98, 120, 105],
    [40, 38, 42, 45, 41, 50, 55]
])

crops = ["Tomatoes", "Carrots", "Potatoes", "Onions"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Shape:", harvest_data.shape)
print("Dimensions:", harvest_data.ndim)
print("Size:", harvest_data.size)

report = harvest_data.T
print("\nReport:")
for day, row in zip(days, report):
    print(day, row)

weekly_total = harvest_data.sum(axis=1)
print("\nWeekly total:")
for crop, total in zip(crops, weekly_total):
    print(crop, total, "kg")

day_average = harvest_data.mean(axis=0)
print("\nDaily average:")
for day, avg in zip(days, day_average):
    print(day, round(avg, 2), "kg")

best = harvest_data.argmax()
crop, day = np.unravel_index(best, harvest_data.shape)
print("\nBest yield:", harvest_data[crop, day], "kg")
print(crops[crop], "on", days[day])

daily_bonus = np.array([0, 0, 0, 0, 5, 10, 15])
with_bonus = harvest_data + daily_bonus

shrinkage = np.array([0.95, 0.98, 0.99, 0.97])
final_weight = with_bonus * shrinkage[:, np.newaxis]

print("\nFinal transported weight:")
print(final_weight.round(2))

print("\nFinal weekly total:")
for crop, total in zip(crops, final_weight.sum(axis=1)):
    print(crop, round(total, 2), "kg")