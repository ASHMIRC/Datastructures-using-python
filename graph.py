class graph:
    def __init__(self,edges):
        self.edges=edges
        self.l={}
        for start,end in self.edges:
            if start in self.l:
                self.l[start].append(end)
            else:
                self.l[start]=[end]
        print(self.l)

    def pathfind(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return[path]
        if start not in self.l:
            return []
        paths=[]
        for node in self.l[start]:
            if node not in path:
                new_path=self.pathfind(node,end,path)
                for i in new_path:
                    paths.append(i)
        return paths
    def get_sortestpath(self,start,end,path=[]):
        path = path + [start]

        if start==end:
            return path
        if start not in self.l:
            return None

        spp=None
        for node in self.l[start]:
            if node not in path:
                sp=self.get_sortestpath(node,end,path)
                if sp:
                    if spp is None or len(sp)<len(spp):
                        spp=sp
        return sp



edges=[
           ('mumbai','delhi'),
           ('mumbai','ladak'),
           ('delhi','pondy'),
           ('pondy','chennai'),
           ('ladak','kochi')]
g=graph(edges)
start='mumbai'
end='pondy'

print(g.get_sortestpath(start,end))

