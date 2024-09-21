from point import *

def interpolate_1d(point1, point2, target_pos, is_x_coord=True):
    ratio_1 = (abs(point1.pos.x - target_pos.x) if is_x_coord else abs(point1.pos.y - target_pos.y)) / \
               (abs(point2.pos.x - point1.pos.x) if is_x_coord else abs(point2.pos.y - point1.pos.y))

    value = round((1 - ratio_1) * point1.value + ratio_1 * point2.value, 4)

    return Point(value, Position(target_pos.x, point1.pos.y) if is_x_coord else Position(point1.pos.x, target_pos.y))

def interpolate_2d(left_top, right_top, left_bottom, right_bottom, target_pos):
    h_top_point = interpolate_1d(left_top, right_top, target_pos)
    h_bottom_point = interpolate_1d(left_bottom, right_bottom, target_pos)
    v_point = interpolate_1d(h_top_point, h_bottom_point, target_pos, False)

    for point in (h_top_point, h_bottom_point, v_point):
        point.info()

    return v_point

p1 = Point(120, Position(0, 0))
p2 = Point(100, Position(1, 0))
p3 = Point(60, Position(0, 1))
p4 = Point(30, Position(1, 1))

test2 = interpolate_2d(p1, p2, p3, p4, Position(0.8, 0.7))
