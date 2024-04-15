list_1 = [
    {"name": "Kanat", "last_name": "Erbolov", "age": 20},
    {"name": "Askar", "last_name": "Paivich", "age": 15},
    {"name": "Kairat", "last_name": "Sadva", "age": 45}
]

total_age = 0
for person in list_1:
    total_age += person["age"]
    
count = len(list_1)


average_age = total_age / count

print("Average age:",average_age)