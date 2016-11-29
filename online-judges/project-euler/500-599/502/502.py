# Project Euler problem 502
# Josh Rees-Jones
# https://projecteuler.net/problem=502
#
# We define a block to be a rectangle with a height of 1 and an integer-valued
# length. Let a castle be a configuration of stacked blocks.
#
# Given a game grid that is w units wide and h units tall, a castle is generated
# according to the following rules:
#
# 1. Blocks can be placed on top of other blocks as long as nothing sticks out past
#		the edges or hangs out over open space.
# 2. All blocks are aligned/snapped to the grid.
# 3. Any two neighboring blocks on the same row have at least one unt of space
#		between them.
# The bottom row is occupied by a block of length w.
# 5. The maximum achieved height of the entire castle is exactly h.
# 6. The castle is made from an even number of blocks.
#
# The following is a sample castle for w = 8 and h = 5:
#
#	░░█░░░█░
#	░░█░░░██
#	░██░█░██
#	█████░██
#	████████
#
# Let F(w, h) represent the number of valid castles, given grid parameters w and h.
#
# For example, F(4, 2) = 10, F(13, 10) = 3729050610636, F(10, 13) = 37959702514,
# and F(100, 100) mod 1000000007 = 841913936.
#
# Find F(10^12, 100) + F(10000, 10000) + F(100, 10^12)) mod 1000000007.

def F(w, h):
	countRow([1 for cell in w], h - 1);

def countRow(base, height):
	if (h == 1):
		# we are at the top level - make sure the number of blocks is even
	# you can only pass a new row with 1 block in it if:
	#	- the total number of blocks in the base is even and height is even
	#	- the total number of blocks in the base is odd and height is odd
	# in other words, if numBlocks % 2 == height % 2
