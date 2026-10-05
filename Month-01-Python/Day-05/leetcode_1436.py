class Solution:
    def destCity(self, paths):
        start_cities = []

        for path in paths:
            start_cities.append(path[0])

        for path in paths:
            destination = path[1]

            if destination not in start_cities:
                return destination
