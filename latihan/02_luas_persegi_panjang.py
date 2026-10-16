def luas_persegi_panjang(p, l):
    return p * l

test_cases = [
    ((8, 5), 40),
    ((2.5, 4), 10.0),
    ((0, 7), 0)
]

for item in test_cases:
    p, l = item[0]
    expected = item[1]
    hasil = luas_persegi_panjang(p, l)
    print("luas(", p, ", ", l, ") -> ", hasil, " (Expected: ", expected, ")", sep="")