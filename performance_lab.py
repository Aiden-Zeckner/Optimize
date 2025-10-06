# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

#lists for ALL questions
data_1=[1, 2, 3, 4, 4]
data_2=[1, 1, 3, 3, 2, 2]
data_3=[-1, 0, 75, 1000000, 1000000]

def most_frequent():
    while True:
        answer=input("Which test? (1,2,3, or end)")
        if answer=="1":
            new_data=dict((num,data_1.count(num)) for num in set(data_1)) #turns list into a dictionary list
            count_max=max(new_data.values())#counts the value in each list item
            print([num for num, count in new_data.items() if count==count_max])#finds which item is most
            
        elif answer=="2":
            new_data=dict((num,data_2.count(num)) for num in set(data_2))
            count_max=max(new_data.values())
            print([num for num, count in new_data.items() if count==count_max])

        elif answer=="3":
            new_data=dict((num,data_3.count(num)) for num in set(data_3))
            count_max=max(new_data.values())
            print([num for num, count in new_data.items() if count==count_max])

        else:
            print("goodbye")
            break
#commented start
#most_frequent()

"""
Time and Space Analysis for problem 1:
- Best-case:list is small, takes only a few inputs
- Worst-case:list is extremely large, has to look over dictionary several times
- Average-case:list is avredge sized, takes a little time with medium inputs
- Space complexity:O(n)
- Why this approach?
it looks over every number so it counts how many times it is seen
- Could it be optimized?
yes, but not though space complexity, it restates a lot of stuff and I could have turned the main function into a seperate definition
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates():
    while True:
        seen=set()
        answer=input("Which test? (1,2,3, or end)")
        if answer=="1":
            new_data=set(data_1)
            print([num for num in data_1 if not (num in seen or seen.add(num))])
        elif answer=="2":
            new_data=set(data_2)
            print([num for num in data_2 if not (num in seen or seen.add(num))])
        elif answer=="3":
            new_data=set(data_3)
            print([num for num in data_3 if not (num in seen or seen.add(num))])
        else:
            print("goodbye")
            break    

#remove_duplicates()
"""
Time and Space Analysis for problem 2:
- Best-case:small list and already in order
- Worst-case:large list that has no repeats
- Average-case:medium list that has some but not many repeats
- Space complexity:O(n)
- Why this approach?
so I could easily remove all reapeats and just have to find a way to put it in order of the original list
- Could it be optimized?
yeah, main function could ahve been a defintion and I could have removed some repeating data
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs():
    while True:
        known_number=[]
        seen_numbers=[]
        answer=input("Which test? (1,2,3, or end)")
        if answer=="1":
            new_data=list(set(data_1))
            for number in new_data:
                possible_number=5-number
                if possible_number in new_data:
                    known_number.append(number)
                    seen_numbers.append(possible_number)
            paired_list=list(zip(known_number,seen_numbers))
            print(paired_list)
            
        elif answer=="2":
            new_data=list(set(data_2))
            for number in new_data:
                possible_number=5-number
                if possible_number in new_data:
                    known_number.append(number)
                    seen_numbers.append(possible_number)
            paired_list=list(zip(known_number,seen_numbers))
            print(paired_list)

        elif answer=="3":
            new_data=list(set(data_3))
            for number in new_data:
                possible_number=5-number
                if possible_number in new_data:
                    known_number.append(number)
                    seen_numbers.append(possible_number)
            paired_list=list(zip(known_number,seen_numbers))
            print(paired_list)

        else:
            print("goodbye")
            break

#find_pairs()
"""
Time and Space Analysis for problem 3:
- Best-case:very small list, with no solutions
- Worst-case:very large list with many solutions
- Average-case:medium list with few solutions
- Space complexity:O(n)
- Why this approach?
I thought it would be easy just to find the number needed to complete the sum ratehr that find two numerbs to coplete the sum
i.e x+3=5 is easier to rotate through than x+y=5
- Could it be optimized?
yeah, I could have turned the main function into a definition
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.



def add_n_items():
    limit=4
    the_list=[]
    new_list=[]
    while True:
        answer=input("would you like to add an item to the list (Y/N)")
        if answer=="Y":
            answer=int(input("how many?, current limit "+str(limit)))
            while True:
                the_list.append(1)
                answer=answer-1
                if answer==0:
                    break
            while True:
                list_amount=len(the_list)
                if list_amount>limit:
                    limit=limit*2
                    print("not enough space, doubling size of current list")
                if list_amount<limit:
                    break
            new_list.extend(the_list)
            the_list.clear()
            print("items added")
        else:
            print("goodbye")
            break

#add_n_items()
"""
Time and Space Analysis for problem 4:
- When do resizes happen?when the limit is surpassed
- What is the worst-case for a single append?a ton of data has to be copied
- What is the amortized time per append overall?)O(1)
- Space complexity:O(n)
- Why does doubling reduce the cost overall?
since theres less data to look throguh
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def adding(data_choice):
    total_list=[]
    current_total=0
    for num in data_choice:
        current_total+=num
        total_list.append(current_total)
    print(total_list)

def running_total():
    while True:
        answer=input("Which test? (1,2,3, or end)")
        if answer=="1":
            data_choice=data_1
            adding(data_choice)
        elif answer=="2":
            data_choice=data_2
            adding(data_choice)
        elif answer=="3":
            data_choice=data_3
            adding(data_choice)
        else:
            print("goodbye")
            break    

running_total()
"""
Time and Space Analysis for problem 5:
- Best-case:little amount of small digigt numbers
- Worst-case:infinite list
- Average-case:medium sized list with decent sized digits
- Space complexity:O(n)
- Why this approach?
just appends stuff with a constatnly changing variable, it is good for small lists
- Could it be optimized?
yeah, main function could have been an definition

-optimization
I optimized this one by changint the main function into a definition. I couldn't change the time and space complexity since 
it had to run by adding things linearly. I did imporve perfromance by reducing the code length and reduced space by reducing code
"""
