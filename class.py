

# class employee :
#     def __init__(self,name):
#         self.name=name
#         print(f'{self.name} is born')
#     def __del__(self):
#         print(f'{self.name}')

# person1=employee('alice')
# person2=employee('bob')

# del person1

# class Employee:

#     id=11222
#     name= "kevin"
#     salary=10000

# kevin= Employee ()
# print(kevin.id)

class MyClass:
    def __init__(self,name):
        self.name = name

    def delete_name(self):
        del self.name  # Delete the 'name' attribute

# Create an instance of the class
obj = MyClass("Object")

# Access the attribute before deletion
print(obj.name)  # Output: Object

# Delete the attribute using a method
obj.delete_name()

# Accessing the attribute after deletion will raise an AttributeError
# because the attribute has been deleted
print(obj.name)  # Raises: AttributeError: 'MyClass' object has no attribute 'name'

