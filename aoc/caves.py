from .aoc_helpers import distinct_counts
from collections import deque


class CaveNetwork():
    def __init__(self, edge_list):
        self.large_caves = []
        self.small_caves = []
        self.edges = []

        for edge in edge_list:
            vertices = edge.split('-')
            for v in vertices:
                if v.upper() == v and v not in self.large_caves:
                    self.large_caves.append(v)
                if v.upper() != v and v not in self.small_caves:
                    self.small_caves.append(v)
            v0, v1 = vertices[0], vertices[1]
            self.edges.extend([(v0, v1), (v1, v0)])

    def extend_path(self, path, new_vertex):
        new_path = [v for v in path]
        new_path.append(new_vertex)
        return new_path

    def valid_next_small_caves_for_path(self, path, mode='d12s1'):
        if mode == 'd12s1':
            return [v for v in self.small_caves
                    if (path[-1], v) in self.edges
                    and v not in path]
        elif mode == 'd12s2':
            if self.has_repeated_small_cave(path):
                return [v for v in self.small_caves
                        if (path[-1], v) in self.edges
                        and v not in path]
            else:
                # Haven't yet repeated any small cave, so
                # can visit any of them (with an edge)
                # Except: don't repeat start
                # Assumes pathing logic catches first visit to end!
                return [v for v in self.small_caves
                        if (path[-1], v) in self.edges
                        and v != 'start']
        else:
            raise ValueError(f'Unexpected mode {mode}')

    def repeated_small_caves(self, path):
        visit_counts = distinct_counts(path, [v for v in self.small_caves])
        return [v for v in visit_counts if visit_counts[v] > 1]

    def has_repeated_small_cave(self, path):
        return len(self.repeated_small_caves(path)) > 0

    def find_all_extensions(self, path, mode='d12s1'):
        possible_next_small_caves = self.valid_next_small_caves_for_path(path,
                                                                         mode)
        possible_next_large_caves = [v for v in self.large_caves
                                     if (path[-1], v) in self.edges]

        new_paths = [self.extend_path(path, v)
                     for v in possible_next_small_caves]
        new_paths.extend([self.extend_path(path, v)
                          for v in possible_next_large_caves])
        return new_paths

    def find_start_to_end(self, mode='d12s1'):
        incomplete_paths = deque([['start']])
        complete_paths = []
        while len(incomplete_paths) > 0:
            next_candidate = incomplete_paths.pop()
            new_paths = self.find_all_extensions(next_candidate, mode)
            incomplete_paths.extend([p for p in new_paths if p[-1] != 'end'])
            complete_paths.extend([p for p in new_paths if p[-1] == 'end'])
        return complete_paths
