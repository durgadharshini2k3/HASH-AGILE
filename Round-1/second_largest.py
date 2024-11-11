n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
nums = list(map(int, input().split()))

largest = None
second_largest = None

if nums[0] > nums[1]:
    largest = nums[0]
    second_largest = nums[1]

else:
    largest = nums[1]
    second_largest = nums[0]


for i in range(2, n):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]

    elif (nums[i] < largest and nums[i] > second_largest):
        second_largest = nums[i]


print(f"The largest element is {largest}")
print(f"The second largest element is {second_largest}")
