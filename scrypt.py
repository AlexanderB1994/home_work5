import csv
import json
import os

if __name__ == '__main__':
    pass

categories = {
    'slow_cars': lambda hp: hp < 120,
    'fast_cars': lambda hp: 120 <= hp < 180,
    'sport_cars': lambda hp: hp >= 180,
    'cheap_cars': lambda price: price < 20000,
    'medium_cars': lambda price: 20000 <= price < 50000,
    'expensive_cars': lambda price: price >= 50000,
}

input_file = 'input.csv'
machines = []
with open(input_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['id'] = hash(str(row))
        row['hp'] = int(row['hp'])
        row['price'] = int(row['price'])
        machines.append(row)

output_dir = 'output_data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for category, condition in categories.items():
    category_file = os.path.join(output_dir, category + '.json')
    if category == 'cheap_cars':
        category_data = [machine for machine in machines if condition(machine['price'])]
    elif category == 'medium_cars':
        category_data = [machine for machine in machines if condition(machine['price'])]
    elif category == 'expensive_cars':
        category_data = [machine for machine in machines if condition(machine['price'])]
    else:
        category_data = [machine for machine in machines if condition(machine['hp'])]
    with open(category_file, 'w') as f:
        json.dump(category_data, f, indent=2)

brands = set(machine['brand'] for machine in machines)
for brand in brands:
    brand_file = os.path.join(output_dir, brand.lower() + '.json')
    brand_data = [machine for machine in machines if machine['brand'].lower() == brand.lower()]
    with open(brand_file, 'w') as f:
        json.dump(brand_data, f, indent=2)
