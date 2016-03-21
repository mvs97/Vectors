class Vector:

  def _init_(self, array1):
    
    self.coords = array1
    self.length = len(array1)
    
    
  def __add__(self, array2):
  
    if (self.length == array2.length):
      result = Vector(self, coords)
      for i in range(array2.length):
        result.coords[i] = self.coords[i] + array2.coords[i]
        return result
      
      else:
        print("Vector dimensions don't match")
        Vector.coords = "ERROR"
        return Vector
        

  def __sub__(self, array2):
    
    if (self.length == array2.length):
      result2 = Vector(self.coords)
      for i in range(array2.length):
        result2.coords[i] = self.coords[i] - array2.coords[i]
        return result2

      else:
        print("Vector dimensions don't match")
        Vector.coords = "ERROR"
        return Vector


  def __mul__(self, array2):
    
    result3 = 0
    if (self.length == array2.length):
      for i in range(array2.legth):
        result3 = result3 + self.coords[i] * array.coords[i]
        return result3
      else:
         print("Vector dimensions don't match")
         return "ERROR"
      
     

        
        
        
      
      
    
    
    

 

  
    
     

  
