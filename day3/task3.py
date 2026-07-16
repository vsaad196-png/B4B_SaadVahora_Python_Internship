#You are given a list of 15 random integers between 1 and 100. Remove all duplicate values while keeping the original order of first appearance. Do not use set() for this task, write your own loop based logic.
lists=["11","12","10","11","11","18","10","18"]
unique_order=[]
for page in lists:
    if page not in unique_order:
        unique_order.append(page)
print(unique_order)
