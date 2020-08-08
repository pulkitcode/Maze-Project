from reference import build_cave 
def check_path(data, path):
    
    """To check the path given by converting each move into a step in a 
        matrix"""
    
    
    # INITIALISATION
    
    given_path = []
    
    index=0
    sword_index=0
    dragon_index=0
    
    enter = data["entrance"]
    
    given_path.append(data["entrance"])
    
    # Building a maze for reference
    
    maze = build_cave(data)
    
    # Getting the path
    
    for i in path:
        
        # South
        if i == "S":
            given_path.append((enter[0] + 1, enter[1]))
            
            enter =  (enter[0] + 1, enter[1])
            
        # West         
        elif i == "W":
            given_path.append((enter[0], enter[1] - 1))
            
            enter =  (enter[0], enter[1] - 1)
            
        # East            
        elif i == "E":
            given_path.append((enter[0], enter[1] + 1))
            
            enter =  (enter[0], enter[1] + 1)
         
        # North   
        else:
            given_path.append((enter[0] - 1, enter[1]))
            
            enter =  (enter[0] - 1, enter[1])
                
    for i in given_path:
        
        index=+1
        
        # Checking all the conditions
        if data["exit"] not in given_path:
            return False
        
        
        if "walls" in data:
            if maze[i[0]][i[1]] == "#":
                return False
        
        # Checking that if the player has picked up the sword
        # does he encounter the dragon before picking it up or after
        # Keeping the track of index of both
        
        if data["sword"] in given_path:
            sword_index = index
                
        if data["dragon"] in given_path:
            dragon_index = index    
            
                
        
    if sword_index > dragon_index:
        return False
    
    return True