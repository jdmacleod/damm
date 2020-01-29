'''Damm algorithm decimal check digit
For reference see http://en.wikipedia.org/wiki/Damm_algorithm
'''
# we use the matrix given in the WP article because it's a good one
matrix = (
            (0, 3, 1, 7, 5, 9, 8, 6, 4, 2),
            (7, 0, 9, 2, 1, 5, 4, 8, 6, 3),
            (4, 2, 0, 6, 8, 7, 1, 3, 5, 9),
            (1, 7, 5, 0, 9, 8, 3, 4, 2, 6),
            (6, 1, 2, 3, 0, 4, 5, 9, 7, 8),
            (3, 6, 7, 4, 2, 0, 9, 5, 8, 1),
            (5, 8, 6, 9, 7, 2, 0, 1, 3, 4),
            (8, 9, 4, 5, 3, 6, 2, 0, 1, 7),
            (9, 4, 3, 8, 6, 1, 7, 2, 0, 5),
            (2, 5, 8, 1, 4, 3, 6, 7, 9, 0)
            )


def encode(number):
    number = str(number)
    interim = 0
    for digit in number:
        interim = matrix[interim][int(digit)]

    return interim

def check(number):
    return encode(number) == 0

if __name__ == '__main__':
    # quick sanity checking
    assert encode(572) == 4 # from wikipedia
    assert check(5724)
    assert encode('43881234567') == 9 # hand-computed
    print("self-test ok")

