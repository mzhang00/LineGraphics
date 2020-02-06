from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    # FIX THIRD LINE NOT SHOWING
    B = x1 - x0
    m = A/B
    # FIX POTENTIAL DIVISION BY ZERO ERRORS HERE
    if (m > 0 and m <= 1):
    # if (A > 0 and A <= B):
        B *= -1
        d = 2 * A + B
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A
    # FINISH THIS BELOW AT HOME!!!!!
    # if (A > B):
    #     B *= -1
    #     d = 2 * B + A
    #     while y <= y1:
    #         plot(screen, color, x,y)
    #         if d < 0:
    #             x += 1
    #             d += B
    #         x += 1
    #         d += A
