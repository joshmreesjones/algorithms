# Solves an assigned CSC113 problem to find the quadrant an angle
# is in without using else if constructs.
# By Josh Rees-Jones

angle1 = 0
angle2 = 45
angle3 = 90
angle4 = 135
angle5 = 180
angle6 = 225
angle7 = 270
angle8 = 315
angle9 = 360
angle10 = 39487583745

def find_quadrant(angle):
	angle %= 360

	# instructions say to only use nested conditional statements
	if angle >= 0:
		if angle >= 90:
			if angle >= 180:
				if angle >= 270:
					return 4
				return 3
			return 2
		return 1

	# in case something weird happens
	return None

print(find_quadrant(angle1))
print(find_quadrant(angle2))
print(find_quadrant(angle3))
print(find_quadrant(angle4))
print(find_quadrant(angle5))
print(find_quadrant(angle6))
print(find_quadrant(angle7))
print(find_quadrant(angle8))
print(find_quadrant(angle9))
print(find_quadrant(angle10))
