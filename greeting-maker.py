# coding=utf-8
import drawSvg as draw
import random

# Define image size
imageSize = 1024
d = draw.Drawing(imageSize, imageSize, origin='center', displayInline=False)

# Define the colors
colors = ['red', 'green', 'blue', 'black', 'yellow', 'orange']

# Define shape adding function
def shapeMaker(drawing, shapename, color, size, count):
	if shapename == 'square':
		for i in range(count):
			shape = draw.Rectangle(random.randrange(-imageSize/2,imageSize/2,2), random.randrange(-imageSize/2,imageSize/2,2), size, size, fill=color)
			#return shape
			drawing.append(shape)
	elif shapename == 'circle':
		for i in range(count):
			shape = draw.Circle(random.randrange(-imageSize/2,imageSize/2,2), random.randrange(-imageSize/2,imageSize/2,2), size, fill=color)
			#return shape
			drawing.append(shape)

# Make a background
background = draw.Rectangle(-511,-511,1023,1023, fill='#AFEEEE', stroke_width=2, stroke='black')
d.append(background)

# Add shapes
color = random.choice(colors)
shapeMaker(d, 'circle', color, 40, 9)
newlist = colors[:]
newlist.remove(color)
color = random.choice(newlist)
shapeMaker(d, 'square', color, 60, 6)
newlist.remove(color)
color = random.choice(newlist)
shapeMaker(d, 'circle', color, 60, 5)
newlist.remove(color)
color = random.choice(newlist)
shapeMaker(d, 'square', color, 40, 7)

# Add greeting "Happy"
greetingplate1 = draw.Rectangle(-250,150,500,100, fill='white', fill_opacity=0.75, stroke_width=2, stroke='black')
d.append(greetingplate1)
d.append(draw.Text('HAPPY', 85, -140, 170, fill='red'))

# Add greeting "Diwali"
greetingplate2 = draw.Rectangle(-250,0,500,100, fill='white', fill_opacity=0.75, stroke_width=2, stroke='black')
d.append(greetingplate2)
d.append(draw.Text('DIWALI', 80, -150, 20, fill='red'))

# Ask user input of name
nameplate = draw.Rectangle(-250,-150,500,100, fill='white', fill_opacity=0.75, stroke_width=2, stroke='black')
d.append(nameplate)
name = input()
d.append(draw.Text(name, 80, -150, -130, fill='blue'))

# Create and save the greeting card
d.setPixelScale(2)
d.setRenderSize(1024, 1024)
d.savePng('diwali-greeting.png')
