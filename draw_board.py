def draw_board():
    size = int(input("enter the size of the board."))
    x = 1
    while x <= size:
        print("---"*size + "\n" + "/ /"*size)
        x += 1
    print("---"*size)

if __name__ == "__main__":
    draw_board()
    input()

