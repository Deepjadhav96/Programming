def main():
  Arr = list() #empty list
  Size = 0

  #print("Enter the number of elements: ")
  Size = int(input("Enter the number of elements: "))

  print("Enter the elements:")
  
  for i in range(Size):
     no = int(input())
     Arr.append(no)

  print(Arr) 
if __name__=="__main__":
    main()