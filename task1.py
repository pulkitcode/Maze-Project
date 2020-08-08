def build_cave(data):
    
    """Building a 2d matrix
        Checking with brute Force every invalid condition"""
    
    
    # MAKING A MATRIX OF GIVEN SIZE
    
    matrix = [[0 for x in range(data['size'])] for y in range(data['size'])] 
    
    
    # Checking given conditions
    
    if len(data)==0:
        return None
    
    if data["size"] <= 0: 
        return None

    if "entrance" in data:
        if len([data["entrance"]])>1:
            return None
    
    if "exit" in data:
        if len([data["exit"]])>1:
            return None
     
    
    # Checking the given conditions
    
    if "entrance" not in data:
        return None
    if "exit" not in data:
        return None
    if "size" not in data:
        return None
    
    
    
    if "walls" not in data and "treasure" not in data and "sword" not in data:
        
        return None
    
    
    # Getting the coordinates near dragon
    
    if "dragon" in data:
        
    
        
            locations_near_dragon = []
            
            dx = data["dragon"][0]
            dy = data["dragon"][1]
            
            
            locations_near_dragon.append((dx - 1, dy))

            locations_near_dragon.append((dx, dy - 1))

            locations_near_dragon.append((dx + 1, dy))

            locations_near_dragon.append((dx, dy + 1))

            locations_near_dragon.append((dx + 1, dy - 1))

            locations_near_dragon.append((dx - 1, dy + 1))
            
            locations_near_dragon.append((dx + 1, dy + 1))

            locations_near_dragon.append((dx - 1, dy - 1))
    
    
    # Checking whether entrance lies near dragon
    
    if "dragon" in data:
        if "entrance" in locations_near_dragon:
                return None
    
    
    
    if "size" not in data:
        return None
    
    if data["size"] <= 0:
        return None
    
    
    
    
    if "exit" not in data:
        
        return None
    
    
    if "treasure" in data:
        if (len(data["treasure"]))>3:
            return None
        
        if (len(data["treasure"]))<0:
            return None
        
        # Making Treasure as $
        
        else:
                
            list1 = []
        
            for i in range(0, len(data["treasure"])):
                list1.append(data["treasure"][i])
            
        for k, j in list1:

            matrix[k][j] = "$"
    
    # Making Entrance as @
    # Making Exit as X
    
    matrix[data['entrance'][0]][data['entrance'][1]] = "@"
    matrix[data['exit'][0]][data['exit'][1]] = "X"
    
    # Making Dragon as W
    
    if "dragon" in data:
        
        if (data["dragon"][0] < 0 or data["dragon"][0] > data["size"] or
            data["dragon"][1] < 0 or data["dragon"][1] > data["size"]):
            return None
        
        if (len([data["dragon"]]))>1:
            return None
        
        elif (len([data["dragon"]]))==1:
            matrix[data['dragon'][0]][data['dragon'][1]] = "W"
    
    # Making Sword as t
    
    if "sword" in data:    
        
        if (len([data["sword"]]))>1:
            return None
        
        elif (len([data["sword"]]))==1:
            matrix[data['sword'][0]][data['sword'][1]] = "t"

    
    
    # Making Walls as #
    
    if "walls" in data: 
        
        list2=[]
        
        for i in range(0, len(data["walls"])):
            
            list2.append(data["walls"][i])

        for k, j in list2:

            matrix[k][j] = "#"
            
    
    
    for m in range(0, data["size"]):
        for n in range(0, data["size"]):
           
            if matrix[m][n] == 0:
                
                matrix[m][n]="."
        
    return matrix