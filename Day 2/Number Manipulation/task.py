bmi = 84 / 1.65 ** 2

print(int(bmi))  # 30.85 -> 31
print(round(bmi)) # 30.858534546456456 -> 31 return bmi to no decimal places and just takes the integer value
print(round(bmi,2)) # 30.8589e8878374 to 30.85 return bmi to two decimal places

# shorthand loop manipulation
    # score++ #shorthand of score = score + 1
    # score+=1 #shorthand of score = score + 1
    # score-=1 #shorthand of score = score - 1


# instead of type casting everytime what we can do is use f string
height = 5.1
score = 0
is_winning = True

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")