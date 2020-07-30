
# Define a filename.
filename = "data_mine/a_1.txt"
data = []
# Open the file as f.
# The function readlines() reads the file.
with open(filename) as f:
    content = f.readlines()
for x in range(len(content)):
    dataFrame = []
    dataFrame.append(content[x].split(' ')[1]) 
    dataFrame.append(content[x].split(' ')[2])
    dataFrame.append(content[x].split(' ')[3])
    dataFrame.append(content[x].split(' ')[4])
    dataFrame.append(content[x].split(' ')[5])
    dataFrame.append(content[x].split(' ')[6])
    data.append(dataFrame)
f.close()
print(data)