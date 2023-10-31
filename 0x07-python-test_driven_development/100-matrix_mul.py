#!/usr/bin/python3
"""
Module
"""


def matrix_mul(m_a, m_b):
    """Multiplies.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_e = False
    m_b_e = False
    m_a_nr = False
    m_b_nr = False
    m_a_nm = False
    m_b_nm = False
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        if len(i) != len(m_a[0]):
            m_a_nr = True
        for j in i:
            if not isinstance(j, (int, float)):
                m_a_nm = True

    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
        if len(i) != len(m_b[0]):
            m_b_nr = True
        for j in i:
            if not isinstance(j, (int, float)):
                m_b_nm = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_nm:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_nm:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_nr:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_nr:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r = [[] for l in range(len(m_a))]

    for l in range(len(m_a)):
        for k in range(len(m_b[0])):
            q = 0
            for n in range(len(m_b)):
                q += m_a[l][n] * m_b[n][k]
            r[l].append(q)

    return r

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
