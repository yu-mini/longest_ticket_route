
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


def find_longest_route(graph):
    best_path = []
    best_distance = -1.0
    def dfs(current,start,visited,path,distance):
        nonlocal best_distance,best_path
        if distance > best_distance:
            best_distance = distance
            best_path = path[:]

        for next_station, d in graph[current]:
            if next_station == start and len(path) >= 3:
                if distance + d > best_distance:
                    best_distance = distance + d
                    best_path = path + [start]
            elif next_station not in visited:
                visited.add(next_station)
                path.append(next_station)
                dfs(next_station,start,visited,path,distance + d)                    
                path.pop()
                visited.remove(next_station)
    for start in graph:
        dfs(start, start, {start}, [start],0.0)
    return best_path
if __name__ == "__main__":
    graph = read_graph(sys.stdin)
    route = find_longest_route(graph)
    for station in route:
        sys.stdout.write(str(station) + "\r\n")
