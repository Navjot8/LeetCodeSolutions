path ="NNNWSSSEEE"
l=[path.count(path[0])]
newpath=path[0]
if "N" in path and "E" in path and "W" in path and "S" in path:
    east=path.find("E")
    west=path.find("W")
    '''For North'''
    if path[0]=="N":
        if east<west:
            print("moving toward east")
            if path.count("W")>path.count("N"):
                print("true")
        else:
            print("moving toward west")
            if path.count("E")>path.count("N"):
                print("true")
    elif path[0]=="S":
        print("South")
        if east<west:
            print("moving toward east")
            if path.count("W")>path.count("S"):
                print("true")
        else:
            print("moving toward west")
            if path.count("E")>path.count("S"):
                print("true")
    elif path[0]=="W":
        south=path.find("S")
        north=path.find("N")
        if north<south:
            print("moving toward North")
            if path.count("W")<path.count("S"):
                print("true")
        else:
            print("moving toward west")
            if path.count("E")>path.count("S"):
                print("true")


else:
    print("False")
