import random

u_case = chr(random.randint(65,90))
u_case2 = chr(random.randint(65,90))
u_case3 = chr(random.randint(65,90))

l_case=chr(random.randint(97,122))
l_case2=chr(random.randint(97,122))
l_case3=chr(random.randint(97,122))

num_1=chr(random.randint(97,122))
num_2=chr(random.randint(97,122))
num_3=chr(random.randint(97,122))

characters = [chr(35),chr(36),chr(37),chr(38),chr(42),chr(63),chr(64),chr(42), chr(33)]
c_choice=(random.choice(characters))
c_choice1=(random.choice(characters))

pwd = u_case+u_case2+u_case3+l_case+l_case2+l_case3+num_1+num_2+num_3+c_choice+c_choice1

tempList = list(pwd)
random.shuffle(tempList)
print(''.join(tempList))