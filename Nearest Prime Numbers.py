# Source: https://www.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print ('\t',f)
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f += 6
  return True    


def nearest_prime(n):

    p1 = None
    p2 = None
    
    if is_prime(n): # Verifiys if N is already a prime.
        return n

    # Find nearest prime < N
    for i in range (n, 0, -1):
        if is_prime(i):
            p1 = str(i) # p1 is a string for the return statement.
            break
    # Finds the nearest prime > N in range between N and N*2, which a prime should exist.
    while is_prime(i) == False:
          i = n
          if (n%2 == 0):
            i += 1
          else:
            i += 2
      
    
    return p1 + '<' + str(n) + '<' + p2
        
    

print(nearest_prime(1425172824437700148))


# Problems: Possible integer overlow with larger integers using N*2
