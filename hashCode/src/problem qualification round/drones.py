import numpy as np
import math
import random

path = 'C:/Users/Ignacio/PycharmProjects/hashCode/src/problem qualification round/'

name_file = 'mother_of_all_warehouses'
# name_file = 'busy_day'
#name_file = 'redundancy'

#def execute(name_file):

with open(path + name_file + '.in', mode='r') as f:
    n_rows, n_columns, n_drones, n_turns, max_payload = [int(x) for x in f.readline().split()]
    n_product_types = int(f.readline().split()[0]) #len of weights
    weights = [int(x) for x in f.readline().split()]
    n_warehouses = int(f.readline().split()[0]) #len of warehouses
    warehouses = list()
    for i in range(n_warehouses):
        x,y = [int(x) for x in f.readline().split()]
        products = [int(x) for x in f.readline().split()]
        warehouses.append([x,y,products])
    n_orders = int(f.readline().split()[0]) #len of orders
    orders = list()
    for i in range(n_orders):
        x,y = [int(x) for x in f.readline().split()]
        n_items = int(f.readline().split()[0]) #len of products
        products = [int(x) for x in f.readline().split()] #types of the product orders
        orders.append([x,y,products])

for i in range(len(orders)):
    orders[i].append(i)

original_orders = orders.copy()

def getWeight(products):
    total_weight = 0
    for i in products:
        total_weight = total_weight + weights[i]
    return total_weight

order_size = list()
for i in orders:
    order_size.append(getWeight(i[2]))



orders.sort(key = lambda x : getWeight(x[2]), reverse = False)
# small_orders = orders[0:140]
# big_orders = orders[140:800]

def dist (a,b):
    distance = math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
    rounded_distance = math.ceil(distance)
    return rounded_distance

def turns (actual_turn):
    return math.ceil(((n_turns - actual_turn) / n_turns)*100)

def get_cost(order):
    w = getWeight(order[2]) // max_payload
    d = dist([order[0],order[1]],[warehouses[0][0],warehouses[0][1]])
    return d * w
#
# def pack_deliveries(orders_list):
#     orders_list.sort(key = lambda x : x[0]+x[1], reverse = False)
#     counter = 0
#     packed_orders = list()
#     aux_list = list()
#     for d in orders_list:
#         counter += getWeight(d[2])
#         if counter < max_payload:
#             aux_list.append(d[3])
#         else:
#             packed_orders.append(aux_list.copy())
#             aux_list.clear()
#             counter = getWeight(d[2])
#             aux_list.append(d[3])
#     return packed_orders

# small_packed = pack_deliveries(small_orders)


# used_drones = [0 for i in range(n_drones)]
# time_drones = [0 for i in range(n_drones)]
#
# instructions = list()
#
# order_counter = 0
# drone_counter = random.randint(0,n_drones)
# for i in orders:
#     used_drones[drone_counter]=1
#     product_left = 0
#     while (product_left > 0):
#
#         instructions.append('{} L {} {} {}'.format())

#pick stuff
#pick more stuff if needed (check variable product_left)
#send the stuff and compute the time
#go back and reload

#140
#all weights are less than 200

def split_delivery(delivery,n_splits):
    res = list()
    if n_splits == 1:
        res = [delivery]
    else:
        weight_counter = 0
        aux_result = list()
        for i in delivery:
            weight_counter += weights[i]
            if weight_counter <= max_payload:
                aux_result.append(i)
            else:
                res.append(aux_result.copy())
                aux_result.clear()
                weight_counter = weights[i]
                aux_result.append(i)
        res.append(aux_result)
    return res


    #return the same if n_splits is one

# orders.sort(key = lambda x : dist([x[0],x[1]],[warehouses[0][0],warehouses[0][1]]), reverse = False)

orders.sort(key = lambda x : get_cost(x), reverse = False)

with open(path + name_file + '.out', mode='w') as f:
    drone_counter = 0
    for i in range(n_orders):
        drones_needed = (getWeight(orders[i][2])//max_payload) + 1
        #separate the orders in several groups
        split = split_delivery(orders[i][2],drones_needed)
        for deliveries in split:
            for j in deliveries:
                f.write('{} L {} {} {}\n'.format(drone_counter%n_drones,0,j,1))
            for j in deliveries:
                f.write('{} D {} {} {}\n'.format(drone_counter%n_drones,orders[i][3],j,1))
            drone_counter += 1
