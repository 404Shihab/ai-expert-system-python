# N Queen Attack Detection

def drawBoard(P):
  N = len(P)
  for i in range(1,N+1):
    print("|", end="")
    for j in range(1,N+1):
      if (i,j) in P:
        ind = str(1+ P.index((i,j)))
        print(" "+ind+" |", end= "")
      else:
        print(" * |", end= "")
    print()


from math import ceil
import random
def generate_positions(N):
    CL = list(range(0,N*N));
    P = []
    for i in range(N):
        p = random.choice(CL)
        CL.remove(p)
        r = ceil((p+1)/N)
        c = 1+p%N
        P.append((r,c))
        print('Q{}: {},{}'.format(i+1,r,c))
    return P


N = 4
positions = generate_positions(N)
drawBoard(positions)


# row attack
def rowAttacK(P):
  count = 0
  for i in range(N):
    for j in range(i+1,N):
      if P[i][0] == P[j][0]:
        print('row attack:', end = " " )
        print(P[i], end = ", ")
        print(P[j]) 
        count = count + 1 
  return count

rowAttacK(positions)


#column attack
def columnAttack(P):
  count = 0
  for i in range(N):
    for j in range(i+1,N):
      if P[i][1] == P[j][1]:
        print('column attack:', end = " " )
        print(P[i], end = ", ")
        print(P[j])
        count = count + 1
  return count

columnAttack(positions)


# diagonal attack
def diagonalAttack(P):
  count = 0
  for i in range(N):
    for j in range(i+1,N):
      if abs(P[i][0] - P[j][0]) == abs(P[i][1] - P[j][1]):
        print('diagonal attack:', end = " " )
        print(P[i], end = ", ")
        print(P[j])
        count = count + 1
  return count

diagonalAttack(positions)


# implement a method to print a state is valid or not
# input row and col (two lists)
def isValid(rows, cols):
  P = []
  for i in range(len(rows)):
    P.append((rows[i], cols[i]))

  global N
  N = len(P)

  row_count = rowAttacK(P)
  column_count = columnAttack(P)
  diagonal_count = diagonalAttack(P)

  if row_count == 0 and column_count == 0 and diagonal_count == 0:
    print("State is valid")
    return True
  else:
    print("State is not valid")
    return False


# Example
rows = [1, 2, 3, 4]
cols = [2, 4, 1, 3]

isValid(rows, cols)