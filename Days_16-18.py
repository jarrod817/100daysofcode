import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
TITAL = [name.title() for name in NAMES]
print(TITAL)


def gen_pairs():
    for _ in NAMES:
        yield random.choice(NAMES)


pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))


def gen_1_name():
    for _ in NAMES:
        yield random.choice(NAMES)


def gen_2_name():
    for _ in NAMES:
        yield random.choice(NAMES)


for _ in range(10):
    print("{} teams up with {}".format(next(gen_1_name()).split()[0].title(), next(gen_2_name()).split()[0].title()))
