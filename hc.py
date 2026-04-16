# import math

import utils
import random
import math




def hill_climbing(map):
    """
    Optimize a board by repeatedly choosing the best local move.

    This function should implement classic hill climbing: on each iteration,
    evaluate every one-step move for every hospital, choose the neighbor with
    the lowest cost, and move there only if it strictly improves the current
    cost. Stop when no improving neighbor exists.

    Pseudocode (Python-style):
    """
    current_map = map
    current_cost = utils.cost(current_map)

    while True:
        best_map = current_map
        best_cost = current_cost

        for hospital in utils.find_objects(current_map, utils.OBJECT_HOSPITAL):
            for candidate_move in utils.actions(current_map, hospital):
                candidate_map = utils.result(current_map, hospital, candidate_move)
                candidate_cost = utils.cost(candidate_map)

                if candidate_cost < best_cost:
                    best_map = candidate_map
                    best_cost = candidate_cost

        if best_cost < current_cost:
            current_map = best_map
            current_cost = best_cost
        else:
            break   

    return current_map
    """
    Args:
        map: Matrix (list of lists) representing the board.

    Returns:
        list[list]: A map configuration with locally minimized cost.
    """

    # raise NotImplementedError("hill_climbing is not implemented yet")



def simulated_annealing(grid, T_min, T_initial, cooling_rate):
    """
    Optimize hospital positions using simulated annealing by exploring random moves
    and occasionally accepting worse states to escape local optima.

    Args:
        grid: Matrix (list of lists) representing the board.
        T_min: Minimum temperature at which the search stops.
        T_initial: Starting temperature for the annealing process.
        cooling_rate: Multiplicative factor used to cool the temperature each step.

    Returns:
        list[list]: A grid configuration produced by the annealing search.
    """

    current_grid = grid
    current_cost = utils.cost(current_grid)
    temperature =  T_initial

    while (temperature > T_min):
        movable_hospitals = utils.find_objects(current_grid, utils.OBJECT_HOSPITAL)
        if (len(movable_hospitals) == 0):
            break
        selected_hospital = random.choice(movable_hospitals)
        
        possible_moves = utils.actions(current_grid, selected_hospital)
        if(len(possible_moves) == 0):
            break

        selected_move = random.choice(possible_moves)
        neighbor_solution =  utils.result(current_grid, selected_hospital, selected_move)
        neighbor_cost = utils.cost(neighbor_solution)
        cost_difference =  neighbor_cost - current_cost

        if (neighbor_cost < current_cost):
            current_grid = neighbor_solution
        else:
            acceptance_probability = math.exp(-cost_difference / temperature)
            value = random.random()
            if  (value < acceptance_probability):
                current_grid = neighbor_solution

        temperature *= cooling_rate

    return current_grid
