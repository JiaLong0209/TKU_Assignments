from point import *

def interpolation_1d(point1, point2, target_pos, is_x_coord = True):
    
    if(is_x_coord):
        ratio_1 = abs(point1.pos.x - target_pos.x) / abs(point2.pos.x - point1.pos.x);
    else:
        ratio_1 = abs(point1.pos.y - target_pos.y) / abs(point2.pos.y - point1.pos.y);

    ratio_2 = 1 - ratio_1;
    a = round(ratio_2 * point1.value, 4)
    b = round(ratio_1 * point2.value, 4)
    value = a + b

    if(is_x_coord):
        return Point(value, Position(target_pos.x, point1.pos.y)) 
    else:
        return Point(value, Position(point1.pos.x, target_pos.y))


def interpolation_2d(left_top, right_top, left_bottom, right_bottom, target_pos):
    h_top_point = interpolation_1d(left_top, right_top, target_pos)
    h_bottom_point = interpolation_1d(left_bottom, right_bottom, target_pos)


    v_point = interpolation_1d(h_top_point, h_bottom_point, target_pos, False)

    h_top_point.info()
    h_bottom_point.info()
    v_point.info()

    return v_point

p1 = Point(120, Position(0, 0))
p2 = Point(100, Position(1, 0))
p3 = Point(60, Position(0, 1))
p4 = Point(30, Position(1, 1))

# test = interpolation_1d(p1, p3, Position(0, 0.2), True)
# test.info()

test2 = interpolation_2d(p1, p2, p3 ,p4, Position(0.8, 0.7))

