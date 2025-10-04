"""
Q1 : Description Sometimes the data has few duplicate values which will affect the analysis done. In this problem, you will be given a list. You have to find and delete the duplicates and print the updated list with no duplicates.

Input: A list of integers.

Output: A list of integers, with duplicates removed if any.

Sample input: [8, 9, 2, 2, 3, 4, 5, 2]

Sample output: [8, 9, 2, 3, 4, 5]
"""

input_list = [8, 9, 2, 2, 3, 4, 5, 2]
output_list = list(set(input_list))
print(output_list) # Using set to remove duplicates and converting back to list
# Note: The order of elements in the output list may vary since sets do not maintain order.
