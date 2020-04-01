graph = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Bucharest": {"Fagaras": 211, "Urziceni": 85, "Giurgiu": 90, "Pitesti": 101},
    "Craiova": {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Dobreta": {"Mehadia": 75, "Craiova": 120},
    "Eforie": {"Hirsova": 86},
    "Fagaras": {"Bucharest": 211, "Sibiu": 99},
    "Giurgiu": {"Bucharest": 90},
    "Hirsova": {"Eforie": 86},
    "Iasi": {"Neamt": 87, "Vaslui": 92},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Dobreta": 75, "Lugoj": 70},
    "Neamt": {"Iasi": 87},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Pitesti": {"Rimnicu Vilcea": 97, "Bucharest": 101},
    "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97},
    "Sibiu": {"Fagaras": 99, "Oradea": 151, "Arad": 140, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Urziceni": {"Hirsova": 98, "Bucharest": 85},
    "Vaslui": {"Iasi": 92, "Urziceni": 142},
    "Zerind": {"Oradea": 71, "Arad": 75}
}

heuristics = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 178,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 98,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}

"""
Best First Search Greedy algorithm

Returns:
    [str] -- List with the path from [start] to [end]
"""


def bfs_shortest_path(graph, start, end):
    explored = []
    queue = [[start]]

    if start == end:
        return []

    while queue:
        path = queue.pop()
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == end:
                    return new_path

            explored.append(node)

    return []


if __name__ == "__main__":
    results = bfs_shortest_path(graph, 'Zerind', 'Bucharest')
    print(results)
