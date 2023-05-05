def update_values(a, b, c, points, lr):
    delta_a = 0
    delta_b = 0
    delta_c = 0
    for x, y in points:
        a_change = -2 * x**2 * (y-a*x**2-b*x-c)
        b_change = -2 * x * (y-a*x**2-b*x-c)
        c_change = -2 * (y-a*x**2-b*x-c)
        delta_a += a_changedelta