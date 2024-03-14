def tup(tx):
    if not any(tx) or all(tx):
        return False
    return True
tx = (0, [1, 2, 3], (4, 5, 6), 7.0, 'knjbihuvgfc')
print(tup(tx))