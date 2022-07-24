with open('file1.txt') as file1:
  list_of_numbers1 = file1.readlines()
  list_of_numbers1 = [int(n.replace('\n', '')) for n in list_of_numbers1]

with open('file2.txt') as file2:
  list_of_numbers2 = file2.readlines()
  list_of_numbers2 = [int(n.replace('\n', '')) for n in list_of_numbers2]

result = [n for n in list_of_numbers1 if n in list_of_numbers2]

# Write your code above 👆

print(result)


