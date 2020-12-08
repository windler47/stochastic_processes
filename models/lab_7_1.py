# Однородная цепь Марковас 3-мя состояниями

from numpy import array, nditer, linalg, eye, ndarray, zeros


def part_1(markov_matrix, deviation=0.00001):
    def print_row(iteration, matrix, dev):
        print('{} \t|\t {} \t|\t {}'.format(iteration, matrix, dev))

    n = 1
    prev_step = markov_matrix
    print_row(n, prev_step, 0)

    n = 2
    current_step = markov_matrix @ markov_matrix
    step_diff = abs_diff(prev_step, current_step)
    print_row(n, current_step, step_diff)

    while step_diff >= deviation:
        n += 1
        prev_step = current_step
        current_step = current_step @ markov_matrix
        step_diff = abs_diff(prev_step, current_step)
        print_row(n, current_step, step_diff)





def part_2(markov_matrix: array):
    rows, columns = markov_matrix.shape
    identity_matrix = eye(rows)

    free_column = zeros(rows, 1)
