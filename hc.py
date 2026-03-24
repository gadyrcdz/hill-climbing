import utils
import math


# def get_move_weight(map, hospital):
#     houses = utils.find_object(map, utils.OBJECT_HOUSE)
#     cost, coordinate = (math.inf, ())
#
#     for house in houses:
#         temp_cost = utils.manhattan(
#             hospital,
#             house,
#         )
#
#         if temp_cost < cost:
#             cost = temp_cost
#             coordinate =
#
#     return cost, coordinate


def hill_climbing(map):
    current_map = map
    current_cost = utils.cost(current_map)

    while True:
        best_map = current_map
        best_cost = current_cost

        for hospital in utils.find_objects(current_map, utils.OBJECT_HOSPITAL):
            for temp_hospital_move in utils.actions(current_map, hospital):
                temp_map = utils.result(current_map, hospital, temp_hospital_move)
                temp_cost = utils.cost(temp_map)

                if temp_cost < best_cost:
                    best_map = temp_map
                    best_cost = temp_cost

        if best_cost < current_cost:
            current_map = best_map
            current_cost = best_cost
        else:
            break

    return current_map
