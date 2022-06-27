class State(object):

    def __init__(self):
        self._board = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 2, 1, 0, 0, 0],
                       [0, 0, 0, 1, 2, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]

    @property
    def board(self):
        return self._board

    def get_value(self, i, j):
        return self._board[i][j]

    def set_value(self, i, j, value):
        self._board[i][j] = value

    def list_valid_moves(self, value): #vraca listu validnih poteza
        valid_moves = []
        for i in range(8):
            for j in range(8):
                if self.is_move_valid(i, j, value):
                    valid_moves.append([i, j])

        return valid_moves

    def is_move_valid(self, i, j, value): #proverava validnost poteza
        if not 0 <= i <= 7 or not 0 <= j <= 7:
            return False

        if self._board[i][j] != 0:
            return False

        k = i + 1
        while k <= 7:
            if self._board[k][j] == 0:
                break
            elif self._board[k][j] == value:
                if k == i + 1:
                    break
                else:
                    return True
            k += 1
        k = i - 1
        while k >= 0:
            if self._board[k][j] == 0:
                break
            elif self._board[k][j] == value:
                if k == i - 1:
                    break
                else:
                    return True
            k -= 1
        m = j + 1
        while m <= 7:
            if self._board[i][m] == 0:
                break
            elif self._board[i][m] == value:
                if m == j + 1:
                    break
                else:
                    return True
            m += 1
        m = j - 1
        while m >= 0:
            if self._board[i][m] == 0:
                break
            elif self._board[i][m] == value:
                if m == j - 1:
                    break
                else:
                    return True
            m -= 1
        k = i + 1
        m = j + 1
        while m <= 7 and k <= 7:
            if self._board[k][m] == 0:
                break
            elif self._board[k][m] == value:
                if k == i + 1:
                    break
                else:
                    return True
            m += 1
            k += 1
        k = i - 1
        m = j - 1
        while m >= 0 and k >= 0:
            if self._board[k][m] == 0:
                break
            elif self._board[k][m] == value:
                if k == i - 1:
                    break
                else:
                    return True
            m -= 1
            k -= 1
        k = i + 1
        m = j - 1
        while m >= 0 and k <= 7:
            if self._board[k][m] == 0:
                break
            elif self._board[k][m] == value:
                if k == i + 1:
                    break
                else:
                    return True
            m -= 1
            k += 1
        k = i - 1
        m = j + 1
        while k >= 0 and m <= 7:
            if self._board[k][m] == 0:
                break
            elif self._board[k][m] == value:
                if k == i - 1:
                    break
                else:
                    return True
            m += 1
            k -= 1
        return False

    def change_state(self, i, j, value): #promena stanja plocica na tabeli prilikom odigravanja poteza
        change_list = []
        k = i + 1
        temp_list = []
        while k <= 7:
            if self._board[k][j] == 0:
                break
            elif self._board[k][j] == value:
                if k == i + 1:
                    break
                else:
                    change_list = change_list + temp_list
                    break
            temp_list.append([k, j])
            k += 1
        k = i - 1
        temp_list = []
        while k >= 0:
            if self._board[k][j] == 0:
                break
            elif self._board[k][j] == value:
                if k == i - 1:
                    break
                else:
                    change_list = change_list + temp_list
                    break
            temp_list.append([k, j])
            k -= 1

        m = j + 1
        temp_list = []
        while m <= 7:
            if self._board[i][m] == 0:
                break
            elif self._board[i][m] == value:
                if m == j + 1:
                    break
                else:
                    change_list = change_list + temp_list
                    break
            temp_list.append([i, m])
            m += 1
        m = j - 1
        temp_list = []
        while m >= 0:
            if self._board[i][m] == 0:
                break
            elif self._board[i][m] == value:
                if m == j - 1:
                    break
                else:
                    change_list = change_list + temp_list
                    break
            temp_list.append([i, m])
            m -= 1
        k = i + 1
        m = j + 1
        temp_list = []
        while m <= 7 and k <= 7:
            if self._board[k][m] == 0:
                break
            elif self._board[k][m] == value:
                if k == i + 1:
                    break
                else:
                    change_list = change_list + temp_list
                    break
            temp_list.append([k, m])
            m += 1
            k += 1
        k = i - 1
        m = j - 1
        temp_list = []
        while m >= 0 and k >= 0:
            if self._board[k][m] == 0:
                break
            elif self._board[k][m] == value:
                if k == i - 1:
                    break
                else:
                    change_list = change_list + temp_list
                    break
            temp_list.append([k, m])
            m -= 1
            k -= 1
        k = i + 1
        m = j - 1
        temp_list = []
        while m >= 0 and k <= 7:
            if self._board[k][m] == 0:
                break
            elif self._board[k][m] == value:
                if k == i + 1:
                    break
                else:
                    change_list = change_list + temp_list
                    break
            temp_list.append([k, m])
            m -= 1
            k += 1
        k = i - 1
        m = j + 1
        temp_list = []
        while k >= 0 and m <= 7:
            if self._board[k][m] == 0:
                break
            elif self._board[k][m] == value:
                if k == i - 1:
                    break
                else:
                    change_list = change_list + temp_list
                    break
            temp_list.append([k, m])
            m += 1
            k -= 1

        for l in change_list:
            self._board[l[0]][l[1]] = value
        self._board[i][j] = value

    def is_end(self, value): #provera kraja igre i vracanje pobednika
        W = 0
        B = 0
        for i in range(8):
            for j in range(8):
                if self.is_move_valid(i, j, value):
                    return False, None
                elif self._board[i][j] == 1:
                    W += 1
                elif self._board[i][j] == 2:
                    B += 1
        if B > W:
            return True, 2
        elif B < W:
            return True, 1
        else:
            return True, 3

    def othello_heuristic_evaluation(self): #heuristika
        my_color = 1
        opp_color = 2
        my_tiles = 0
        opp_tiles = 0
        my_front_tiles = 0
        opp_front_tiles = 0
        p = c = l = f = m = d = 0
        X1 = [-1, -1, 0, 1, 1, 1, 0, -1]
        Y1 = [0, 1, 1, 1, 0, -1, -1, -1]

        V = [[20, -3, 11, 8, 8, 11, -3, 20], [-3, -7, -4, 1, 1, -4, -7, -3], [11, -4, 2, 2, 2, 2, -4, 11],
             [8, 1, 2, -3, -3, 2, 1, 8],
             [8, 1, 2, -3, -3, 2, 1, 8], [11, -4, 2, 2, 2, 2, -4, 11], [-3, -7, -4, 1, 1, -4, -7, -3],
             [20, -3, 11, 8, 8, 11, -3, 20]]

        for i in range(0, 8):
            for j in range(0, 8):
                if self._board[i][j] == my_color:
                    d += V[i][j]
                    my_tiles += 1
                elif self._board[i][j] == opp_color:
                    d -= V[i][j]
                    opp_tiles += 1
                if self._board[i][j] != 0:
                    for k in range(0, 8):
                        x = i + X1[k]
                        y = j + Y1[k]
                        if 0 <= x < 8 and 0 <= y < 8 and self._board[x][y] == 0:
                            if self._board[i][j] == my_color:
                                my_front_tiles += 1
                            else:
                                opp_front_tiles += 1
                            break

        if my_tiles > opp_tiles:
            p = (100.0 * my_tiles) / (my_tiles + opp_tiles)
        elif my_tiles < opp_tiles:
            p = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
        else:
            p = 0
        if my_front_tiles > opp_front_tiles:
            f = -(100.0 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
        elif my_front_tiles < opp_front_tiles:
            f = (100.0 * opp_front_tiles) / (my_front_tiles + opp_front_tiles)
        else:
            f = 0

        my_tiles = opp_tiles = 0
        if self._board[0][0] == my_color:
            my_tiles += 1
        elif self._board[0][0] == opp_color:
            opp_tiles += 1
        if self._board[0][7] == my_color:
            my_tiles += 1
        elif self._board[0][7] == opp_color:
            opp_tiles += 1
        if self._board[7][0] == my_color:
            my_tiles += 1
        elif self._board[7][0] == opp_color:
            opp_tiles += 1
        if self._board[7][7] == my_color:
            my_tiles += 1
        elif self._board[7][7] == opp_color:
            opp_tiles += 1
        c = 25 * (my_tiles - opp_tiles)

        my_tiles = opp_tiles = 0
        if self._board[0][0] == 0:
            if self._board[0][1] == my_color:
                my_tiles += 1
            elif self._board[0][1] == opp_color:
                opp_tiles += 1
            if self._board[1][1] == my_color:
                my_tiles += 1
            elif self._board[1][1] == opp_color:
                opp_tiles += 1
            if self._board[1][0] == my_color:
                my_tiles += 1
            elif self._board[1][0] == opp_color:
                opp_tiles += 1

        if self._board[0][7] == 0:
            if self._board[0][6] == my_color:
                my_tiles += 1
            elif self._board[0][6] == opp_color:
                opp_tiles += 1
            if self._board[1][6] == my_color:
                my_tiles += 1
            elif self._board[1][6] == opp_color:
                opp_tiles += 1
            if self._board[1][7] == my_color:
                my_tiles += 1
            elif self._board[1][7] == opp_color:
                opp_tiles += 1

        if self._board[7][0] == 0:
            if self._board[7][1] == my_color:
                my_tiles += 1
            elif self._board[7][1] == opp_color:
                opp_tiles += 1
            if self._board[6][1] == my_color:
                my_tiles += 1
            elif self._board[6][1] == opp_color:
                opp_tiles += 1
            if self._board[6][0] == my_color:
                my_tiles += 1
            elif self._board[6][0] == opp_color:
                opp_tiles += 1

        if self._board[7][7] == 0:
            if self._board[6][7] == my_color:
                my_tiles += 1
            elif self._board[6][7] == opp_color:
                opp_tiles += 1
            if self._board[6][6] == my_color:
                my_tiles += 1
            elif self._board[6][6] == opp_color:
                opp_tiles += 1
            if self._board[7][6] == my_color:
                my_tiles += 1
            elif self._board[7][6] == opp_color:
                opp_tiles += 1

        l = -12.5 * (my_tiles - opp_tiles)
        my_tiles = len(self.list_valid_moves(my_color))
        opp_tiles = len(self.list_valid_moves(opp_color))

        if my_tiles > opp_tiles:
            m = (100.0 * my_tiles) / (my_tiles + opp_tiles)
        elif my_tiles < opp_tiles:
            m = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
        else:
            m = 0
        score = (10 * p) + (801.724 * c) + (382.026 * l) + (78.922 * m) + (74.396 * f) + (10 * d)
        return score

    def __str__(self): #pretvaranje objekta klase state u string tj u tabelu
        ret = "\n"
        column_value = "     1   2   3   4   5   6   7   8  "
        row_value = ["A", "B", "C", "D", "E", "F", "G", "H"]
        row_split = "   +---+---+---+---+---+---+---+---+"
        white = " ● "
        black = " ⭘ "
        ret += column_value + "\n"
        ret += row_split + "\n"
        for i in range(8):
            current_row = " " + row_value[i] + " |"
            for j in range(8):
                if self._board[i][j] == 0:
                    current_row += "   |"
                elif self._board[i][j] == 1:
                    current_row += white + "|"
                else:
                    current_row += black + "|"
            ret += current_row + "\n" + row_split + "\n"
        return ret
