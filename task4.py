from reference import build_cave, shortest_path

# FUNCTION TO GIVE THE SHORTEST PATH LIST BETWEEN TWO POINTS

def optimal_path(data):
   
    
    # BRUTE FORCED METHOD
    
    """I have tracked every possible combination and figured a way out
        Using Try and Except at every case otherwise it returns
        a none type error"""
    
    # INITIALISATION
    
    altpath = 0

    j = 0
    maze = build_cave(data)
   
    list2 = []
    list3 = []
    list5 = []
    list6 = []
    list1 = []
    list8 = []
    list9 = []
    list11 = []
    
   
     
    
    if "treasure" in data:
        
        temp_treasures = data["treasure"]
    
    
    # CHECKING BASIC CONDITIONS
    
    
    if "entrance" == "exit":
        return None
    
    
    if 'entrance' not in data:
        return None
    
    if 'exit' not in data:
        return None
    
    if "size" not in data:
        return None
    
    
    near_exit = data["exit"]
    
    list10 = []
    
    # IF TREASURE IS BLOCKED ON ALL FOUR SIDES
    
    if "treasure" in data:
        for i in data["treasure"]:
            
            near_treasure = i
    
            if near_treasure:
                locations_near_treasure = []
                
                dx = i[0]
                dy = i[1]

                locations_near_treasure.append((dx - 1, dy))

                locations_near_treasure.append((dx, dy - 1))

                locations_near_treasure.append((dx + 1, dy))

                locations_near_treasure.append((dx, dy + 1))

                count_near_treasure = 0

                for j in locations_near_treasure:
                    x = j[0]
                    y = j[1]
                    if (x in range(0, data["size"]) and
                        y in range(0, data["size"])):
                        list10.append((x, y))


                for i in list10:
                    if maze[i[0]][i[1]] == "#":
                        count_near_treasure += 1


                if count_near_treasure == len(list10):
                    return None
    
    
    # GETTING LOCATIONS NEXT TO ENTRANCE
    
    near_entrance = data["entrance"]
    
    if near_entrance:
            locations_near_entrance = []
            # W, N, E, S
            dx, dy = data["entrance"]
            
            locations_near_entrance.append((dx - 1, dy))

            locations_near_entrance.append((dx, dy - 1))

            locations_near_entrance.append((dx + 1, dy))

            locations_near_entrance.append((dx, dy + 1))
    
    # IF EXIT IS BLOCKED ON ALL FOUR SIDES
    
    if near_exit:
            locations_near_exit = []
            # W, N, E, S
            dx, dy = data["exit"]
            
            locations_near_exit.append((dx - 1, dy))

            locations_near_exit.append((dx, dy - 1))

            locations_near_exit.append((dx + 1, dy))

            locations_near_exit.append((dx, dy + 1))

            
           
    
    count_near_exit = 0
    
    for i in locations_near_exit:
        x = i[0]
        y = i[1]
        if x in range(0, data["size"]) and y in range(0, data["size"]):
            list1.append((x, y))

    
    for i in list1:
        if maze[i[0]][i[1]] == "#":
            count_near_exit += 1
    

    if count_near_exit == len(list1):
        return None
    
    # GETTING LOCATIONS NEAR DRAGON
    
    if "dragon" in data:
        
        dragon_location = data["dragon"]
   
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
            
    
    # Here I have started testing all the test cases 
    
    # Sword - YES, Dragon - YES, Treasure - NO
    
    if "sword" in data and "dragon" in data and "treasure" not in data:
        
        if "exit" in locations_near_dragon:
            
            altpath = altpath + (shortest_path(data,
                                 data["entrance"], data["sword"], False))
            
            altpath = altpath + (shortest_path(data,
                                 data["sword"], data["exit"], True))
            
            return altpath
            
        elif "exit" not in locations_near_dragon:
            
            try:
                altpath = altpath + (shortest_path(data,
                                      data["entrance"], data["exit"], False))
                
                list6.append(altpath)
                
            except:
                list6.append(100000)
                
            try:
                altpath = altpath + (shortest_path(data,
                                      data["entrance"], data["sword"], False))
                
                altpath = altpath + (shortest_path(data,
                                      data["sword"], data["exit"], True))
            
                
                list6.append(altpath)
                list6.sort()
                if list6[0] == 100000:
                    return None
                else:
                    return list6[0]
                
            except:
                list6.append(100000)
                list6.sort()
                
                if list6[0] == 100000:
                    return None
                else:
                    return list6[0]
                
    # Sword - NO, Dragon - YES, Treasure - NO
    
    if "sword" not in data and "dragon" in data and "treasure" not in data:
        
        if "exit" in locations_near_dragon:
            
            
            return None
            
        elif "exit" not in locations_near_dragon:
            
            try:
                altpath = altpath + (shortest_path(data,
                                      data["entrance"], data["exit"], False))
                
                return altpath
                
            except:
                
                return None
                
            
    
    if "sword" in data:
        
        picks_sword = True
        
        # Sword - YES, Dragon - NO, Treasure - NO
            
        if "dragon" not in data and "treasure" not in data:

            altpath = altpath + (shortest_path(data,
                                      data["entrance"], data["exit"], True))

            return altpath
        
        # here we have tested whether picking the sword would give less
        # distance or not
        
        if picks_sword:
            
            
            
            
            # Sword - YES, Dragon - YES, Treasure - YES
            
            if "treasure" in data and "dragon" in data:
           
                for m in locations_near_entrance:
                    if maze[m[0]][m[1]] == "$":
                        list11.append(m)
                
                try:
                    d = shortest_path_list(data, 
                                      data["entrance"], data["sword"], True)

                    
                    for k in list11:
                        for l in d:
                            if l==k:
                                d.remove(l)


                    for i in data["treasure"]:
                        for j in d:
                            if i==j:
                                list8.append(i)
                
                except:
                    list8 = []
                
                # WHILE TRAVERSING TO SWORD IF THE PLAYER FINDS A TREASURE 
                if len(list8)!=0:
                
                    
                        
                    altpath = altpath + shortest_path(data,
                                      data["entrance"], data["sword"], True)
                
                    
                    for j in data["treasure"]:
                        if j in list8:
                            temp_treasures.remove(j)
                    
                    if len(temp_treasures) == 0:
                        altpath = altpath + shortest_path(data,
                                      data["sword"], data["exit"], True)
                        return altpath
                    
                    try:

                        for i in temp_treasures:

                            list2.append((i, shortest_path(data,
                                               data["entrance"], i, True)))


                        if len(temp_treasures)==2:

                            if list2[0][1]<list2[1][1]:

                                temp = list2[0] 
                                list2[0] = list2[1]
                                list2[1] = temp

                       
                        if len(temp_treasures)==3:
                            for m in range(0, 2):
                                if list2[m][1]<list2[m + 1][1]:

                                    temp = list2[m] 
                                    list2[m] = list2[m + 1]
                                    list2[m + 1] = temp

                            for m in range(0, 2):
                                if list2[m][1]<list2[m + 1][1]:

                                    temp = list2[m] 
                                    list2[m] = list2[m + 1]
                                    list2[m  + 1] = temp
                        
                        # HERE LIST2 IS LIST WITH ALL TREASURES
                        
                        if len(temp_treasures)==1:

                            altpath = altpath + shortest_path(data,
                                        data["sword"], temp_treasures[0], True)

                            altpath = altpath + shortest_path(data, 
                                         temp_treasures[0], data["exit"], True)
                            
                            
                        if len(data["treasure"])==2:

                            altpath = altpath + shortest_path(data,
                                             data["sword"], list2[0][0], True)

                            altpath = altpath + shortest_path(data,
                                              list2[0][0], list2[1][0], True)

                            altpath = altpath + shortest_path(data,
                                              list2[1][0], data["exit"], True)


                        if len(data["treasure"])==3:

                            altpath = (altpath + shortest_path(data,
                                       data["sword"], list2[0][0], True))

                            altpath = (altpath + shortest_path(data,
                                       list2[0][0], list2[1][0], True))  

                            altpath = (altpath + shortest_path(data,
                                       list2[1][0], list2[2][0], True))  

                            altpath = (altpath + shortest_path(data,
                                      list2[2][0], data["exit"], True))

                 
                        return altpath

                    except:

                        return None
                        
                
                
                # WHILE TRAVERSING TO SWORD IF THE PLAYER
                # DOES NOT FIND A TREASURE
                
                else:
            
                    
                    
                    try:
                        altpath = altpath + shortest_path(data,
                                      data["entrance"], data["sword"], False)

                        for i in data["treasure"]:

                            list2.append((i, shortest_path(data,
                                               data["entrance"], i, True)))


                        if len(data["treasure"])==2:

                            if list2[0][1]<list2[1][1]:

                                temp = list2[0] 
                                list2[0] = list2[1]
                                list2[1] = temp

                        if len(data["treasure"])==3:
                            for m in range(0, 2):
                                if list2[m][1]<list2[m + 1][1]:

                                    temp = list2[m] 
                                    list2[m] = list2[m + 1]
                                    list2[m + 1] = temp
                            
                            m = 0
                            
                            for m in range(0, 2):
                                if list2[m][1]<list2[m + 1][1]:

                                    temp = list2[m] 
                                    list2[m] = list2[m + 1]
                                    list2[m + 1] = temp
                       
                        if len(data["treasure"])==1:

                            altpath = altpath + shortest_path(data,
                                      data["sword"], data["treasure"][0], True)

                            altpath = altpath + shortest_path(data,
                                      data["treasure"][0], data["exit"], True)
                            
                   
                        if len(data["treasure"])==2:

                            altpath = altpath + shortest_path(data, 
                                          data["sword"], list2[0][0], True)

                            altpath = altpath + shortest_path(data,
                                          list2[0][0], list2[1][0], True)

                            altpath = altpath + shortest_path(data,
                                          list2[1][0], data["exit"], True)

                       
                        if len(data["treasure"])==3:

                            altpath = altpath + (shortest_path(data,
                                             data["sword"], list2[0][0], True))

                            altpath = altpath + shortest_path(data, 
                                          list2[0][0], list2[1][0], True)  

                            altpath = altpath + shortest_path(data, 
                                          list2[1][0], list2[2][0], True)  

                            altpath = altpath + shortest_path(data, 
                                          list2[2][0], data["exit"], True)

          
                        list9.append(altpath)
    


                    except:
                        
                        list9.append(1000000)
    
                picks_sword = False
                
                # here we have tested whether not 
                # picking the sword would give less
                # distance or not
                
                if not picks_sword:
                    
                    altpath = 0
                    try:
                        if len(data["treasure"])==1:

                            list3.append((data["treasure"][0],
                              shortest_path(data, data["entrance"],
                                            data["treasure"][0], False)))            

                        if len(data["treasure"])==2:

                            list3.append((data["treasure"][0],
                                          shortest_path(data, data["entrance"],
                                            data["treasure"][0], False)))

                            list3.append((data["treasure"][1],
                                          shortest_path(data,
                                data["entrance"], data["treasure"][1], False)))
                            
                            
                        if len(data["treasure"])==3:

                            list3.append((data["treasure"][0], 
                                          shortest_path(data,
                                data["entrance"], data["treasure"][0], False)))  

                            list3.append((data["treasure"][1], 
                                          shortest_path(data,
                                data["entrance"], data["treasure"][1], False))) 

                            list3.append((data["treasure"][2], 
                                          shortest_path(data,
                                data["entrance"], data["treasure"][2], False))) 



                        if len(data["treasure"])==2:

                            if list3[0][1]<list3[1][1]:

                                temp = list3[0] 
                                list3[0] = list3[1]
                                list3[1] = temp



                        if len(data["treasure"])==3:
                            for m in range(0, 2):
                                if list3[m][1]<list3[m + 1][1]:

                                    temp = list3[m] 
                                    list3[m] = list3[m + 1]
                                    list3[m + 1] = temp

                        # LIST3 IS LIST WITH ALL TREASURES
                        
                        if len(data["treasure"])==1:

                                altpath = altpath + (shortest_path(data, 
                                                 data["entrance"], 
                                               data["treasure"][0], False))

                                altpath = altpath + (shortest_path(data, 
                                          data["treasure"][0],
                                               data["exit"], False))


                        elif len(data["treasure"])==2:

                            altpath = altpath + shortest_path(data,
                                                  data["entrance"],
                                                  list3[0][0], False)
                           
                            altpath = altpath + shortest_path(data,
                                                      list3[0][0], 
                                                      list3[1][0], False)

                            altpath = altpath + shortest_path(data,
                                                      list3[1][0], 
                                                      data["exit"], False)
                            
                            

                        elif len(data["treasure"])==3:

                            altpath = altpath + shortest_path(data,
                                                  data["entrance"],
                                                      list3[0][0], False)

                            altpath = altpath + shortest_path(data,
                                                      list3[0][0],
                                                      list3[1][0], False)  

                            altpath = altpath + shortest_path(data,
                                                      list3[1][0],
                                                      list3[2][0], False)  

                            altpath = altpath + shortest_path(data,
                                                      list3[2][1], 
                                                      data["exit"], False)


                        list9.append(altpath)
                        list9.sort()

                        if list9[0] == 1000000:
                            return None
                        else:
                            return list9[0]
                    except:

                        list9.append(1000000)

                        list9.sort()
                        if list9[0] == 1000000:
                            return None
                        else:
                            return list9[0]
                
           
           
    # SWORD - NO DRAGON - NO TREASURE - NO
        
    if "sword" not in data and "dragon" not in data and "treasure" not in data:

        altpath = altpath + shortest_path(data,
                                      data["entrance"], data["exit"], False)

        return altpath
            
        
        
    # SWORD - NO DRAGON - YES TREASURE - YES
    
    if "sword" not in data and "dragon" in data and "treasure" in data:

        
        for i in data["treasure"]:
            if i in locations_near_dragon:
                return None
        
        
        try:

            if len(data["treasure"])==1:

                list5.append((data["treasure"][0], shortest_path(data,
                                data["entrance"], data["treasure"][0], False)))            

            if len(data["treasure"])==2:

                list5.append((data["treasure"][0], shortest_path(data,
                                data["entrance"], data["treasure"][0], False)))

                list5.append((data["treasure"][1], shortest_path(data,
                                data["entrance"], data["treasure"][1], False)))

            if len(data["treasure"])==3:

                list5.append((data["treasure"][0], shortest_path(data,
                                data["entrance"], data["treasure"][0], False)))  

                list5.append((data["treasure"][1], shortest_path(data,
                                data["entrance"], data["treasure"][1], False))) 

                list5.append((data["treasure"][2], shortest_path(data,
                                data["entrance"], data["treasure"][2], False))) 


            if len(data["treasure"])==2:

                if list5[0][1]<list5[1][1]:

                    temp = list5[0] 
                    list5[0] = list5[1]
                    list5[1] = temp


            if len(data["treasure"])==3:
                for m in range(0, 2):
                    if list5[m][1]<list5[m + 1][1]:

                        temp = list5[m] 
                        list5[m] = list5[m + 1]
                        list5[m + 1] = temp

            if len(data["treasure"])==1:

                        altpath = altpath + shortest_path(data,
                                  data["entrance"], data["treasure"][0], False)

                        altpath = altpath + shortest_path(data,
                                      data["treasure"][0], data["exit"], False)


            elif len(data["treasure"])==2:

                altpath = altpath + shortest_path(data,
                                          data["entrance"], list5[0][0], False)

                altpath = altpath + shortest_path(data,
                                          list5[0][0], list5[1][0], False)

                altpath = altpath + shortest_path(data,
                                          list5[1][0], data["exit"], False)


            elif len(data["treasure"])==3:

                altpath = altpath + shortest_path(data,
                                      data["entrance"], list5[0][0], False)

                altpath = altpath + shortest_path(data, list5[0][0],
                                          list5[1][0], False)  

                altpath = altpath + shortest_path(data, list5[1][0],
                                          list5[2][0], False)  

                altpath = altpath + shortest_path(data,
                                          list5[2][1], data["exit"], False)

            return altpath
        
        except:
            
            return None
        
    # SWORD - NO DRAGON - NO TREASURE - YES
    
    if "sword" not in data and "dragon" not in data and "treasure" in data:
        
        try:

            if len(data["treasure"])==1:

                    list5.append((data["treasure"][0], shortest_path(data,
                                 data["entrance"], data["treasure"][0], True)))            
              
            if len(data["treasure"])==2:

                list5.append((data["treasure"][0], shortest_path(data,
                                 data["entrance"], data["treasure"][0], True)))

                list5.append((data["treasure"][1], shortest_path(data,
                                 data["entrance"], data["treasure"][1], True)))

            if len(data["treasure"])==3:

                list5.append((data["treasure"][0], shortest_path(data,
                                data["entrance"], data["treasure"][0], True)))  

                list5.append((data["treasure"][1], shortest_path(data,
                                data["entrance"], data["treasure"][1], True))) 

                list5.append((data["treasure"][2], shortest_path(data,
                                data["entrance"], data["treasure"][2], True))) 



            if len(data["treasure"])==2:

                if list5[0][1]<list5[1][1]:

                    temp = list5[0] 
                    list5[0] = list5[1]
                    list5[1] = temp


            if len(data["treasure"]) == 3:
                for m in range(0, 2):
                    if list5[m][1]<list5[m + 1][1]:

                        temp = list5[m] 
                        list5[m] = list5[m + 1]
                        list5[m + 1] = temp

            if len(data["treasure"])==1:

                        altpath = altpath + (shortest_path(data, 
                                 data["entrance"], data["treasure"][0], True))

                        altpath = altpath + (shortest_path(data,
                                     data["treasure"][0], data["exit"], True))


            elif len(data["treasure"])==2:

                altpath = altpath + (shortest_path(data,
                                      data["entrance"], list5[0][0], True))

                altpath = altpath + (shortest_path(data, 
                                           list5[0][0], list5[1][0], True))

                altpath = altpath + (shortest_path(data,
                                           list5[1][0], data["exit"], True))


            elif len(data["treasure"])==3:

                altpath = altpath + (shortest_path(data,
                                          data["entrance"], list5[0][0], True))

                altpath = altpath + (shortest_path(data,
                                          list5[0][0], list5[1][0], True))  

                altpath = altpath + (shortest_path(data,
                                          list5[1][0], list5[2][0], True))  

                altpath = altpath + (shortest_path(data,
                                          list5[2][1], data["exit"], True))

            return altpath
        except:
            return None
        

