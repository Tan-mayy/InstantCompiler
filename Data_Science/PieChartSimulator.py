import matplotlib.pyplot as plt

i = 0
for i in range(0,11) :
    print( (i+1) * '*')

print('             Pie-Chart Simulator')

for j in range(0,11):
    print((11 - j) * '*')


data = []

def check_data():
    a = input('Enter value : \n')
    data.append(a)
    
    
while True:
    check_data()
    ques = input('Is there any more data ? (Y/N)\n')
    if ques == 'Y' or ques == 'y':
        pass
    elif ques == 'N' or ques == 'n':
        break


size = len(data)
# print(size)

head = input('Enter a Title for Your Pie-Chart :\n')
plt.title(head)

labelss = []
for i in range(0,size):
    l = input('Label your Segments of Pie-Chart Sequentially \n Enter :\n')
    labelss.append(l) 

chart = plt.pie(data, labels=labelss,)

plt.show()
        


