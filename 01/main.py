#! /usr/bin/env python

def load_data(path):
    data = []
    with open(path) as in_f:
        for line in in_f:
            clean = line.strip()
            if clean:
                data.append(int(clean))
    return data


def find_pair(data):
    for x in data:
        for y in data:
            if x + y == 2020:
                return x, y
    raise Exception("pair not found")


def find_triple(data):
    for x in data:
        for y in data:
            for z in data:
                if x + y + z == 2020:
                    return x, y, z
    raise Exception("triple not found")


if __name__ == "__main__":
    data = load_data("01/data")
    
    x, y = find_pair(data)
    print(x * y)

    x, y, z = find_triple(data)
    print(x * y * z)
