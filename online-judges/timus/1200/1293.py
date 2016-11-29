input_vars = input().split()

panels = int(input_vars[0])
width = int(input_vars[1])
height = int(input_vars[2])
g_per_m2 = 1

area = width * height
total_area = area * panels * 2 # both sides
total_weight = total_area * g_per_m2

print(total_weight)
