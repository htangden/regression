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
    delta_a / len(points)
    delta_b / len(points)
    delta_c / len(points)
    return a + delta_a, b + delta_b, c + delta_c


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