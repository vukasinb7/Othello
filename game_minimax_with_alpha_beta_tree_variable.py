from state import State
import time
import copy
import Tree
import hashmap
hmp = hashmap.ChainedHashMap(10000)


class Game(object):
    __slots__ = ['_current_state', '_player_turn']

    def __init__(self):
        self._current_state = None
        self._player_turn = 1
        self.initialize_game()

    def initialize_game(self):
        self._current_state = State()
        self._player_turn = 1

    def max_ab(self, alpha, beta, node): #maximizer
        maxv = -9999999999
        px = py = -1
        if node.is_leaf():
            hashed_node = hmp[node.data[0].board]
            if hashed_node == None:
                heuristic = node.data[0].othello_heuristic_evaluation()
                hmp[node.data[0].board] = heuristic

                return heuristic, px, py
            else:
                return hashed_node, px, py

        result, winner = node.data[0].is_end(1)
        if result:
            if winner == 1:
                return -9999999999, -1, -1
            elif winner == 2:
                return +9999999999, -1, -1
            else:
                return 0, -1, -1
        for child in node.children:
            m = self.min_ab(alpha, beta, child)[0]
            if m > maxv:
                maxv = m
                px = child.data[1]
                py = child.data[2]

            if maxv > alpha:
                alpha = maxv
            if alpha >= beta:
                return maxv, px, py
        return maxv, px, py

    def min_ab(self, alpha, beta, node): #minimizer
        qx = qy = -1
        if node.is_leaf():
            hashed_node = hmp[node.data[0].board]
            if hashed_node == None:
                heuristic = node.data[0].othello_heuristic_evaluation()
                hmp[node.data[0].board] = heuristic
                return heuristic, qx, qy
            else:
                return hashed_node, qx, qy

        minv = 9999999999
        result, winner = node.data[0].is_end(2)

        if result:
            if winner == 1:
                return +9999999999, -1, -1
            elif winner == 2:
                return -9999999999, -1, -1
            else:
                return 0, -1, -1

        for child in node.children:
            m = self.max_ab(alpha, beta, child)[0]
            if m < minv:
                minv = m
                qx = child.data[1]
                qy = child.data[2]
            if minv < beta:
                beta = minv
            if alpha >= beta:
                return minv, qx, qy
        return minv, qx, qy

    def create_tree(self, node, depth, player):  # pravljenje stabla odredjene dubine
        if depth == 0:  # ukoliko je dostignuta zeljena dubina ne pretrazuje se dalje stablo
            return
        else:
            for i in range(8):
                for j in range(8):
                    if node.data[0].is_move_valid(i, j,
                                                  player):  # ukoliko je potez na trenutnom stanju validan pravi se novo dete cvora
                        board_copy = copy.deepcopy(node.data[0])
                        board_copy.change_state(i, j, player)
                        child = Tree.TreeNode([board_copy, i, j])
                        node.add_child(child)
            opp_player = 1
            if player == 1:
                opp_player = 2
            for child in node.children:
                self.create_tree(child, depth - 1, opp_player)

    def play(self):
        while True:
            print(self._current_state)
            result, winner = self._current_state.is_end(self._player_turn)  # provera kraja igre
            if result:
                if winner == 1:
                    print('The winner is Black!')
                elif winner == 2:
                    print('The winner is White!')
                else:
                    print("It's a tie!")

                self.initialize_game()
                return

            if self._player_turn == 1:  # igracev potez
                row_value = ["A", "B", "C", "D", "E", "F", "G", "H"]
                column_value = ["1", "2", "3", "4", "5", "6", "7", "8"]
                list_free_moves = self._current_state.list_valid_moves(1)
                s = "Available moves:"
                for i in range(len(list_free_moves)):
                    s += row_value[list_free_moves[i][0]] + column_value[list_free_moves[i][1]] + ", "
                print(s[0:-2])
                while True:
                    field = input("Insert field name(ex. A4):")
                    if len(field) == 2:
                        if field[0].capitalize() in row_value and field[1] in column_value:
                            px = row_value.index(field[0].capitalize())
                            py = eval(field[1]) - 1
                            if self._current_state.is_move_valid(px, py, 1):
                                self._current_state.change_state(px, py, 1)
                                self._player_turn = 2
                                break
                            else:
                                print('The move is not valid! Try again.')
                        else:
                            print('The move is not valid! Try again.')
                    else:
                        print('The move is not valid! Try again.')

            else:  # potez ai-ja
                start = time.time()
                root_node = Tree.Tree(Tree.TreeNode([self._current_state, 0, 0]))
                num_valid_moves = len(self._current_state.list_valid_moves(2))
                if num_valid_moves < 4:
                    depth = 5
                elif 4 <= num_valid_moves <= 8:
                    depth = 4
                else:
                    depth = 3
                self.create_tree(root_node.root, depth, 2)
                x = y = None
                maxv = -99999999999999
                for child in root_node.root.children:
                    temp = self.max_ab(-99999999999, 99999999999, child)[0]
                    if temp > maxv:
                        maxv = temp
                        x = child.data[1]
                        y = child.data[2]

                self._current_state.change_state(x, y, 2)
                end = time.time()
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                self._player_turn = 1
