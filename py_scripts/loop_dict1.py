book = ''' I know not if there is a reason
Why I am so sad at heart.
A legend of bygone ages
Haunts me and will not depart.
The air is cool under nightfall.
The calm Rhine courses its way.
The peak of the mountain is sparkling
With evening's final ray.'''

# make the string and make it a list of words
book_list = book.split()

dictionary = {'I':0}

for word in book_list:
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1
    


for k,v in dictionary.items():
    print(k)
    print(v)
