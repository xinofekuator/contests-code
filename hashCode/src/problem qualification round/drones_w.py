import numpy as np
import math
import random

path = 'C:/Users/Ignacio/PycharmProjects/hashCode/src/problem qualification round/'

name_files = ['mother_of_all_warehouses', 'busy_day', 'redundancy']
# name_files = 'mother_of_all_warehouses'
# name_file = 'busy_day'
# name_file = 'redundancy'

#def execute(name_file):

for name_file in name_files:
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

    warehouses_info = warehouses.copy()
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

    def dist (a,b):
        distance = math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
        rounded_distance = math.ceil(distance)
        return rounded_distance

    def turns (actual_turn):
        return math.ceil(((n_turns - actual_turn) / n_turns)*100)

    def get_cost(order):
        w = getWeight(order[2]) // max_payload
        max_dist = dist([0,0],[300,500])
        d = 0
        for i in order[2]:
            warehouse_counter = get_warehouse(i,order)
            d += dist([order[0],order[1]],[warehouses[warehouse_counter][0],warehouses[warehouse_counter][1]])
        return w + (d/max_dist)*10

    def get_cost2(order):
        w = getWeight(order[2]) // max_payload
        d = 0
        for i in order[2]:
            warehouse_counter = get_warehouse(i,order)
            d += dist([order[0],order[1]],[warehouses[warehouse_counter][0],warehouses[warehouse_counter][1]])
        return d * w

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

    def get_warehouse(product,order):
        result = list()
        for w in range(n_warehouses):
            if warehouses_info[w][2][product]>0:
                result.append([w,dist([order[0],order[1]],[warehouses[w][0],warehouses[w][1]])])
        if len(result) is 0:
            return None
        else:
            result.sort(key = lambda x : x[1], reverse = False)
            return result[0][0]

    def product_avaiable(products_ordered,order):
        stock = True
        for i in products_ordered:
            if get_warehouse(i,order) is None:
                stock = False
        return stock

    # orders.sort(key = lambda x : dist([x[0],x[1]],[warehouses[0][0],warehouses[0][1]]), reverse = False)

    orders.sort(key = lambda x : get_cost(x), reverse = False)

    instructions = list()

    drone_counter = 0
    for i in range(n_orders):
        if product_avaiable(orders[i][2],orders[i]):
            drones_needed = (getWeight(orders[i][2])//max_payload) + 1
            #separate the orders in several groups
            split = split_delivery(orders[i][2],drones_needed)
            for deliveries in split:
                for j in deliveries:
                    warehouse_counter = get_warehouse(j,orders[i])
                    warehouses_info[warehouse_counter][2][j] -= 1
                    # f.write('{} L {} {} {}\n'.format(drone_counter%n_drones,warehouse_counter,j,1))
                    instructions.append('{} L {} {} {}\n'.format(drone_counter%n_drones,warehouse_counter,j,1))
                for j in deliveries:
                    # f.write('{} D {} {} {}\n'.format(drone_counter%n_drones,orders[i][3],j,1))
                    instructions.append('{} D {} {} {}\n'.format(drone_counter%n_drones,orders[i][3],j,1))
                drone_counter += 1

    with open(path + name_file + '.out', mode='w') as f:
        f.write('{}\n'.format(len(instructions)))
        for text in instructions:
            f.write(text)
