mixed_list = ['cat', 5, 'flower', 10]
string_list = []
num_list = []

for item in mixed_list:
    if type(item)== str:
        string_list.append(item)
    else:
        num_list.append(item)

print(string_list)
print(num_list)
        
