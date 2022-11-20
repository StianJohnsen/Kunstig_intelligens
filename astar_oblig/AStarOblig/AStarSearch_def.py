def AStarSearch(self, startVertexName = None, targetVertexName = None):
        self.initPygame()

        start_node = self.vertecies[startVertexName] # Initialize starting nodes
        end_node = self.vertecies[targetVertexName]

        open_list = [start_node]

        self.pygameState(start_node,self.BLUE)
        self.pygameState(end_node,self.RED)

        while open_list: # The whole algorithm is done within this while loop
            current_node = open_list[0]
            self.pygameState(current_node,self.GREEN)
            for i in open_list:
                if i.f < current_node.f: # Smallest f is the best f
                    current_node = i
            
            current_node.known = True
            open_list.remove(current_node)

            if current_node == end_node:
                break # We're done when we have reached our final destination

            for neighbor in current_node.adjecent:
                if neighbor.vertex.known:
                    continue # No need in checking current neighbor if it has already been checked

                self.pygameState(neighbor.vertex,self.PINK)
                
                neighbor.vertex.g = current_node.g + 1# Should use neighbor.vertex.distance instead of 1, if weight is changing

                neighbor.vertex.h = self.heuristics(neighbor.vertex.name,targetVertexName) # Setting the heuristic value
                neighbor.vertex.f = neighbor.vertex.g + neighbor.vertex.h # f(n) = g(n) + h(n) equation
                neighbor.vertex.previous = current_node # Keeping track of previous nodes
                neighbor.vertex.known = True

                open_list.append(neighbor.vertex)   

            self.pygameState(current_node,self.LIGHTGREY)

        for n in self.getPath(startVertexName, targetVertexName):
            self.pygameState(n,self.DARKGREEN)
        return self.getPath(startVertexName, targetVertexName) 
   