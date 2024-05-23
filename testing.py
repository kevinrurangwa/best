# class Employee:
#     id=None
#     salary=None
#     dep=None

# obj= Employee()
# obj.id=123333
# obj.salary=2000
# obj.dep='It'
# print(obj.salary)

# .................
class Employee:
 def __init__(self,id,salary,dep):
    self.id=None
    self.salary= dep
    self.dep=None

obj= Employee(12,2000,'IT')
print(obj.salary)


