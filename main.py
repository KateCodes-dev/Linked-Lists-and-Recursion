
from linked_list import LinkedList

employees = LinkedList()

# Insert employee IDs.
for employee_id in [10, 20, 30, 40]:
    employees.insert_at_front(employee_id)

print("Original list:", employees.to_list())
print("Sum of IDs:", employees.sum())
print("Search for 20:", employees.search(20))
print("Search for 99:", employees.search(99))

employees.reverse()
print("Reversed list:", employees.to_list())

# Test empty-list behavior.
empty_list = LinkedList()
print("Empty list sum:", empty_list.sum())
print("Search empty list:", empty_list.search(10))
empty_list.reverse()
print("Reversed empty list:", empty_list.to_list())
