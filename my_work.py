

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
    if N % 2 == 1:
        print("Please choose an even number for a more accurate drawing, and rerun the program.")
        return
    
    fill_char = input("What character would you like to use to draw the triangle?")

    RATIO = 1/1 
    BOTTOM_LINE = int(N)

    def draw(height: int):
        for i in range(0, height):
            print(fill_char * i)

    draw(N + 1)

draw_right_triangle()

def compound_interest() -> None:
    N = int(input("How much money is your principal? (Money you're starting with)."))
    T = int(input("How long to you plan to leave your money in this acount?"))
 

    for year in range(T):
           N = N * (1 + 0.05)
           print(f"At year {year + 1}, your new balance will be ${N:.2f}")

compound_interest()

def draw_hollow_square() -> None:
    S = int(input("How big do you want the hollow square to be?"))
    T = int(input("How thick do you want the walls to be?"))  
    if T > S // 2:
        print("Please choose a smaller thickness and rerun the program")
        return
    
    fill_char = input("What character do you want to draw the hollow square with?")   
    fill_space = ' '

    def draw_top_bottom(S, T):
        for i in range(T):
        # print T many times
            print(fill_char * S)

    def draw_middle(S, T):
        space = (S - 2*T) * fill_space
        for i in range(T):
            print((fill_char * T) + (space) + (fill_char * T))

    draw_top_bottom(S, T)
    draw_middle(S, T)
    draw_top_bottom(S, T)

draw_hollow_square()


# REFLECTION

"""
1.
I did not constrain the parameter of greet as string, or specify that
another string should be returned. I also did not make it an f-string
and rather just used addition signs to be able to input the name
into the greeting.

I should have specifies the string to string apspect of the function
to clarify that it is made for names and words rather than numbers.

Additionally, using an f-string would probably make the code look cleaner
and easier to read.






"""
