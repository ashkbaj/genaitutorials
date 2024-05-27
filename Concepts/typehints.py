from typing import Tuple, Dict, List, Union, Optional, Any, Iterable, Callable, Literal, Final #, TypeAlias



emp_name: str = "Ashish"

emp_year:int = 10
emp_tasks:list = []
emp_projects1:tuple = ()
emp_personal_info:dict = {}



# Enforcing Typehints
emp_tasks: List[int] = []
emp_projects: Tuple[str] = ()
emp_personal_info: Dict[int, str] = {}

print(emp_name)
print(type(emp_projects))
print(type(emp_projects1))


#Any type
data1: Any = 10

#Optional type
data2:Optional[int] = 2

#Union of two or more datatypes
side1: float = 10
side2: float = 2.537
area: Union[int, float] = side1 * side2
#area: int|float = side1 * side2
print(area)

#Constant Objects using Final
pi: Final = 3.1412


#Iterable Objects
arr: Iterable[str] = [1, 45, 'Ashish', 'New', '65', 89]
print (type(arr))
print (arr)

#Typehints for fixed values
fixed:Literal = ['A', 'B', 'C', 'D']
print(type(fixed))

#Typehint in functions
def returndef(var1: str, var2: str) -> str:
    return 'Return Value'


#TypeAlias as typehint
#InfloStr: TypeAlias = Union[int, float, str]
#data3: InfloStr = 10
#print(type(data3))

#callable function

def functionB(int):
    return int*5

def functionA(function: Callable) -> int:
    print(function)


functionA(functionB(5))




