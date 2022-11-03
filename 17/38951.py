'''
Назовём парой два идущих подряд элемента последовательности.
Определите количество пар, в которых хотя бы один из двух элементов делится на 3, а их сумма делится на 5.
В ответе запишите два числа: сначала количество найденных пар, а затем – максимальную сумму элементов таких пар.
'''
count = 0
max = 0
f = open('17.txt')
nums = f.readlines()
for i in range(len(nums)):
    nums[i] = int(nums[i])
for i in range(len(nums) - 1):
    if (nums[i] % 3 == 0 or nums[i + 1] % 3 == 0) and (nums[i] + nums[i + 1]) % 5 == 0:
        count += 1
        if nums[i] + nums[i + 1] > max:
            max = nums[i] + nums[i + 1]
print(count, max)





