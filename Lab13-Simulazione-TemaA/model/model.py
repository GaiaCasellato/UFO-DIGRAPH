import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.stati = DAO.getAllStates()
        self._nodes = []
        self._edges = []

    def buildGraph(self, anno):
        self.grafo.clear()
        self.stati_anno = DAO.getNodi(anno)

        self.idMap = {}
        for i in self.stati:
            self.idMap[i.id]= i
        for k in self.stati_anno:
            self.grafo.add_node(self.idMap[k.upper()])
        for i in self.grafo.nodes:
            for j in self.grafo.nodes:
                    self._edges = DAO.getArchi(i.id,j.id,anno)
                    for g in self._edges:
                        self.grafo.add_edge(self.idMap[g[0].upper()],self.idMap[g[1].upper()])


    def vicini(self,n):
        nodo = self.idMap[n.upper()]
        successivi = self.grafo.neighbors(nodo)
        precedenti = self.grafo.predecessors(nodo)
        return successivi,precedenti

    def getDFSNodes(self, source):
        edges = nx.dfs_edges(self.grafo, source)
        visited = []
        for u,v in edges:
            visited.append(v)
        return visited



    def get_num_of_nodes(self):
        return self.grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self.grafo.number_of_edges()




