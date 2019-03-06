    
def move():
    their_history = 'c'    
    if their_history[-3:] == 'ccc':
      return 'b'
    elif their_history[-2:]  == 'cc':
      return 'c'
    else:
        return 'b'
        
        