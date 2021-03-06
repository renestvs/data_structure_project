__author__ = 'rene_'

from django.test import TestCase

from data_structure.second_bim import graphs, pattern_searching, dynamic_programing


class Second_Bim_Test(TestCase):
# ==============================================
# ================= patterns ===================
# ==============================================
    def pattern_test(self):
        c = pattern_searching

        text = "GEEK FOR GEEKS"
        word = "EEKS"
        q = 101  # A prime number
        c.kr(text, word, q)

        text = c.convert_string("abacaabaccabacabaabb")
        word = c.convert_string("abacab")
        self.assertEqual(c.kmp(text, word), 19)
        self.assertEqual(c.bm(text, word), 16)
        self.assertEqual(c.brute_force(text, word), 23)

        text = c.convert_string("HERE IS A SIMPLE EXAMPLE")
        word = c.convert_string("EXAMPLE")
        self.assertEqual(c.kmp(text, word), 27)
        self.assertEqual(c.bm(text, word), 16)
        self.assertEqual(c.brute_force(text, word), 17)

        text = c.convert_string("Faturei com folga na prova de complexidade de algoritmos")
        word = c.convert_string("algo")
        self.assertEqual(c.kmp(text, word), 55)
        self.assertEqual(c.bm(text, word), 19)
        self.assertEqual(c.brute_force(text, word), 50)

        text = c.convert_string("esta prova e mais longa que complicada")
        word = c.convert_string("cada")
        self.assertEqual(c.kmp(text, word), 39)
        self.assertEqual(c.bm(text, word), 18)
        self.assertEqual(c.brute_force(text, word), 34)

        text = c.convert_string("A jabuticaba acabou de acabar")
        word = c.convert_string("cabar")
        self.assertEqual(c.kmp(text, word), 31)
        self.assertEqual(c.bm(text, word), 13)
        self.assertEqual(c.brute_force(text, word), 29)

        text = c.convert_string("vi na mata uma arara e duas aranhas")
        word = c.convert_string("araras")
        self.assertEqual(c.kmp(text, word), 46)
        self.assertEqual(c.bm(text, word), 9)
        self.assertEqual(c.brute_force(text, word), 37)

        text = c.convert_string("a pattern matching algorithm")
        word = c.convert_string("rithm")
        self.assertEqual(c.kmp(text, word), 29)
        self.assertEqual(c.bm(text, word), 12)
        self.assertEqual(c.brute_force(text, word), 23)

    # ==============================================
    # =================== DFS ======================
    # ==============================================
    def dfs_test(self):

        graph = {'A': set(['B', 'C']),
                 'B': set(['A', 'D', 'E']),
                 'C': set(['A', 'F']),
                 'D': set(['B']),
                 'E': set(['B', 'F']),
                 'F': set(['C', 'E'])}

        graph.__setattr__("name")
        c = graphs
        self.assertEqual(c.dfs(graph, 'A'), {'E', 'C', 'D', 'B', 'A', 'F'})
        self.assertEqual(c.dfs_recursive(graph, 'A'), {'B', 'E', 'D', 'C', 'F', 'A'})
        self.assertEqual(list(c.dfs_paths(graph, 'A', 'F')), [['A', 'C', 'F'], ['A', 'B', 'E', 'F']])
        self.assertEqual(list(c.dfs_paths_recursive(graph, 'C', 'F')), [['C', 'F'], ['C', 'A', 'B', 'E', 'F']])

    # ==============================================
    # =================== BFS ======================
    # ==============================================
    def bfs_test(self):
        graph = {'A': set(['B', 'C']),
                 'B': set(['A', 'D', 'E']),
                 'C': set(['A', 'F']),
                 'D': set(['B']),
                 'E': set(['B', 'F']),
                 'F': set(['C', 'E'])}

        c = graphs
        self.assertEqual(c.bfs(graph, 'A'), {'B', 'C', 'A', 'F', 'D', 'E'})
        self.assertEqual(list(c.bfs_paths(graph, 'A', 'F')), [['A', 'C', 'F'], ['A', 'B', 'E', 'F']])
        self.assertEqual(c.shortest_path(graph, 'A', 'F'), ['A', 'C', 'F'])

    # ==============================================
    # ================= Tarjan =====================
    # ==============================================
    def tarjan_main_test(self):
        self.tarjan_cycles_test()

        self.tarjan_edges_class_test()

        self.tarjan_topological_sort_test()

        self.tarjan_coloring_test()

        self.tarjan_scc_test()

        self.tarjan_cut_edge_test()

        self.tarjan_cut_vertex_test()  # TODO refactor

    def tarjan_cut_vertex_test(self):
        c = graphs
        graph = [set([1, 3, 5]),  # 0 - A,
                 set([0, 2, 3]),  # 1 - B,
                 set([1, 3, 4, 5, 7]),  # 2 - C,
                 set([0, 1, 2]),  # 3 - D,
                 set([2]),  # 4 - E,
                 set([0, 2, 7]),  # 5 - F,
                 set([7]),  # 6 - G,
                 set([2, 5, 6])  # 7 - H
                 ]
        # c.tarjan_cut_vertex(graph, 0) #TODO refactor

    def tarjan_cut_edge_test(self):
        c = graphs
        graph = [set([1, 3, 5]),  # 0 - A,
                 set([0, 2, 3]),  # 1 - B,
                 set([1, 3, 4, 5, 7]),  # 2 - C,
                 set([0, 1, 2]),  # 3 - D,
                 set([2]),  # 4 - E,
                 set([0, 2, 7]),  # 5 - F,
                 set([7]),  # 6 - G,
                 set([2, 5, 6])  # 7 - H
                 ]
        self.assertEqual(c.tarjan_cut_edge(graph, 0), {(7, 6): 'cut_edge', (2, 4): 'cut_edge'})

    def tarjan_scc_test(self):
        c = graphs
        graph = [[1, 4, 5],  # A - 0,
                 [2],  # B - 1,
                 [5, 7],  # C - 2,
                 [2, 4, 6],  # D - 3,
                 [2],  # E - 4,
                 [1],  # F - 5,
                 [3],  # G - 6,
                 [],  # H - 7
                 ]
        self.assertEqual(c.tarjan_scc(graph), [1, 2, 2, 7, 6, 2, 7, 5])

    def tarjan_coloring_test(self):
        c = graphs
        graph = [set([1, 2, 5, 6]),  # 0,
                 set([0, 3]),  # 1,
                 set([0]),  # 2,
                 set([1, 5]),  # 3,
                 set([5, 6]),  # 4,
                 set([0, 4]),  # 5,
                 set([0, 4, 7]),  # 6,
                 set([6, 8]),  # 7
                 set([7, 10]),  # 8
                 set([10, 11]),  # 9
                 set([8, 9, 12]),  # 10
                 set([9, 12]),  # 11
                 set([11, 10]),  # 12
                 ]
        self.assertEqual(c.tarjan_coloring(graph), 1)

    def tarjan_topological_sort_test(self):
        c = graphs
        graph = [[],  # 0,
                 [10],  # 1,
                 [5, 7, 8],  # 2,
                 [],  # 3,
                 [7],  # 4,
                 [1, 10, 11],  # 5,
                 [],  # 6,
                 [0, 3],  # 7
                 [1, 5, 6],  # 8
                 [8],  # 9
                 [],  # 10
                 [3]  # 11
                 ]
        self.assertEqual(c.tarjan_topological_sort(graph), [9, 4, 2, 8, 6, 7, 5, 11, 3, 1, 10, 0])

    def tarjan_edges_class_test(self):
        c = graphs
        graph = [[1, 4, 5],  # A,
                 [2],  # B,
                 [5, 7],  # C,
                 [2, 4, 6],  # D,
                 [2],  # E,
                 [1],  # F,
                 [3],  # G,
                 []  # H
                 ]
        self.assertEqual(c.tarjan_edges(graph),
                         {(0, 1): 'tree', (1, 2): 'tree', (3, 2): 'cross', (2, 7): 'tree', (4, 2): 'cross',
                          (6, 3): 'back', (0, 5): 'forward', (3, 6): 'tree', (0, 4): 'tree', (5, 1): 'back',
                          (2, 5): 'tree', (3, 4): 'cross'})

    def tarjan_cycles_test(self):
        c = graphs
        graph = [[1],
                 [4, 6, 7],
                 [4, 6, 7],
                 [4, 6, 7],
                 [2, 3],
                 [2, 3],
                 [5, 8],
                 [5, 8],
                 [],
                 []]
        c.tarjan_cycles(graph)

    # ==============================================
    # ================= Dijkstra ===================
    # ==============================================
    def dijkstra_test(self):
        graph = {'A': {'B': 10, 'D': 4, 'F': 10},
                 'B': {'E': 5, 'J': 10, 'I': 17},
                 'C': {'A': 4, 'D': 10, 'E': 16},
                 'D': {'F': 12, 'G': 21},
                 'E': {'G': 4},
                 'F': {'H': 3},
                 'G': {'J': 3},
                 'H': {'G': 3, 'J': 5},
                 'I': {},
                 'J': {'I': 8}}

        c = graphs
        # print(c.dijkstra(graph, 'C', 'I'))

        graph = {'A': {'B': 2, 'J': 7},
                 'B': {'C': 10, 'J': 3, 'K': 8},
                 'C': {'K': 4, 'M': 11},
                 'D': {'C': 9},
                 'J': {'K': 4},
                 'K': {'R': 6},
                 'M': {'D': 19, 'N': 11, 'S': 9},
                 'N': {'D': 7, 'S': 8, 'T': 6},
                 'P': {'J': 8, 'R': 6, 'X': 9},
                 'R': {'P': 6, 'S': 4, 'X': 10},
                 'S': {'X': 7},
                 'T': {'S': 4, 'Y': 4},
                 'X': {'Y': 3},
                 'Y': {'T': 3}}

        print(c.dijkstra(graph, 'A', 'X'))


# ==============================================
# ================= Dynamic Prog. ==============
# ==============================================

    def lcs_text(self):
        c = dynamic_programing
        self.assertEqual(c.lcs("HUMAN", "CHIMPANZEE"), ['H', 'M', 'A', 'N'])

# ==============================================
# ================= memoizatoin ================
# ==============================================

    def fibonacci_test(self):
        c = dynamic_programing
        self.assertEqual(c.fibonacci(10), 55)

    def knapsack_memoization_test(self):
        c = dynamic_programing
        items = [(7, 1), (7, 2), (2, 3), (3, 4)]
        print(c.knapsack(items, 11))

    def lcs_memoization_test(self):
        c = dynamic_programing
        self.assertEqual(c.lcs("HUMAN", "CHIMPANZEE"), ['H', 'M', 'A', 'N'])


    def make_change_memoization_test(self):
        c = dynamic_programing
        # self.assertEqual(c.make_change_memoization(100, (50,25,10,5,1)), ['H', 'M', 'A', 'N'])
        print(c.make_change_memoization(15, (1,5,10,25)))