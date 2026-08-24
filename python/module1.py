def recursion(k):
  if(k>0):
    result = k+recursion(k-1)
    
  else:
    result = 0
    
  return result

