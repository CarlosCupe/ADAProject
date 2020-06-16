import math
from utils import *

def main():
  a, b = getData()
  p, w = minMatch(a, b)
  print ('Pares:', p)
  print ('Weight:', w)

def minMatch(a,b):
  a_blocks = getBlocks(a)
  b_blocks = getBlocks(b)
  pairs = minMatchUtil(a_blocks, b_blocks)
  weight = calcWeight(a_blocks, b_blocks, pairs)
  return pairs, weight

def minMatchUtil(a_blocks, b_blocks):
  i = len(a_blocks)
  j = len(b_blocks)

  # Caso Base
  if i == 1 or j == 1:
    return simplePair(i, j)
  
  min_weight = math.inf
  min_pairs = []
  
  # Division
  for x in range(j-1):
    m = minMatchUtil(a_blocks[:-1], b_blocks[0:x+1])
    n = staticPair([i-1], range(x+1, j))
    pairs = m + n
    
    weight = calcWeight(a_blocks, b_blocks, pairs)
    if weight < min_weight:
      min_weight = weight
      min_pairs = pairs
  
  # Agrupacion
  for x in range(i-1):
    m = minMatchUtil(a_blocks[:x+1], b_blocks[:-1])
    n = staticPair(range(x+1, i), [j-1])
    pairs = m + n
    
    weight = calcWeight(a_blocks, b_blocks, pairs)
    if weight < min_weight:
      min_weight = weight
      min_pairs = pairs

  return min_pairs

if __name__ == "__main__":
  main()
