
#Git Tutorial
#This tutorial is setup for 4 individuals to see how git functions, please make sure you have gotten the instructions
#The instructions can be gotten via a git request to the API at: http://gatlin-server:5001/instructions/<user#>
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#Person 1 (add what instructions say) || Person 3 change after rebase
for i in range(10):
  print(i)


#Person 2 (add what instructions say) || Person 4 change before rebase to cause a merge conflict
i = 2
if i % 4 == 0:
  print("divisble by 4")
else:
  print("not divisble by 4")

