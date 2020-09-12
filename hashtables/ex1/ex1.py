def get_indices_of_item_weights(weights, length, limit):
    
    cache = {}
    x = None
    for i in range(0, length):
        cache[weights[i]] = i 
  
    for j in range(0, length):
        x = limit - weights[j]
        if x in cache:
          return [cache[x], j]
            
    
    return None