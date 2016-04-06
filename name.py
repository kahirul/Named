import string
from nltk.util import ngrams
from sys import argv

input_file = argv[1]
output_file = argv[2]

raw = open('names.pair', 'r').read().split('\n')
raw = filter(string.strip, raw)

def mapper(pair):
  name, gender = pair.strip().split('@')
  return [name.strip().lower(), gender.strip().lower()]

names = map(mapper, raw)

bi = dict()

for pair in names:
  name, gender = pair
  tri_grams = ngrams(name, 3)
  tri_grams = list(tri_grams)

  if len(tri_grams) > 0:
    for two in tri_grams[:-1]:
      bi.setdefault(two, dict(m=0, f=0))
      bi[two][gender] += 1
    bi.setdefault(tri_grams[-1], dict(m=0, f=0))
    bi[tri_grams[-1]][gender] += 2


out_file = open(output_file, 'w')
out_file.write('Tested_Name, Predicted_Gender, Female_Score, Male_Score, Percentage\n')

test_names = open(input_file, 'r').read().split('\n')
test_names = filter(string.strip, test_names)

for test_name in test_names:
  t_names = map(string.strip, test_name.split())
  t_names = map(string.lower, t_names)

  t_bi = bi
  m_total = 0
  f_total = 0
  t_gender = '?'
  percentage = 0.0
  all_total = 0

  for t_name in t_names:
    two_grams = ngrams(t_name, 3)
    for two in two_grams:
      t_bi.setdefault(two, dict(m=0, f=0))
      m_total += t_bi[two]['m']
      f_total += t_bi[two]['f']

  all_total = float(f_total + m_total)

  if f_total > m_total:
    t_gender = 'f'
    percentage = f_total / all_total

  elif m_total > f_total:
    t_gender = 'm'
    percentage = m_total / all_total

  out_file.write("'" + test_name + "', " + t_gender + ", " + str(f_total) + ", " + str(m_total) + ", " + str(percentage) + "\n")

out_file.close()
