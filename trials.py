# program to accept user input to create a list of intergers

user_input = input(123)
int_list = [int(num) for num in user_input.split()]

# compute the sum of the intergers in the list

sum_results = sum(int_list)
print(f"sum of the integers: {sum_results}")