import csv
import json
import os
import uuid


if __name__ == '__main__':
    input_file = 'input.csv'
    vehicles = []
    with open(input_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = str(uuid.uuid4())
            row['hp'] = int(row['hp'])
            row['price'] = float(row['price'])
            vehicles.append(row)

    categories = {
        'slow_cars': lambda hp: hp < 120,
        'fast_cars': lambda hp: 120 <= hp < 180,
        'sport_cars': lambda hp: hp >= 180,
        'cheap_cars': lambda price: price < 20000,
        'medium_cars': lambda price: 20000 <= price < 50000,
        'expensive_cars': lambda price: price >= 50000,
    }

    output_dir = 'output_data'
    if os.path.exists(output_dir):
        for category in categories:
            category_file = os.path.join(output_dir, category + '.json')
            if os.path.exists(category_file):
                os.remove(category_file)
    else:
        os.mkdir(output_dir)

    for category, condition in categories.items():
        category_file = os.path.join(output_dir, category + '.json')
        if category in ['cheap_cars', 'medium_cars', 'expensive_cars']:
            category_data = [vehicle for vehicle in vehicles if condition(vehicle['price'])]
        else:
            category_data = [vehicle for vehicle in vehicles if condition(vehicle['hp'])]
        with open(category_file, 'w') as f:
            json.dump(category_data, f, indent=2)

    brands = set(vehicle['brand'] for vehicle in vehicles)
    for brand in brands:
        brand_file = os.path.join(output_dir, brand.lower() + '.json')
        brand_data = [vehicle for vehicle in vehicles if vehicle['brand'].lower() == brand.lower()]
        with open(brand_file, 'w') as f:
            json.dump(brand_data, f, indent=2)
