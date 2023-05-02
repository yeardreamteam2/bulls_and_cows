import random

guess_num = random.sample(range(10), 4)
print(guess_num)

while True:
  num_list = list()
  for i in range(4):
        
    while True:
        print(f"give me {i+1}th num: ", end="")

        try :
            num = int(input())
            num_list.append(num)
            break
        except :
            print("your number is not a number")

  match_cnt = 0
  goal_cnt = 0

  for i in range(4):
    if num_list[i] == guess_num[i]:
      goal_cnt += 1
    elif num_list[i] in guess_num:
      match_cnt += 1
    
  if goal_cnt == 4:
    print('win')
    break
  else:
    print(f'bulls:{goal_cnt}, cows:{match_cnt}')
