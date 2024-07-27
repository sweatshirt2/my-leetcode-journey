def isValidSudoku(self, board: list[list[str]]) -> bool:
    cols = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
    cubes = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
    for i in range(9):
        row = set()
        for j in range(9):
            current = board[i][j]
            if current != '.' and current in row and current in cols[j]:
                return False
            if i < 3 and j < 3:
                if current in cubes[1]:
                    return False
                cubes[1].add(current)
            if i < 3 and j > 2 and j < 6:
                if current in cubes[2]:
                    return False
                cubes[2].add(current)
            if i < 3 and j > 5:
                if current in cubes[3]:
                    return False
                cubes[3].add(current)

            if i > 2 and i < 6 and j < 3:
                if current in cubes[1]:
                    return False
                cubes[1].add(current)
            if i > 2 and i < 6 and j > 2 and j < 6:
                if current in cubes[2]:
                    return False
                cubes[2].add(current)
            if i > 2 and i < 6 and j > 5:
                if current in cubes[3]:
                    return False
                cubes[3].add(current)

            if i > 5 and j < 3:
                if current in cubes[1]:
                    return False
                cubes[1].add(current)
            if i > 5 and j > 2 and j < 6:
                if current in cubes[2]:
                    return False
                cubes[2].add(current)
            if i > 5 and j > 5:
                if current in cubes[3]:
                    return False
                cubes[3].add(current)
            row.add(current)
            cols[j].add(current)
    return False