# Romanian Map

romanian_map = {
    'Arad': {'Sibiu':140, 'Zerind':75, 'Timisoara':118},
    'Zerind': {'Arad':75, 'Oradea':71},
    'Oradea': {'Zerind':71, 'Sibiu':151},
    'Sibiu': {'Arad':140, 'Oradea':151, 'Fagaras':99, 'Rimnicu':80},
    'Timisoara': {'Arad':118, 'Lugoj':111},
    'Lugoj': {'Timisoara':111, 'Mehadia':70},
    'Mehadia': {'Lugoj':70, 'Drobeta':75},
    'Drobeta': {'Mehadia':75, 'Craiova':120},
    'Craiova': {'Drobeta':120, 'Rimnicu':146, 'Pitesti':138},
    'Rimnicu': {'Sibiu':80, 'Craiova':146, 'Pitesti':97},
    'Fagaras': {'Sibiu':99, 'Bucharest':211},
    'Pitesti': {'Rimnicu':97, 'Craiova':138, 'Bucharest':101},
    'Bucharest': {'Fagaras':211, 'Pitesti':101, 'Giurgiu':90, 'Urziceni':85},
    'Giurgiu': {'Bucharest':90},
    'Urziceni': {'Bucharest':85, 'Vaslui':142, 'Hirsova':98},
    'Hirsova': {'Urziceni':98, 'Eforie':86},
    'Eforie': {'Hirsova':86},
    'Vaslui': {'Iasi':92, 'Urziceni':142},
    'Iasi': {'Vaslui':92, 'Neamt':87},
    'Neamt': {'Iasi':87}
}


def bfs(startingNode, destinationNode, G):
    reached = [] # to store reached (generated) nodes
    expand_sequence = [] # to store the order of nodes expanded
    frontier = []

    snode = {'City':startingNode,'Path cost':0, 'Path':[startingNode]}
    frontier.append(snode)    # insert the starting node
    reached.append(startingNode)

    while len(frontier) > 0:
        print(frontier)
        unode  = frontier.pop(0)     # selceting the node to expand
        u = unode['City']
        expand_sequence.append(u)
        print(u + " expanding..")
        # expand u

        for v in G[u].keys():
            if v not in reached: # process if v is not reached (generated) yet
                print(v+" generated.")
                cost = unode['Path cost'] + G[u][v]
                path =  unode['Path']+ [v]
                vnode = {'City': v,'Path cost': cost,'Path': path}
                frontier.append(vnode)# store the new child node in the frontier
                reached.append(v)
                # goal test
                if v == destinationNode:
                    #print(vnode)
                    print(expand_sequence)
                    return vnode # breaking from while
    print('Failed')


bfs('Arad', 'Bucharest', romanian_map)  # change the source and destination