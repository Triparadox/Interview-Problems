def solution():
    grid = [
        [6, 2, 8, 9, 5, 4, 3, 1, 7],
        [3, 4, 9, 1, 2, 7, 6, 5, 8],
        [7, 1, 5, 8, 3, 6, 9, 4, 2],
        [8, 6, 3, 2, 7, 5, 1, 9, 4],
        [5, 9, 2, 4, 1, 8, 7, 6, 3],
        [4, 7, 1, 6, 9, 3, 8, 2, 5],
        [2, 3, 6, 5, 8, 9, 4, 7, 1],
        [1, 8, 4, 7, 6, 2, 5, 3, 9],
        [9, 5, 7, 3, 4, 1, 2, 8, 6]
    ]

    number = set()
    status = True

    # Test for sub matrix
    for offset_y in range(0, 9, 3):
        for offset_x in range(0, 9, 3):
            for y in range(0, 3):
                for x in range(0, 3):
                    number.add(grid[y+offset_y][x+offset_x])
            if len(number) == 9:
                pass
            else:
                status = False
            number.clear()

    # Test for global horizontal matrix
    for y in range(0, 9):
        for x in range(0, 9):
            number.add(grid[y][x])
        if len(number) == 9:
            pass
        else:
            status = False
        number.clear()

    # Test for global vertical matrix
    for x in range(0, 9):
        for y in range(0, 9):
            number.add(grid[y][x])
        if len(number) == 9:
            pass
        else:
            status = False
        number.clear()

    print(status)


solution()