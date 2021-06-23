import csv

with open("../WGUPS_C950_CHRIS_BRUNDIGE/distance_2.csv") as readMe:
    reader = csv.reader(readMe)
    locations = [pkg[1:] for pkg in reader]

start = [0, 0]
current_pos = start
route = []
load = [20, 1, 4, 5, 11, 8, 10, 2, 12, 13, 14, 15, 16, 19, 17]
nxt_stop = []
closest_stop = []
total_distance = 0
current_min = 50

while len(load) > 0:
    # searches pkg in load and returns the one closes to the current position
    for pkg in load:
        coord = [pkg, current_pos[0]]
        pkg_distance = float(locations[coord[0]][coord[1]])
        if pkg_distance < current_min and pkg_distance != 0.0:
            current_min = pkg_distance
            closest_stop = coord

            distance = float(locations[coord[0]][coord[1]])
    total_distance += closest_stop[0]
    route.append(closest_stop)
    current_pos[0] = closest_stop[0]
    current_pos[1] = closest_stop[1]
    if current_pos[0] in load:
        load.remove(current_pos[0])
    current_min = 999  # resets min for nxt number, 999 is just an arbitrary high
print("****************************************************")
print("closest_stop", closest_stop, "distance", distance, "route:", route, "current position", current_pos, "load",
      load,"total miles",total_distance )
