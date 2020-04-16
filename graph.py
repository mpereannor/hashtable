#adjacency list
class Graph:
  def__init__(self):
    self.vertices= {
      "A": {"B"},
      "B": {"C", "D"},
      "C": {"F", "G"},
      "E": {"C"},
      "F": {"C"},
      "G": {"A", "F"}
    }

#adjacency matrix
class Graph:
  def__init__(self):
    self.edges = [
      [],
      [],
      []
      []
    ]