import queue

def dfs(edges, start_vertex):
    visited = [False for _ in range(len(edges))]
    stack = [start_vertex]
    dfs_vertex = []
    while stack:
        current_vertex = stack.pop()
        if not visited[current_vertex]:
            dfs_vertex.append(current_vertex)
            visited[current_vertex] = True
            for v in sorted(edges[current_vertex], reverse=True):
                if not visited[v]:
                    stack.append(v)
    return dfs_vertex

def bfs(edges, start_vertex):
    visited = [False for _ in edges]
    q = queue.Queue()
    q.put_nowait(start_vertex)

    bfs_vertex = []
    visited[start_vertex] = True

    while not q.empty():
        current_vertex = q.get_nowait()
        bfs_vertex.append(current_vertex)
        for v in sorted(edges[current_vertex]):
            if not visited[v]:
                q.put_nowait(v)
                visited[v] = True

    return bfs_vertex

def print_list(list):
    print(' '.join(map(str, list)))

if __name__ == '__main__':
    N, M, V = map(int, input().split())
    edges = [[] for i in range(N + 1)]

    for i in range(M):
        v1, v2 = map(int, input().split())
        edges[v1].append(v2)
        edges[v2].append(v1)

    print_list(dfs(edges, V))
    print_list(bfs(edges, V))