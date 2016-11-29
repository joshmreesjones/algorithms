numbers = [int(num) for num in input().split()]

harry = numbers[0]
larry = numbers[1]
total_cans = harry + larry - 1

print("%d %d" % (total_cans - harry, total_cans - larry))
