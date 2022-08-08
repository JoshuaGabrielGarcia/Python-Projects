def fib(n):
  list=[]
  for i in range(n):
    if i > 1:
      list.append(list[i - 2] + list[i - 1])
    else:
      list.append(i)
  print(list)

num = input("Up to which number of Fibonacci seq : ")
fib(int(num))











