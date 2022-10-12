import re

number_1 = "431$**$&&50"
number_2 = "90133--éé"
number_3 = "989,459"

#first question
first_result = re.sub('[^0-9]', '0', number_1)

#second question
second_result = re.sub('[^0-9]', '', number_2)

#third question
number_3_4_array = number_3.split(',')

third_result = number_3_4_array[0]
fourth_result = number_3_4_array[1]

#fourth question
fifth_result = first_result + second_result + third_result

#fifth question
remainder = int(fifth_result)%int(fourth_result)
print(5%4)

