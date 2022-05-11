def bot_saves_princess(grid, n):

    # getting index of bot and princess
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 'p':
                p_index = [x, y]
            elif grid[x][y] == 'b':
                m_index = [x, y]

    # getting to the position of princess
    path = []
    # princess -> top-left
    if p_index == [0, 0]:
        while m_index[0] != p_index[0]:
            m_index[0] -= 1
            path.append("left")
        while m_index[1] != p_index[1]:
            m_index[1] += 1
            path.append("top")

    # princess -> bottom-right
    elif p_index == [0, n-1]:
        while m_index[0] != p_index[0]:
            m_index[0] += 1
            path.append("right")
        while m_index[1] != p_index[1]:
            m_index[1] -= 1
            path.append("bottom")

    # princess -> top-right
    elif p_index == [n-1, 0]:
        while m_index[0] != p_index[0]:
            m_index[0] += 1
            path.append("right")
        while m_index[1] != p_index[1]:
            m_index[1] += 1
            path.append("top")

    # princess -> bottom-left
    else:
        while m_index[0] != p_index[0]:
            m_index[0] -= 1
            path.append("left")
        while m_index[1] != p_index[1]:
            m_index[1] -= 1
            path.append("bottom")

    return path
