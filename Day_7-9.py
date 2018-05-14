cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    return ", ".join(cars['Jeep'])


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    lst = []
    for make, model in cars.items():
        lst.append(model[0])
    return lst


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    lst = []
    for make, model in cars.items():
        for version in model:
            if grep.upper() in version.upper():
                lst.append(version)
    return sorted(lst)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    for make, model in cars.items():
        cars[make] = sorted(model)
    return cars


def main():
    print(get_all_jeeps())
    print(get_first_model_each_manufacturer())
    print(get_all_matching_models())
    print(sort_car_models())


main()
