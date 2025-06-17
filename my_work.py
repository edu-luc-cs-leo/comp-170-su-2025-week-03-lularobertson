

def diamond() -> None:

  
    N = int(input("How wide do you want the diamond to be"))
    if N % 2 == 0:
         print("Please choose an odd number and re-run the program.")
         return

         
    fill_char = input("What character would you like to use to fill the diamond?")
    print(f"Thank you, I will use {fill_char} to draw the diamond of {N} width")


    space_char = ' '
    TOP_SPACE = int((2/5)*int(N))
    MIDDLE_SPACE = int((1/5)*int(N))

    RATIO = 1/1 # height over width
    TOP_LINE = int((1/5)*int(N))
    TOP_MIDDLE_LINE = int((3/5)*int(N))
    MIDDLE_LINE = int(N)

    #centered line
    def draw_line(number_char):
        space_num = (N - number_char) // 2 #calculating space and rounding
        print(space_char * space_num + fill_char * number_char + space_char * space_num) #printing line with the spaces incl.

    draw_line(TOP_LINE)
    draw_line(TOP_MIDDLE_LINE)
    draw_line(MIDDLE_LINE)
    draw_line(TOP_MIDDLE_LINE)
    draw_line(TOP_LINE)

diamond()


def draw_right_triangle () -> None:
    N = int(input("How tall do you want the right triangle to be?"))
    fill_char = input("What character would you like to use to draw the triangle?")

    RATIO = 1/1 
    #height to width. I'm guessing the width will be the same as the height.

    BOTTOM_WIDTH = int(N)
    