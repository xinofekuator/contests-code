import numpy as np
import math
import random
import os


class Satellite:
    LAT_LOWER_BOUND = -324000
    LAT_UPPER_BOUND = 324000
    LON_LOWER_BOUND = -648000
    LON_UPPER_BOUND = 647999

    # lat: -324000 (90S) to 324000 (90N)
    # lon: -648000 (180W) to 647999 (179 59' 59'' E). It wraps around, so -648001 = 647999
    def __init__(self, lat, lon, velocity, orientation_change, orientation_amplitude):
        self.lat = lat
        self.lon = lon
        self.velocity = velocity
        self.orientation_change = orientation_change
        self.orientation_amplitude = orientation_amplitude

    def advance(self):
        advance_value = self.lat + self.velocity
        if advance_value > self.LAT_UPPER_BOUND:
            self.lat = - self.LON_LOWER_BOUND - advance_value
            self.lon = self.LON_LOWER_BOUND + (self.lon - 15)
            if self.lon < self.LON_LOWER_BOUND:
                self.lon = -self.LON_LOWER_BOUND - (self.LON_LOWER_BOUND - self.lon)
            self.velocity = - self.velocity
        elif advance_value < self.LAT_LOWER_BOUND:
            self.lat = self.LON_LOWER_BOUND - advance_value
            self.lon = self.LON_LOWER_BOUND + (self.lon - 15)
            if self.lon < self.LON_LOWER_BOUND:
                self.lon = -self.LON_LOWER_BOUND - (self.LON_LOWER_BOUND - self.lon)
            self.velocity = - self.velocity
        else:
            self.lat = advance_value
            self.lon = self.lon - 15
            if self.lon < self.LON_LOWER_BOUND:
                self.lon = -self.LON_LOWER_BOUND - (self.LON_LOWER_BOUND - self.lon)


class Orbit:
    def __init__(self, simulation_time, satellite):
        self.simulation_time = simulation_time
        self.satellite = satellite
        self.points = list()
        for i in range(simulation_time):
            self.points.append([satellite.lat, satellite.lon])
            satellite.advance()
        self.points_enumerate = list(enumerate(self.points))
        self.photos_taken = dict()

    def take_photo(self, photo_coordinates, time_range):
        d = self.satellite.orientation_amplitude
        photo_allowed = False
        start_turn = time_range[0]
        end_turn = time_range[1]
        valid_turns = [i for i,x in self.points_enumerate if
                      (i>=start_turn and i<=end_turn and photo_coordinates[0] >= x[0] - d and photo_coordinates[0] <= x[0] + d
                       and photo_coordinates[1] >= x[1] - d and photo_coordinates[1] <= x[1] + d)]
        print('TURNS:{}'.format(len(valid_turns)))
        for turn_aux in valid_turns:
            if self.is_photo_possible(photo_coordinates, turn_aux):
                photo_allowed = True
                print('DEBUG: PHOTO.{}:{} TURN.{}'.format(photo_coordinates[0],photo_coordinates[1],turn_aux))
                self.photos_taken[turn_aux] = photo_coordinates
                break
        return photo_allowed

    def is_photo_possible(self, photo_coordinates, turn_aux):
        photos_ordered = list(self.photos_taken.keys())
        dx = self.points[turn_aux][0] - photo_coordinates[0]
        dy = self.points[turn_aux][1] - photo_coordinates[1]
        for i in photos_ordered:
            dx_aux = self.points[i][0] - self.photos_taken[i][0]
            dy_aux = self.points[i][1] - self.photos_taken[i][1]
            # if abs(turn_aux-i)<round(self.satellite.orientation_amplitude/self.satellite.orientation_change)*2:
            diff_dx = abs(dx - dx_aux)
            diff_dy = abs(dy - dy_aux)
            if abs(turn_aux-i)<round((diff_dx + diff_dy)/self.satellite.orientation_change):
                # print('NO!! dx:{} dy:{} dx_aux:{} dy_aux:{} dx_diff:{} dy_diff:{} value:{} turns: {}'.format(dx, dy, dx_aux, dy_aux, diff_dx, diff_dy, round((diff_dx + diff_dy)/self.satellite.orientation_change),abs(turn_aux-i)))
                return False
            # with open(path + 'debug' + '.out', mode='a') as f:
            #     f.write('X:{} Y:{} dx:{} dy:{} dx_aux:{} dy_aux:{} dx_diff:{} dy_diff:{} value:{} turns: {}\n'.format(photo_coordinates[0],photo_coordinates[1],dx, dy, dx_aux, dy_aux, diff_dx, diff_dy, round((diff_dx + diff_dy)/self.satellite.orientation_change),abs(turn_aux-i)))
        return True


