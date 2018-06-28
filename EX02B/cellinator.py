"""Conversion from row, col => cell index and vice versa."""


def get_cell_index(row, col, row_len):
    """
    Given the row and column indices and the number of columns in the table
    return cell index at the given location.

    :param row: row index
    :param col: column index
    :param row_len: number of columns in the table
    :return: cell index at the given location
    """
    if row_len < col:
        return -1
    index = (row * row_len) + col
    return index


def get_row_and_col(cell_index, row_len):
    """
    Given the cell index and the number of columns in the table
    return tuple with row and col indices of that cell.

    :param cell_index: cell index
    :param row_len: number of columns in the table
    :return: row index, col index as tuple
    """
    row = int(cell_index / row_len)
    col = cell_index - (row * row_len)
    return row, col


def get_row_len(row, col, cell_index):
    """
    Given the row and column indices and the cell index
    return the number of columns in the table.

    If the given setup is not possible
    or it is not possible to deduct column count
    return -1

    :param row: row index
    :param col: column index
    :param cell_index: cell index
    :return: number of columns in the table
    """
    row_len = (cell_index - col) / row
    if row_len.is_integer() and col < row_len:
        return int(row_len)
    else:
        return -1


if __name__ == '__main__':
    print(get_cell_index(0, 0, 5))  # => 0
    print(get_cell_index(1, 3, 5))  # => 8
    print(get_cell_index(1, 1, 5))  # => 6
    print(get_cell_index(3, 1, 5))  # => 16
    print(get_cell_index(4, 2, 5))  # => 22

    print(get_row_and_col(5, 5))  # (1, 0)
    print(get_row_and_col(11, 5))  # (2, 1)
    print(get_row_and_col(3, 5))  # (0, 3)
    print(get_row_and_col(20, 5))  # (4, 0)
    print(get_row_and_col(14, 5))  # (2, 4)

    print(get_row_len(1, 3, 4))  # => -1
    print(get_row_len(1, 0, 3))  # => 3
    print(get_row_len(12, 0, 12))  # => 1