# FUNCTION WHICH IS SUPPOSED TO BE CALLED        
        
# WE USE THIS FUNCTION TO DETERMINE
# WHETHER THERE IS A TREASURE BETWEEN ENTRANCE AND SWORD

def shortest_path_list(data, start, end, has_sword):
    
    
    
    every_point_visited = []
    i=0
    j=0
    maze = build_cave(data)
    dragon_location = data["dragon"]
    rows = data["size"]
    cols = data["size"]
    
    
    # our list which has the starting node at the beginning
    unexplored = [start]
    
    # Checking basic conditions
    
    

    # Getting the 8 locations near the dragon
    
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


    
    node = start

    
    
    while unexplored: 
        
        
        if unexplored[-1] == end:
            
            return every_point_visited
        
        
        
        for i in unexplored:

            every_point_visited.append(i)
            node = i


            r = node[0]
            c = node[1]

            
            temp=[]

            for j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                
                
                # Checking whether the coordinate is in our range
                if j[0]<0 or j[1]<0:
                    continue
                if j[0]>=rows or j[1]>=cols:
                    continue
                
                # When we don't have the sword
                # Checking whether the coordinate is a wall or
                # Checking whether the coordinate is a dragon or
                # Checking whether the coordinate is already visited
                # Checking whether the coordinate is near the dragon
                
                if (not has_sword) and ("dragon" in data):  

                    if (maze[j[0]][j[1]]!="#" and j not in unexplored and
                       j != data["dragon"] and j not in
                       locations_near_dragon and j not in every_point_visited):
                        
                        
                        temp.append((j))
                        
                # Here we don't need to check the dragon conditions
                # because we have the sword
                
                else:

                    if (maze[j[0]][j[1]]!="#" and j not in unexplored and 
                        j not in every_point_visited):
                        
                        temp.append((j))
                  
        unexplored = temp
        
        