import math
from utils import *

reg = []

def main():
  a, b = getData()
  p, w = minMatchMemorized(a, b)
  print ('Pares:', p)
  print ('Weight:', w)

def minMatchMemorized(a,b):
  global reg
  a_blocks = getBlocks(a)
  b_blocks = getBlocks(b)
  i = len(a_blocks)
  j = len(b_blocks)
  reg = [[math.inf for x in range(j)] for y in range(i)]
  weight = minMatchMemorizedUtil(a_blocks, b_blocks)
  pairs = reconstructPairs(reg, i-1, j-1)
  return pairs, weight

def minMatchMemorizedUtil(a_blocks, b_blocks):
  global reg

  i = len(a_blocks)
  j = len(b_blocks)
  
  # Revisa el registro
  if reg[i-1][j-1] != math.inf:
    return reg[i-1][j-1]

  # Caso Base
  if i == 1 or j == 1:
    n = simplePair(i, j)
    w = calcWeight(a_blocks, b_blocks, n)
    reg[i -1][j-1] = w
    return w
  
  min_weight = math.inf
  min_pairs = []

  # Division
  for x in range(j-1):
    w = minMatchMemorizedUtil(a_blocks[:-1], b_blocks[0:x+1])
    n = staticPair([i-1], range(x+1, j))
    weight = w + calcWeight(a_blocks, b_blocks, n)
    
    if weight < min_weight:
      min_weight = weight
      min_pairs = n
  
  # Agrupacion
  for x in range(i-1):
    w = minMatchMemorizedUtil(a_blocks[:x+1], b_blocks[:-1])
    n = staticPair(range(x+1, i), [j-1])
    weight = w + calcWeight(a_blocks, b_blocks, n)
    
    if weight < min_weight:
      min_weight = weight
      min_pairs = n
    
  for p in min_pairs:
    if min_weight < reg[p[0]][p[1]]:
      reg[p[0]][p[1]] = min_weight
  
  return reg[i-1][j-1]

def reconstructPairs(matrix, i, j):
  pairs = []
  state = 0
  added = False

  while i != 0 and j != 0:
    added = False
    if state == 0:
      pairs.append((i, j))
      if matrix[i][j] == matrix[i-1][j]:
        state = 1
        i -= 1
      elif matrix[i][j] == matrix[i][j-1]:
        state = 2
        j -= 1
      else:
        state = 0
        i -= 1
        j -= 1
    elif state == 1:
      pairs.append((i, j))
      if matrix[i][j] == matrix[i-1][j]:
        i -= 1
      else:
        i -= 1
        j -= 1
        state = 0
        added = True
    else:
      pairs.append((i, j))
      if matrix[i][j] < matrix[i][j-1]:
        j -= 1
      else:
        i -= 1
        j -= 1
        state = 0
        added = True

  if not added:
    if i > 0:
      i -= 1
    if j > 0:
      j -= 1

  while i > 0:
    pairs.append((i, j))
    i -= 1

  while j > 0:
    pairs.append((i, j))
    j -= 1
  
  pairs.append((i, j))
  pairs.reverse()
  
  return pairs

if __name__ == "__main__":
  main()
