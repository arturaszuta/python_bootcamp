my_list = [1,2,3];
your_list = [4,5,6];

print(my_list);

#indexing
print(my_list[1]);

#everything after that element
print(my_list[1:]);

#length of the array/string
print(len(my_list))

#concatonate lists
print(my_list + your_list);

#change items in the list
your_list[0] = 'four'

print(your_list)

#add new item to the end
your_list.append('seven')

print(your_list)

#remove last element of an array
popped_item = your_list.pop()

print(your_list)
print(popped_item)

all_list = your_list + my_list;

print(all_list);

#remove an element at a specific index
all_list.pop(-3);

print(all_list);

num_list = [1,5,7,4,3,6]

char_list = ['g','b','d','t','y','f','d']

#sorting a list - you've to execute sort fully before accesing 
print(num_list)
num_list.sort()
print(num_list)

print(char_list)
char_list.reverse()
print(char_list)
