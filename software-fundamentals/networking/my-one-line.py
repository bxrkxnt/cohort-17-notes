def thing(s: str, symbol: str): # O(n)
    return s.replace(symbol, " ", 1).find(symbol)

def dif_thing(s: str, symbol: str): # O(n)
    return s.find(symbol, s.find(symbol)+1)