n = int(input())

knights = []

for i in range(n):
    knights.append(input())

for knight in knights:
    total = None

    if (knight[0] in "cdef") and (knight[1] in "3456"):
        # in center
        total = 8

    else:
        # not in center

        if (knight[0] not in "ah") and (knight[1] not in "18"):
            # in inner ring

            if knight[0] in "bg" and knight[1] in "27":
                # inner ring corner
                total = 4
            else:
                # inner ring edge
                total = 6

        elif knight[0] in "ah" and knight[1] in "18":
            # outer ring corner
            total = 2

        elif ((knight[0] in "bg") and (knight[1] in "18")) or ((knight[0] in "ah") and (knight[1] in "27")):
            # outer ring corner edge
            total = 3

        else:
            # outer ring edge
            total = 4

    print(total)
