##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='black')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

drawpad.create_rectangle(300,300,500,500, fill = 'red')
drawpad.create_line(300,300,400,200, fill = 'blue')
drawpad.create_line(400,200,500,300, fill = 'blue')
drawpad.create_rectangle(320,320,370,370, fill = 'purple')
drawpad.create_rectangle(430,390,480,340, fill = 'blue')
drawpad.create_rectangle(400,460,420,500, fill = 'blue')
drawpad.create_line(350,250,350,190, fill = 'yellow')
drawpad.create_line(350,190,420,190, fill = 'yellow')
drawpad.create_line(420,190,420,220, fill = 'yellow')
root.mainloop()
