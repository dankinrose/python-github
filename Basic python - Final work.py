#Ex1--------------------------------------------------------------------------------------------------

def print_num():
    print("numbers from 12 to 24:")
    for x in range(12, 25):
        print(x)

#Ex2--------------------------------------------------------------------------------------------------

def print_odd():
    print("ODD numbers from 7 to 31:")
    for x in range(7, 32):
        if x % 2 != 0:
            print(x)

#Ex3--------------------------------------------------------------------------------------------------

def print_even():
    print("EVEN numbers from 10 to 20:")
    for x in range(10, 21):
        if x % 2 == 0:
            print(x)

#Ex4--------------------------------------------------------------------------------------------------

def print_multiples():
    for x in range(1, 46):
        if x % 3 == 0 and x % 5 == 0:
            print(str(x) + ": FizzBuzz")
        elif x % 3 == 0:
            print(str(x) + ": Fizz")
        elif x % 5 == 0:
            print(str(x) + ": Buzz")

#Ex5:-------------------------------------------------------------------------------------------------

def calculate_sum(given_array):
    sum = 0
    for n in given_array:
        sum += n
    return sum

#Ex6:--------------------------------------------------------------------------------------------------
#part 1-2:
def delete_students_property(student_list, property):
        for student in student_list:
            if property in student:
                del student[property]

def print_student_properties(student_list):
    for student in student_list:
        print("---- student", student_list.index(student) +1,"----")
        for key, value in student.items():
            print(f"{key} : {value}")
#part 3:
def sort_students_by_age(student_list):
    new_list = []
    for student in student_list:
        new_list.append((student["age"], student))
        new_list.sort(reverse = True)
    sorted_students = []
    for age, student in new_list:
        sorted_students.append(student)
    return sorted_students

#Ex7:----------------------------------------------------------------------------------------------------
#part 1:
def print_cat(our_pets):
    for pet in our_pets:
       for key in pet.keys():
           if pet[key] == "cat":
               print(key, ":", pet[key])
#part 2:
def print_pet_names(our_pets, animal_type):
    for pet in our_pets:
        if pet["animal_type"] == animal_type:
            print(pet["names"])
            break
    else:
        print(None)
#part 3:
def add_pet_name(our_pet, new_name):
    for pet in our_pet:
        for name in pet["names"]:
            if name == new_name:
                break
        else:
            pet["names"].append(new_name)

#Ex8:----------------------------------------------------------------------------------------------------
#part 1:
def print_student_data(student):
    for key, value in student.items():
        print(f"{key} : {value}")
#part 2-3:
def add_new_hobby(student, new_hobby):
        if new_hobby not in student["hobbies"]:
            student["hobbies"].append(new_hobby)
#part 4-5:
def delete_hobby(hobby):
            if hobby in student["hobbies"]:
                student["hobbies"].remove(hobby)
#part 6:
def add_property(new_prop):
    student.update(new_prop)
    print_student_data(student)

#Ex9:------------------------------------------------------------------------------------------------------

def print_matrix(matrix1):
    for row in matrix1:
        for element in row:
            print(element, end = " ")

#Ex10:-----------------------------------------------------------------------------------------------------

def zero_count(matrix2):
    zero_count = 0
    for row in matrix2:
        for num in row:
            if num == 0:
                zero_count += 1
    return zero_count

#Ex11:-------------------------------------------------------------------------------------------------------

def find_dup(arr):
    arr_result = []
    for e in set(arr):
        count_num = arr.count(e)
        if count_num > 1:
            arr_result.append(e)
    return arr_result

#Ex12:-----------------------------------------------------------------------------------------------------

def reverse_array(my_array):
    reversed_array = []
    for element in my_array:
        reversed_array.insert(0, element)
    return reversed_array

#Ex13:-----------------------------------------------------------------------------------------------------

def sum_arrays(first_array, second_array):
    sum_array = []
    for i in range(len(first_array)):
        sum_array.append(first_array[i] + second_array[i])
    return sum_array

#Ex14------------------------------------------------------------------------------------------------------

def is_palindrome(pal_str):
    reverse_string = ""
    pal_str = pal_str.lower().replace(" ", "")
    for char in pal_str:
        reverse_string = char + reverse_string
    return pal_str == reverse_string

