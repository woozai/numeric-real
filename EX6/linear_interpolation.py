

def linearInterpolation(table_points, point):
    p = []
    result = 0
    flag = 1
    for i in range(len(table_points)):
        p.append(table_points[i][0])
    for i in range(len(p) - 1):
        if i <= point <= i + 1:
            x1 = table_points[i][0]
            x2 = table_points[i + 1][0]
            y1 = table_points[i][1]
            y2 = table_points[i + 1][1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print( "\nThe approximation (interpolation) of the point ", point, " is: ", round(result, 4))
            flag = 0
    if flag:
        x1 = table_points[0][0]
        x2 = table_points[1][0]
        y1 = table_points[0][1]
        y2 = table_points[1][1]
        m = (y1 - y2) / (x1 - x2)
        result = y1 + m * (point - x1)
        print( "\nThe approximation (extrapolation) of the point ", point, " is: ", round(result, 4))


if __name__ == '__main__':

    table_points = [(1.2, 3.5095), (1.3, 3.6984), (1.4, 3.9043), (1.5, 4.1293), (1.6, 4.3756)]
    x = 1.37
    print( "----------------- Interpolation & Extrapolation Methods -----------------\n")
    print( "Table Points: ", table_points)
    print( "Finding an approximation to the point: ", x)
    linearInterpolation(table_points, x)
    print( "\n---------------------------------------------------------------------------\n")