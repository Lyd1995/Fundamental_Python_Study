import  NearestPoints

def main():
    numberOfPoints=eval(input("Enter number of points: "))

    points=[]
    for i in range(numberOfPoints):
        point=2*[0]
        # point=2*[0]
        point[0],point[1]=eval(input("Enter coordinates separated by a comma: "))
        points.append(point)

    p1,p2,min=NearestPoints.nearestPoints(points)

    print("The closest two points are (",
          points[p1][0],",",points[p1][0],")  (",
          points[p2][0],",",points[p2][1],")")
    print("The distance is",min)

main()
