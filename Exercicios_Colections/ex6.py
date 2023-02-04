'''
ZIP
'''

p1 = [80, 91, 78]
p2 = [98, 89, 53]
alunos = ['ze', 'lira', 'maria']

final = zip(alunos, map(lambda nota : max(nota), zip(p1, p2)))
print(dict(final))
