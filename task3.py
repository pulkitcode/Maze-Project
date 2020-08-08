from reference import build_cave 
def shortest_path(data, start, end, has_sword):
    
    
    """ Basically used the pseudocode provided with lists and getting valid
    nodes at each step and counting them"""
    
    # Initialisation
    
    list4 = [data["entrance"]]
    list5 = [data["exit"]]
    all_visited = []
    i=0
    j=0
    maze = build_cave(data)
    dragon_location = data["dragon"]
    rows = data["size"]
    cols = data["size"]
    unexplored = [start]
    
    # Basic conditions
    
    if "exit" not in data:
        return None
    elif "entrance" not in data:
        return None

    elif (len(list4))>1:
        return None

    elif (len(list5))>1:
        return None

    elif (len(data["treasure"]))>3:
        return None

    # Checking the corners of the dragon location
    
    if dragon_location:
            locations_near_dragon = []
            
            dx, dy = dragon_location
            
            locations_near_dragon.append((dx - 1, dy))

            locations_near_dragon.append((dx, dy - 1))

            locations_near_dragon.append((dx + 1, dy))

            locations_near_dragon.append((dx, dy + 1))

            locations_near_dragon.append((dx + 1, dy - 1))

            locations_near_dragon.append((dx - 1, dy + 1))
            
            locations_near_dragon.append((dx + 1, dy + 1))

            locations_near_dragon.append((dx - 1, dy - 1))

    # Checking whether end near dragon
    
    if (not has_sword) and ("dragon" in data): 
        if end in locations_near_dragon:
            return None

    node = start

    count = 0
    
    # The main loop begins
    
    while unexplored: 
        
        if unexplored[0] == end:
            return count
        
        # when reach the end return no. of steps
        
        if unexplored[-1] == end:
            return count
        
        
        count = count +1
        for i in unexplored:

            # all_visited has every node which has been visited
            # to avoid redundance
            
            all_visited.append(i)
            node = i


            r = node[0]
            c = node[1]

            # All moves possible from node
            
            
            temp=[]

            for j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                
                
                # Checking which moves are valid
                if j[0]<0 or j[1]<0:
                    continue
                if j[0]>=rows or j[1]>=cols:
                    continue
                if (not has_sword) and ("dragon" in data):  

                    if (maze[j[0]][j[1]]!="#" and j not in unexplored and
                       j != data["dragon"] and j not in
                       locations_near_dragon and j not in all_visited):
                        
                        
                        temp.append((j))
                        

                else:

                    if (maze[j[0]][j[1]]!="#" and j not in unexplored and 
                        j not in all_visited):
                        
                        temp.append((j))
        
        # Keep changing unexplored with temp so as to move to another level
        unexplored = temp

        
        
        
    