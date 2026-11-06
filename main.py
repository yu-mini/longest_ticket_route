
import sys
def read_graph(lines):    
    graph = {}
    for line in lines:
        line = line.strip().lstrip("\ufeff")
        if not line:
            continue
        s,f,d = line.split(",")
        s,f,d = int(s),int(f),float(d)
        if s not in graph:
            graph[s] = []
        if f not in graph:
            graph[f] = []
        graph[s].append((f,d))
        graph[f].append((s,d))
    return graph

if __name__ == "__main__":
    graph = read_graph(sys.stdin)
    print(graph)
