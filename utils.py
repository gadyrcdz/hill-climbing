OBJECT_EMPTY = None
OBJECT_HOUSE = "🏠"
OBJECT_HOSPITAL = "🏥"

MOVE_UP = (0, -1)
MOVE_DOWN = (0, 1)
MOVE_LEFT = (-1, 0)
MOVE_RIGHT = (1, 0)


def is_free_to_move(map, move):
    x, y = move
    return map[y][x] == OBJECT_EMPTY


def is_valid_move(map, move):
    x, y = move
    rows = len(map)
    cols = len(map[0]) if rows > 0 else 0
    return 0 <= x < cols and 0 <= y < rows


def find_objects(map, target_object_symbol):
    coords = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == target_object_symbol:
                coords.append((x, y))
    return coords


def result(map, hospital_coordinates, target_move):
    import copy
    new_map = copy.deepcopy(map)
    hx, hy = hospital_coordinates
    tx, ty = target_move
    new_map[hy][hx] = OBJECT_EMPTY
    if (hx, hy) != (tx, ty):
        new_map[ty][tx] = OBJECT_HOSPITAL
    return new_map


def manhattan(pos, pos_2):
    return abs(pos_2[0] - pos[0]) + abs(pos_2[1] - pos[1])


def cost(map):
    hospitals = find_objects(map, OBJECT_HOSPITAL)
    houses = find_objects(map, OBJECT_HOUSE)
    total = 0
    for hospital in hospitals:
        for house in houses:
            total += manhattan(hospital, house)
    return total


def move(pos, pos_2):
    return (pos[0] + pos_2[0], pos[1] + pos_2[1])


def actions(map, hospital_position):
    valid_actions = []
    for direction in [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]:
        target = move(hospital_position, direction)
        if is_valid_move(map, target) and is_free_to_move(map, target):
            valid_actions.append(target)
    return valid_actions