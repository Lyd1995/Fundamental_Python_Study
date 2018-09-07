def distance(x1,y1,x2,y2):
    return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)

def nearestPoints(points):
    p1,p2=0,1
    min_distance=distance(points[p1][0],points[p1][1],points[p2][0],points[p2][1])
    for i in range(len(points)):
        for j in range (i+1,len(points)):
            d = distance(points[i][0], points[i][1], points[j][0], points[j][1])

            if min_distance>d:
                min_distance=d
                p1,p2=i,j

    return p1,p2,min_distance
