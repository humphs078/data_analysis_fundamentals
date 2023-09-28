import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

lower = 1
upper = 10001


def collatz(number):
  collatz_sequence_list=[]
  len_collatz_list = []
  loop_list = [4, 2, 1]
  if number == 1:
    collatz_sequence_list = [4, 2, 1]
  elif number == 2:
    collatz_sequence_list = [1, 4, 2, 1]
  else:
    # collatz_sequence_list.append(number)
    while(number!=1):
      if(number%2==0):
        number=number//2
        collatz_sequence_list.append(number)
      else:
        number=number*3+1
        collatz_sequence_list.append(number)
        print(collatz_sequence_list)

collatz(10)

def collatz_orbit_lenghth(number):
  collatz_sequence_list_2 = []
  
  while(number !=1):
    if number%2==0:
      number = number/2
      collatz_sequence_list_2.append(number)
    else:
      number = (3*number)+1
      collatz_sequence_list_2.append(number)
  return len(collatz_sequence_list_2) 
  #print(len(collatz_sequence_list_2))

list = []
for x in range(lower, upper):
  q = collatz_orbit_lenghth(x)
  list.append(q)

number = [x for x in range(lower, upper)]
# print(number)

print(list)

data = {"number": number,"length": list}

df = pd.DataFrame(data)
print(df)

sns.scatterplot(data=df, x="number", y="length")
plt.show()
