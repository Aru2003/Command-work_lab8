korteg1=(),korteg2=()
def fill_tuple(start,end):
 return tuple(range(start,end))
korteg1=fill_tuple(0,6)
print(korteg1)
print('__________________')
korteg2=fill_tuple(-5,1)
print(korteg2)
print('__________________')
korteg3=korteg1+korteg2
count_zero = korteg3.count(0)
print(f"tree corteg: {korteg3}")
print(f"Count of zeros: {count_zero}")