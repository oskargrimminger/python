dinner_list = ['Einstein', 'Musk', 'Newton']

message1 = "Would you like dinner with me Mr " + dinner_list[0].title() + "?"
message2 = "Would you like dinner with me Mr " + dinner_list[1].title() + "?"
message3 = "Would you like dinner with me Mr " + dinner_list[2].title() + "?"


print(message1)
print(message2)
print(message3)

message4 = dinner_list[1] + " cant make it"
print(message4)

del dinner_list[1]
dinner_list.append('Oppenheimer')
print(dinner_list)


message5 = "Would you like dinner with me Mr " + dinner_list[0].title() + "?"
message6 = "Would you like dinner with me Mr " + dinner_list[1].title() + "?"
message7 = "Would you like dinner with me Mr " + dinner_list[2].title() + "?"

print(message5)
print(message6)
print(message7)


dinner_list.insert(0,'Ronaldo')
dinner_list.insert(2,'Federer')
dinner_list.insert(6,'Jordan')

print(dinner_list)

first_one = dinner_list.pop(0)
first_message= "I am sorry you cant come " + dinner_list[0] + "!"
print(first_message)

second_one= dinner_list.pop(1)
second_message = "I am sorry you cant come " + dinner_list[1] +"!"
print(second_message)

third_one = dinner_list.pop(2)
third_message =  "I am sorry you cant come " + dinner_list[2] +"!"
print(third_message)

del dinner_list[4]
del dinner_list[5]
del dinner_list[6]


print(dinner_list)






