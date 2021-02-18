'''
BOX_FUNCTION
------------
Write a function called box that will output boxes (made of lower case o's) 
given a height and width. Once you've finished writing your function, copy 
and paste the following code after it and make sure it works with the function you wrote:

INPUT
-----
box(7,5) # Print a box 7 high, 5 across
print() # Blank line
box(3,2) # Print a box 3 high, 2 across
print() # Blank line
box(3,10) # Print a box 3 high, 10 across

OUTPUT
------
ooooo
ooooo
ooooo
ooooo
ooooo
ooooo
ooooo

oo
oo
oo

oooooooooo
oooooooooo
oooooooooo
'''


def box(h, w):
    for i in range(h):
        print("o"*w)


def main():
    box(7, 5)  # Print a box 7 high, 5 across
    print()  # Blank line
    box(3, 2)  # Print a box 3 high, 2 across
    print()  # Blank line
    box(3, 10)  # Print a box 3 high, 10 across


if __name__ == '__main__':
    main()
