import math


def difference_formula(n, d):
  total = 0
  for i in range(n+1):
    total += math.comb(n, i)*(-1)**(n-i)*(i+1)**d

  return total


def get_difference(n, k):
  difference_coefficients = []
  for j in range(k+2-n):
    total = difference_formula(n, k+1-j)
    difference_coefficients.append(total)
  
  return difference_coefficients


def get_value(n, k):
  total = 0
  sequence = []
  for j in range(1, k+3):
    total += j**k
    sequence.append(total)

  value = 0
  for i in range(n+1):
    value += math.comb(n, i)*(-1)**(n-i)*sequence[i]

  return value


def lcm(a, b):
  return (a*b) // math.gcd(a, b)


def simplify(n, d):
  g = math.gcd(n, d)
  n //= g
  d //= g
  return n, d


def multiply(number, rational):
  n = int(rational[:rational.index('/')])
  d = int(rational[rational.index('/')+1:])
  n *= number
  n, d = simplify(n, d)
  return str(n) + '/' + str(d)


def add(r1, r2):
  n1 = int(r1[:r1.index('/')])
  d1 = int(r1[r1.index('/')+1:])
  n2 = int(r2[:r2.index('/')])
  d2 = int(r2[r2.index('/')+1:])
  d3 = lcm(d1, d2)
  n3 = n1*(d3//d1) + n2*(d3//d2)
  n3, d3 = simplify(n3, d3)
  return str(n3) + '/' + str(d3)


def subtract(number, rational):
  n = int(rational[:rational.index('/')])
  d = int(rational[rational.index('/')+1:])
  n2 = number*d - n
  n2, d = simplify(n2, d)
  return str(n2) + '/' + str(d)


def divide(rational, number):
  n = int(rational[:rational.index('/')])
  d = int(rational[rational.index('/')+1:])
  d *= number
  n, d = simplify(n, d)
  return str(n) + '/' + str(d)
  

def solve(c, v, s):
  total = '0/1'
  for i in range(len(s)):
    total = add(total, multiply(c[i], s[i]))

  return divide(subtract(v, total), c[-1])


def get_coefficients(k):
  coefficients = []
  for i in range(k+1, -1, -1):
    difference_coefficients = get_difference(i, k)
    difference_value = get_value(i, k)
    coefficients.append(solve(difference_coefficients, difference_value, coefficients))
  
  return coefficients


def generate_polynomial(coefficients):
  polynomial = []
  for i in range(len(coefficients)):
    j = len(coefficients) - i - 1
    c = coefficients[i]
    if c != '0/1':
      if j == 0:
        polynomial.append(c)
      elif j == 1:
        polynomial.append(c + 'n')
      else:
        polynomial.append(c + 'n^' + str(j))

  return (' + '.join(polynomial)).replace('+ -', '- ')


def get_formula(k):
  coefficients = get_coefficients(k)
  return generate_polynomial(coefficients)


def main():
  k = 6
  print(get_formula(k))


if __name__ == "__main__":
  main()
