
marks = [14,12,18,20,15]
for mark in marks:
    print(mark)
# # expense total using for loop
# total = 0
# for expense in expenses:
#     total = total + expense
# print(total)

# # explain for loop iterations by debugging code

# # range() function
# print(range(1,11))
# print(list(range(1,11)))
# for i in range(1,11):
#     print(i)

# # in monthly expense list print month number, expense and then total
# total = 0
# for i in range(len(expenses)):
#     print(f"Month {i+1}, expense: {expenses[i]}")
#     total += expenses[i]
# print(f"Total expenses is {total}")

# # break
# key_location="chair"
# locations = ["sofa","garage","chair","table","closet"]
# for loc in locations:
#     if loc == key_location:
#         print("Key found at:",loc)
#         break
#     else:
#         print("Key not found in:",loc)