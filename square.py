Square of each value
l=[0,1,2,3,4,5]
l1=list(map(lambda n:n*n,l))
print(l1)
Thank You
Nested Functions
def outer():
  print("Outer function execution")
  def inner():
    print("Inner function execution")
  inner()
outer()  
