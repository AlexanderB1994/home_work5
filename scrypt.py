import csv
import json
import os
import uuid


def is_slow_car(hp):
    return hp < 120


def is_fast_car(hp):
    return 120 <= hp < 180


def is_sport_car(hp):
    return hp >= 180


def is_cheap_car(price):
    return price < 20000


def is_medium_car(price):
    return 20000 <= price < 50000


def is_expensive_car(price):
    return price >= 50000


def write_json_file(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


categories = {
    'slow_cars': is_slow_car,
    'fast_cars': is_fast_car,
    'sport_cars': is_sport_car,
    'cheap_cars': is_cheap_car,
    'medium_cars': is_medium_car,
    'expensive_cars': is_expensive_car,
}

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

    output_dir = 'output_data'
    if os.path.exists(output_dir):
        for category in categories:
            category_file = os.path.join(output_dir, category + '.json')
            if os.path.exists(category_file):
                os.remove(category_file)
    else:
        os.makedirs(output_dir)

    for category, condition in categories.items():
        category_file = os.path.join(output_dir, category + '.json')
        if category in ['cheap_cars', 'medium_cars', 'expensive_cars']:
            category_data = [vehicle for vehicle in vehicles if condition(vehicle['price'])]
        else:
            category_data = [vehicle for vehicle in vehicles if condition(vehicle['hp'])]
        write_json_file(category_file, category_data)

    brands = set(vehicle['brand'] for vehicle in vehicles)
    for brand in brands:
        brand_file = os.path.join(output_dir, brand.lower() + '.json')
        brand_data = [vehicle for vehicle in vehicles if vehicle['brand'].lower() == brand.lower()]
        write_json_file(brand_file, brand_data)
