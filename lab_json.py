import json

numbers = [1,2,3,4]
#numbers 리스트를 json 형식으로 변환
numbers_string = json.dumps(numbers)
print(type(numbers_string))
print(numbers_string)

value_string = '{"x":10, "y":20, "size":4.5}'
value = json.loads(value_string)
print(type(value))
print(value)