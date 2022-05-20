#https://stepik.org/lesson/590762/step/4?unit=585719

def nearest_perfect_number(a):
#a=int(input())

  to_check=[]
  for i in range(1,a+1,1):

      if a%i==0 and i<a:
          to_check.append(i)
         # print(i)
  '''down below constant argument in comparision to updated sum of list'''
  if sum(to_check)==a and a!=0: 
      print(
          "True", 
            sum(to_check), 
            to_check)
 # else:
#      print('sum: ',sum(to_check))
test=[30,28,6,19]
test=range(1,10000,1)
for a in test:
  nearest_perfect_number(a)
