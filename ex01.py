people =[ 
  {"name": "Alice", "age": 25, "city": "New York"}, 
  {"name": "Bob", "age": 30, "city": "Los Angeles"}, 
  {"name": "Charlie", "age": 35, "city": "Chicago"},
  {"name": "David", "age": 40, "city": "Houston"},
  {"name": "Eve", "age": 45, "city": "Phoenix"} 
] 
def binary_search_people(people, target_name): 
 """Perform binary search fora person's name in alist of dictionaries."""
 #Sort the list of people by name 
 sorted_people =sorted(people, key=lambda x: x["name"]) 
 left, right = 0, len(sorted_people)- 1
 while left <= right:
  mid =(left +right)// 2 
  if sorted_people[mid]["name"] == target_name: 
     return sorted_people[mid] 
  elif sorted_people[mid]["name"] < target_name: 
    left = mid +1
  else: 
    right = mid-1
 return None 
target_name =input("Enter the name that you wanna search:") 
result = binary_search_people(people, target_name) 
if result:
   print(f"Found {target_name}: {result}") 
else:
  print(f"{target_name} not found in the list")