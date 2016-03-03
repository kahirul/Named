import string
from nltk.util import ngrams
from sys import argv

test_name = argv[1]

raw = open('names.pair', 'r').read().split('\n')
raw = filter(string.strip, raw)

def mapper(pair):
  name, gender = pair.strip().split('@')
  return [name.strip(), gender.strip()]

names = map(mapper, raw)

bi = dict()

for pair in names:
  name, gender = pair
  two_grams = ngrams(name, 3)
  two_grams = list(two_grams)
  for two in two_grams[:-1]:
    bi.setdefault(two, dict(m=0, f=0))
    bi[two][gender] += 1
  bi.setdefault(two_grams[-1], dict(m=0, f=0))
  bi[two_grams[-1]][gender] += 2



# Test
t_bi = bi
m_total = 0
f_total = 0

t_names = map(string.strip, test_name.split(' '))
for t_name in t_names:
  two_grams = ngrams(t_name, 3)
  for two in two_grams:
    t_bi.setdefault(two, dict(m=0, f=0))
    m_total += t_bi[two]['m']
    f_total += t_bi[two]['f']

print test_name

if f_total > m_total:
  print 'female'
else:
  print 'male'

print f_total, m_total

