def areahouse_fun(l,w):
    area=l*w
    return area * tiles
    print("Area of House=",area)
    

def tiles_fun(l,w):
    tiles=l*w
    notiles=area/tiles
    return tiles
    print("No of Tiles=",noties)
    
def tilesprice_fun(p):
    tilesprice=notiles*p
    print("Total cost of Tiles=",tilesprice)
def labourcost_fun(sqrft):
    labaourcost=area*sqrft
    print("Total Labour cost=",labourcost)
    
areahouse_fun(l=int(input("enter value of legth")),
              w=int(input("enter value of width"))
              )
tiles_fun(
          l=int(input("enter value of legth")),
            w=int(input("enter value of width"))
          )
tilesprice_fun(p=int(input("enter price one tiles")))
labourcost_fun(sqrft=int(input("enter per square feet price")))
