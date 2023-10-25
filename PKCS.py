def padding(block : bytes, size = 16) : 
  if len(block) >= size : 
    return block 
  padding_number = size - len(block)  

  for i in range(padding_number) : 
    block += padding_number.to_bytes(1, 'big')
  
  return block 


if __name__ == '__main__' : 
  key = "YELLOW SUBMARINE"
  print(padding(key.encode(), 21))
  