#Ex15-------------------------------------------------------------------------------------------------------

def iterate_less_100():
    print("iterate loop as long as counter is less than 100:")
    counter = 1
    while counter < 100:
        print(counter)
        counter = counter * 2

#Ex16-------------------------------------------------------------------------------------------------------

def iterate_greater_50():
    print("iterate loop as long as counter is greater than 50:")
    counter = 900000
    while counter > 50:
        print(counter)
        counter = counter / 2

#Ex17:------------------------------------------------------------------------------------------------------

def find_dup_str(string_array):
    i = 0
    dup_strings_arr = []

    while i < len(string_array):
        count = 0
        x = 0
        while x <len(string_array):
            if string_array[i] == string_array[x]:
                count += 1
            x += 1
        if count > 1 and string_array[i] not in dup_strings_arr:
            dup_strings_arr.append(string_array[i])
        i += 1
    return dup_strings_arr

#Ex18:-------------------------------------------------------------------------------------------------------

def remove_dup(names_ar):
    clean_list = []
    i = 0

    while i < len(names_ar):
        if names_ar[i] not in clean_list:
            clean_list.append(names_ar[i])
        i += 1
    return clean_list

#Ex19:--------------------------------------------------------------------------------------------------------

def remove_dup_and_skip(names_array):
    clean_list = []
    i = 0

    while i < len(names_array):
            current_name = names_array[i]
            i += 1
            if current_name == "Pete":
                continue
            elif current_name not in clean_list:
                clean_list.append(current_name)
    return clean_list

#Ex20:------------------------------------------------------------------------------------------------------

def find_successive_values(boolean_array):
    i = 1
    while i < len(boolean_array):
        if boolean_array[i] == boolean_array[i - 1]:
            return i
        i += 1
    return -1

#Ex21:--------------------------------------------------------------------------------------------------------

def get_user_input():
    while True:
        full_name = input("enter your full name(first and last):")
        full_name_parts = full_name.split()
        if len(full_name_parts) == 2:
            first, last = full_name_parts
            if first.isalpha() and last.isalpha():
                break
            else:
                print("invalid input, please enter exactly two words.")
        else:
            print("invalid input, please enter exactly two words.")

    while True:
        age = input("enter your age(1-130):")
        if age.isdigit():
            age = int(age)
            if 1 <= age <= 130:
                break
            else:
                print("invalid age, please enter a number between 1 and 130")
        else:
            print("invalid age, please enter a number between 1 and 130")

    while True:
        email = input("enter your email:")
        if "@" in email and email.count("@") == 1:
            email_parts = email.split("@")
            if email_parts[0] != "" and email_parts[1] != "":
                break
            else:
                print("invalid email, please enter text before and after '@' ")
        else:
            print("invalid email, please enter text that includes one '@' inside")

    print()
    print("---- User data ----\n")
    print("Full name:", full_name)
    print("Age:", age)
    print("Email:", email)