def get_distance(self, actual_lat_position, photo_lat_position):
    corrected_actual_lat = actual_lat_position + 324000
    corrected_photo_lat = photo_lat_position + 324000
    distance = abs(corrected_actual_lat - corrected_photo_lat) - self.satellite.orientation_amplitude
    return distance

def correct_lat(self, wrong_lat):
    lat_lower_bound = -324000
    lat_upper_bound = 324000
    lon_lower_bound = -648000
    if wrong_lat > lat_upper_bound:
        correct_lat = - lon_lower_bound - wrong_lat
    elif wrong_lat < lat_lower_bound:
        correct_lat = lon_lower_bound - wrong_lat
    else:
        correct_lat = wrong_lat
    return correct_lat


def correct_lon(self, wrong_lon):
    lon_lower_bound = -648000
    if wrong_lon < lon_lower_bound:
        correct_lon = -lon_lower_bound - (lon_lower_bound - wrong_lon)
    else:
        correct_lon = wrong_lon
    return correct_lon


path = 'C:/Users/Ignacio/PycharmProjects/hashCode/src/problem final round/'

# name_files = ['forever_alone']
name_files = ['weekend']
# name_files = ['constellation','forever_alone','overlap','weekend']

for name_file in name_files:
    with open(path + name_file + '.in', mode='r') as f:
        simulation_time = int(f.readline().split()[0])
        n_satellites = int(f.readline().split()[0])
        satellites = list()
        for i in range(n_satellites):
            lat, lon, velocity, orientation_change, orientation_amplitude = [int(x) for x in f.readline().split()]
            satellites.append([lat, lon, velocity, orientation_change, orientation_amplitude])
        n_collections = int(f.readline().split()[0])
        collections = list()
        for i in range(n_collections):
            score, n_locations, n_time_ranges = [int(x) for x in f.readline().split()]
            images = list()
            for j in range(n_locations):
                lat, lon = [int(x) for x in f.readline().split()]
                images.append([lat, lon])
            times = list()
            for k in range(n_time_ranges):
                t_start, t_end = [int(x) for x in f.readline().split()]
                times.append([t_start, t_end])
            collections.append([score, images, times])

    collections.sort(key=lambda x: x[0], reverse=True)

    satellite_objects = list()
    orbit_objects = list()
    for i in satellites:
        satellite_objects.append(Satellite(i[0], i[1], i[2], i[3], i[4]))
    for i in satellite_objects:
        orbit_objects.append(Orbit(simulation_time, i))
    for i in collections[0:1]:
        # iterate over the images
        for j in i[1]:
            # iterate over the time ranges
            for k in i[2]:
                photo_taken = False
                for o in orbit_objects[0:1]:
                    photo_taken = o.take_photo2(j, k)
                    if photo_taken:
                        break
                if photo_taken:
                    break

    instructions = list()
    for i, j in enumerate(orbit_objects):
        for m, n in j.photos_taken.items():
            instructions.append('{} {} {} {}\n'.format(n[0], n[1], m, i))

    with open(path + name_file + '.out', mode='w') as f:
        f.write('{}\n'.format(len(instructions)))
        for text in instructions:
            f.write(text)

# i = 0
# while i<1000:
#     [i for i,x in s if (125347 >= x[0] - 4197 and 125347 <= x[0] + 4197 and -33096>=x[1] - 4197 and -33096<=x[1] - 4197)]
#     print(i)
#     i += 1
