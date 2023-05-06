def update_values_quadratic(a, b, c, points, lr):
    delta_a = 0
    delta_b = 0
    delta_c = 0
    for x, y in points:
        a_change = -2 * x**2 * (y-(a*x**2)-b*x-c)
        b_change = -2 * x * (y-(a*x**2)-b*x-c)
        c_change = -2 * (y-(a*x**2)-b*x-c)
        delta_a += a_change * -lr
        delta_b += b_change * -lr
        delta_c += c_change * -lr
    return a + delta_a, b + delta_b, c + delta_c

def create_quadratic(a, b, c):
    def gooba(x):
        return a*x**2 + b*x + c
    return gooba, f"{a}x^2 + {b}x + {c}"


def update_values_linear(a, b, points, lr):
    delta_a = 0
    delta_b = 0
    for x, y in points:
        a_change = -2*x * (y-a*x-b)
        b_change = -2 * (y-a*x-b)
        delta_a += a_change * -lr
        delta_b += b_change * -lr
    delta_a / len(points)
    delta_b / len(points)
    return a + delta_a, b + delta_b

def find_point_bounds(points):
    smallest_x = None
    smallest_y = None
    biggest_x = None
    biggest_y = None

    for x, y in points:
        if smallest_x == None:
            smallest_x = x
            smallest_y = y
            biggest_x = x
            biggest_y = y
        else:
            if x < smallest_x:
                smallest_x = x
            elif x > biggest_x:
                biggest_x = x
            if y < smallest_y:
                smallest_y = y
            elif y > biggest_y:
                biggest_y = y
    
    return [smallest_x, biggest_x, smallest_y, biggest_y]