#-----------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    print("Ex1:")
    print_num()
    print()

    print("*********\n")

    print("Ex2:")
    print_odd()
    print()

    print("*********\n")

    print("Ex3:")
    print_even()
    print()

    print("*********\n")

    print("Ex4:")
    print_multiples()
    print()

    print("*********\n")

    print("Ex5:")
    given_array = [1,13,22,123,49,34,5,24,57,45]
    print("sum of array:",calculate_sum(given_array))
    print()

    print("*********\n")

    print("Ex6:")

    student_list = [
        { "id" : 1,
          "first_name" : "Daniel",
          "last_name" : "rozenberg",
          "age" : 27,
          "country" : "Israel",
          "city" : "Ariel"
          },
        {"id": 2,
         "first_name": "Josh",
         "last_name": "Brown",
         "age": 30,
         "country": "USA",
         "city": "New York"
         },
        {"id": 3,
         "first_name": "Dana",
         "last_name": "Levi",
         "age": 28,
         "country": "Israel",
         "city": "Tel Aviv"
         }
                    ]

    print("original array:")
    print(student_list, "\n")
    delete_students_property(student_list, "country")
    print("part 1-2:")
    print("each property of each student in the array after property deletion:\n")
    print_student_properties(student_list)
    print()
    print("part 3:")
    print("sorted array by students age:")
    print(sort_students_by_age(student_list))
    print()

    print("*********\n")

    print("Ex7:")
    our_pets = [
        {
            "animal_type": "cat",
            "names": [
                "Meowzer",
                "Fluffy",
                "Kit-Cat"
            ]
        },
        {
            "animal_type": "dog",
            "names": [
                "Spot",
                "Bowser",
                "Frankie"
            ]
        }
    ]

    print("part 1:")
    print("requested key-value:")
    print_cat(our_pets)
    print()

    print("part 2:")
    print("first condition - animal type exists in the object:")
    print_pet_names(our_pets, "dog")
    print("second condition - animal type is not exists in the object:")
    print_pet_names(our_pets, "mouse")
    print()

    print("part 3:")
    add_pet_name(our_pets, "Star")
    print("array after addition of new name to pets:")
    print(our_pets)
    print()

    print("*********\n")

    print("Ex8:")
    student = {
        'name': 'John',
        'age': 20,
        'hobbies': ['reading', 'games', 'coding'],
    }
    print("part 1:")
    print("all student data:")
    print_student_data(student)
    print()

    print("part 2-3:")
    print("student data after adding new hobby:")
    add_new_hobby(student, "running")
    print_student_data(student)
    print()

    print("part 4-5:")
    print("student data after deleting hobby:")
    delete_hobby("reading")
    print_student_data(student)
    print()

    print("part 6:")
    new_prop= {"family_name": "rozenberg"}
    print("student data after adding new property:")
    add_property(new_prop)
    print()

    print("*********\n")

    print("Ex9:")
    matrix1 = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    print("all the elements in matrix:")
    print_matrix(matrix1)
    print("\n")

    print("*********\n")

    print("Ex10:")
    matrix2 = [
        [0, 1, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]

    print("total zero count:", zero_count(matrix2))
    print()

    print("*********\n")

    print("Ex11:")
    arr = [4,2,34,4,1,12,1,4]
    print("array of repeated elements:")
    print(find_dup(arr))
    print()

    print("*********\n")

    print("Ex12:")
    my_array =  [43, "what", 9, True, "cannot", False, "be", 3, True]
    print("reversed array:", reverse_array(my_array))
    print()

    print("*********\n")

    print("Ex13:")
    first_array = [4, 6, 7]
    second_array = [8, 1, 9]
    print("sum of arrays:", sum_arrays(first_array, second_array))

    print("*********\n")

    print("Ex14:")
    first_str = "racecar"
    second_str = "Java"
    print("first string is palindrome:", is_palindrome(first_str))
    print("second string is palindrome:", is_palindrome(second_str))
    print()

    print("*********\n")

    print("Ex15:")
    iterate_less_100()
    print()

    print("*********\n")

    print("Ex16:")
    iterate_greater_50()
    print()

    print("*********\n")

    print("Ex17:")
    string_array = ["AI", "daniel", "AI", "rozenberg", "daniel", "student", "student", "Hay"]
    print("array of the repeated values:")
    print(find_dup_str(string_array))
    print()

    print("*********\n")

    print("Ex18:")
    names_ar =  ["Chris", "Kevin", "Naveed", "Pete", "Victor", "Chris", "Kevin"]
    print("names array after removing duplicated names:")
    print(remove_dup(names_ar))
    print()

    print("*********\n")

    print("Ex19:")
    names_array =  ["Chris", "Kevin", "Naveed", "Pete", "Victor", "Chris", "Kevin"]
    print("names array after function:")
    print(remove_dup_and_skip(names_array))
    print()

    print("*********\n")

    print("Ex20:")
    print("check for index of the same successive value in the arrays:")
    print("first array:", find_successive_values([True, False, False, True, True, False]))
    print("second array:", find_successive_values([True, False, True, False, True, True]))
    print("third array:", find_successive_values([True, False, True, False, True, False]))
    print()

    print("*********\n")

    print("Ex21:")
    get_user_input()
    print()

    print("********** End of final work **********")









