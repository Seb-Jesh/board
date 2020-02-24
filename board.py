def playingBoard(row, clmn):
    for row in range(row):  # 0,1,2,3,4,5
        if row % 2 == 0:
            for col in range(clmn):  # 0,1,2,3,4,5
                if col % 2 == 0:
                    if col != clmn - 1:
                        print("❤", end=" ")  # continues to print on the same line
                    else:
                        print("❤")
                else:
                    print("🌹", end=" ")
        else:
            print("=============")
playingBoard(6,5)