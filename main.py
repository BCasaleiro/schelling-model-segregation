from random import random, randint
from time import sleep

def print_matrix(m):                                                            #TODO: remove this method
    for i in m:
        print i

def calculate_cumulative_prob(n, p):
    """
    generate_matrix method

    Parameters:
        n (int): dimension of the array
        p (array:float): array of probabilities
    Returns:
        p (array:float): cumulative version of the array inputed
    """
    for i in range(1, n):
        p[i] += p[i - 1]

    return p

def generate_matrix(n):
    """
    generate_matrix method

    Parameters:
        n (int): dimension of the neighborhood
    Returns:
        m (array:array:int): n by n matrix populated with 0's
    """
    return [[0 for i in range(n)] for k in range(n)]

def populate_matrix(m, n, p, e):
    """
    populate_matrix method

    Parameters:
        m (array:array:int): matrix representing the neighborhood
        n (int): number of ethnicities
        p (array:float): array of probabilitie for each ethnicity
        e (int): number of empty spots
    Returns:
        m (array:array:int): populated neighborhood with the individuals of each ethnicity and also e empty spots
    """

    n_m = len(m)
    p = calculate_cumulative_prob(n, p)

    for l in range(n_m):
        for c in range(n_m):
            r = random()
            for et_i, et_p in enumerate(p):
                if r <= et_p:
                    m[l][c] = et_i
                    break

    for i in range(e):
        l = randint(0, len(m) - 1)
        c = randint(0, len(m) - 1)
        if m[l][c] == -1:
            i -= 1
        else:
            m[l][c] = -1

    return m

def is_not_empty_spot(n):
    if n == -1:
        return 0
    else:
        return 1

def is_same_kind(k, n):
    if n == k:
        return 1
    else:
        return 0

def calculate_individual_satisfation(m, l, c):
    n_m = len(m)
    count = 0
    sm = 0
    if l - 1 >= 0:
        count += is_not_empty_spot(m[l - 1][c])
        sm += is_same_kind(m[l - 1][c], m[l][c])

        if c - 1 >= 0:
            count += is_not_empty_spot(m[l - 1][c - 1])
            sm += is_same_kind(m[l - 1][c - 1], m[l][c])
        if c + 1 < n_m:
            count += is_not_empty_spot(m[l - 1][c + 1])
            sm += is_same_kind(m[l - 1][c + 1], m[l][c])
    if l + 1 < n_m:
        count += is_not_empty_spot(m[l + 1][c])
        sm += is_same_kind(m[l + 1][c], m[l][c])

        if c - 1 >= 0:
            count += is_not_empty_spot(m[l + 1][c - 1])
            sm += is_same_kind(m[l + 1][c - 1], m[l][c])
        if c + 1 < n_m:
            count += is_not_empty_spot(m[l + 1][c + 1])
            sm += is_same_kind(m[l + 1][c + 1], m[l][c])
    if c - 1 >= 0:
        count += is_not_empty_spot(m[l][c - 1])
        sm += is_same_kind(m[l][c - 1], m[l][c])
    if c + 1 < n_m:
        count += is_not_empty_spot(m[l][c + 1])
        sm += is_same_kind(m[l][c + 1], m[l][c])

    if count == 0:
        return 1
    else:
        return float(sm)/count

def calculate_satisfation(m, l_s, m_s):
    n_m = len(m)
    s = []
    mean_s = 0
    for l in range(n_m):
        for c in range(n_m):
            if(m[l][c] != -1):
                sat = calculate_individual_satisfation(m, l, c)
                mean_s += sat
                if sat < l_s or sat > m_s:
                    s.append( (l, c) )
    print 'mean satisfaction: {}'.format(float(mean_s) / (n_m * n_m))
    print 'satisfaction: {} {}'.format(len(s), 1 - float(len(s)) / (n_m * n_m))
    return s

def get_empty_spots(m):
    e = []
    n_m = len(m)

    for l in range(n_m):
        for c in range(n_m):
            if m[l][c] == -1:
                e.append( (l,c) )

    return e

def moving(m, s):
    e = get_empty_spots(m)

    for s_i in s:
        r = randint(0, len(e) - 1)
        m[ e[r][0] ][ e[r][1] ] = m[ s_i[0] ][ s_i[1] ]
        m[ s_i[0] ][ s_i[1] ] = -1
        e[r] = (s_i[0], s_i[1])

    return m

def main():
    it = 0

    m = generate_matrix(50)
    m = populate_matrix(m, 2, [0.5, 0.5], 250)

    s = calculate_satisfation(m, 0.7, 1)

    while len(s) > 0:
        m = moving(m, s)
        it += 1
        s = calculate_satisfation(m, 0.7, 1)
        print 'it: {}'.format(it)

if __name__ == '__main__':
    main()
