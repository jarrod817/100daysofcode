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

# numlist = [1,2,3,4,5]
# print(numlist)
# numlist.reverse()
# print(numlist)
# numlist.sort()
# print(numlist)
# for num in numlist:
#     print(str(num))
# mystring = "Jarrod"
# list(mystring)
# l = list(mystring)
# print(l[0])
# print(l.pop())
# print(l)
# l.insert(5,"d")
# print(l)
# del l[0]
# print(l)
# l.pop(1)
# print(l)
# l.append('s')
# print(l)
# mystring = "Jarrod"
# l = list(mystring)
# t = tuple(mystring)
# print(l, t)
# l[0]= "t"
# # immutable -> t[0] = "t"
# for let in t:
#     print (let)
#
# pybytes = {"jarrod": 33, "Sarah": 30 }
# print(pybytes)
# people = {}
# people["Jarrod"] = 33
# print(people)
# people["Sarah"] = 30
# print(people.keys())
# print(people.values())
# print(people.items())
# for keys in pybytes.keys():
#     print(keys)
# for keys,values in pybytes.items():
#     print("Keys:{}  Values:{}".format(keys, values))
#
# l =list("Jarrod")
# n = [1,2,3,4,5,6]
# for values in n:
#     people[values] = people.get(values,values+1)
#
# print(people.items())
