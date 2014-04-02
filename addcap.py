from __future__ import print_function
import os, sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageOps
import textwrap
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--img', help='Image to add a caption to.', default='source_1600/cat-like-readiness.jpg')
parser.add_argument('-sx','--startX', type=int, help='Starting X Coordinate for caption bubble.', default=900)
parser.add_argument('-sy','--startY', type=int, help='Starting Y Coordinate for caption bubble.', default=100)
parser.add_argument('-tw','--textWrapWidth', type=int, help='How many characters before a line wrap in the bubble?', default=40)
parser.add_argument('-fs','--fontSize', type=int, help='Font size', default=30)
parser.add_argument('-cc','--characterCount', type=int, help='Character count.  limited to 140 by default.', default=140)
parser.add_argument('-sc','--startingCorner', help='The corner that your start coordinates create.  Values are Values are UPPER_LEFT, LOWER_LEFT, LOWER_RIGHT, UPPER_RIGHT', default="LOWER_LEFT")
parser.add_argument('-ca','--calloutArrow', type=int, help='Which call out arrow do you want, starting at 11oclock, going counter clockwise.  Just put the number, like 6', default=6)
parser.add_argument('-f','--folder', help='If defined, create a folder and store addcap images there.  Otherwise defaults to current folder.', default='.')
parser.add_argument('-o','--outfile', help='The outfile prefix name.  Will append a number and JPG to the end.', default='addcap_out')
parser.add_argument('-qf','--quoteFile', help='A file with 1 quote per line.  Quotes should not exceed 140 characters.')
parser.add_argument('-q','--quote', nargs='+', help='One or more quotes in the form "This is a quote.", "This is another quote", "This is yet another quote". 	Individual quotes should not exceed 140 characters. ', default=["Very. . .Very. . .Try it!", "kick wall and talking?", "Sit in das cheyer?"])
args = parser.parse_args()

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.ERROR)

BACKGROUND = (255, 255, 255) #white
FOREGROUND = (0,0,0) #black
OUTLINE = FOREGROUND

FOLDER = str(args.folder)

try: 
    os.makedirs(FOLDER)
    logging.debug('Checking if folder [%s] exists - if not, create it.', FOLDER )
except OSError as e:
    if not os.path.isdir(FOLDER):
        logging.error('Error %s: Folder [%s] did not exist or was not created.', e,  FOLDER )
        raise

INFILE_IMAGENAME = str(args.img)
OUTFILE_IMAGENAME = str(args.outfile)
OUTFILE_TYPE =".gif"
X_BUBBLE_START = args.startX
Y_BUBBLE_START = args.startY
BUBBLE_MAX_WIDTH = 900
BUBBLE_MAX_HEIGHT = 230

START_POINT_ON=str(args.startingCorner)
CALLOUT_ARROW = args.calloutArrow
'''
POSSIBLE CALLOUT ARROWS - backwards around the clock.

    ____
10) <
9) <---

8) <___


7) v---
6) -v- 
5) --v

4) __>
3) -->
  ___
2)   >

1) --^
12) -^-
11) ^--
'''
#print(str(args.quote))
captions = args.quote

#CAPTION SPECIFIC VALUES
FONTFACE = "/opt/X11/share/fonts/TTF/VeraBd.ttf"
FONTSIZE = args.fontSize
MAXCAPTIONLENGTH = args.characterCount
CAPTIONWRAPWIDTH = args.textWrapWidth
CAPTIONWRAPLINEHEIGHT = FONTSIZE + 10
X_CAPTIONTEXTOFFSET = 25
Y_CAPTIONTEXTOFFSET = 25

# Set the font size/face to use.
try:
	font = ImageFont.truetype(FONTFACE, FONTSIZE)
	logging.debug('Font Face (size): %s (%s)', FONTFACE, FONTSIZE)
except (AttributeError, IOError):
	font = None



def drawCaptionBubble(draw, startX, startY, capWidth, capHeight, calloutArrow):
	upper_left = startX, startY
	lower_left = startX, startY+capHeight
	lower_right = startX+capWidth,startY+capHeight
	upper_right = startX+capWidth, startY
	#LEFT SIDE CALLOUTS
	if(calloutArrow == 10):
		ca_1_1 = startX, startY+10
		ca_1_2 = startX-15, startY+20
		ca_1_3 = startX, startY+30
	elif(calloutArrow == 9):
		ca_1_1 = startX, startY+(capHeight/2)-10
		ca_1_2 = startX-15, startY+(capHeight/2)
		ca_1_3 = startX, startY+(capHeight/2)+10
	elif(calloutArrow == 8):
		ca_1_1 = startX, startY+capHeight -30
		ca_1_2 = startX-15, startY+capHeight-20
		ca_1_3 = startX, startY+capHeight-10
	else:
		ca_1_1 = startX, startY
		ca_1_2 = startX, startY
		ca_1_3 = startX, startY
	#BOTTOM SIDE CALLOUTS	
	if(calloutArrow == 7):
		ca_2_1 = startX+10, startY+capHeight
		ca_2_2 = startX+20, startY+capHeight+15
		ca_2_3 = startX+30, startY+capHeight
	elif(calloutArrow == 6):
		ca_2_1 = startX+(capWidth/2)-10, startY+capHeight
		ca_2_2 = startX+(capWidth/2), startY+capHeight+15
		ca_2_3 = startX+(capWidth/2)+10, startY+capHeight
	elif(calloutArrow == 5):
		ca_2_1 = startX+(capWidth)-30, startY+capHeight
		ca_2_2 = startX+(capWidth)-20, startY+capHeight+15
		ca_2_3 = startX+(capWidth)-10, startY+capHeight
	else:
		ca_2_1 = startX, startY+capHeight
		ca_2_2 = startX, startY+capHeight
		ca_2_3 =startX, startY+capHeight	
	#RIGHT SIDE CALLOUTS	
	if(calloutArrow == 4):
		ca_3_1 = startX+capWidth,startY+capHeight-10
		ca_3_2 = startX+capWidth+15, startY+capHeight-20
		ca_3_3 = startX+capWidth, startY+capHeight-30
	elif(calloutArrow == 3):
		ca_3_1 = startX+capWidth,startY+(capHeight/2)+10
		ca_3_2 = startX+capWidth+15, startY+(capHeight/2)
		ca_3_3 = startX+capWidth, startY+(capHeight/2)-10
	elif(calloutArrow == 2):
		ca_3_1 = startX+capWidth,startY+30
		ca_3_2 = startX+capWidth+15, startY+20
		ca_3_3 = startX+capWidth, startY+10
	else:
		ca_3_1 = startX+capWidth,startY+capHeight
		ca_3_2 = startX+capWidth,startY+capHeight
		ca_3_3 = startX+capWidth,startY+capHeight		
		
	#TOP SIDE CALLOUTS	
	if(calloutArrow == 1):
		ca_4_1 = startX+capWidth-10, startY
		ca_4_2 = startX+capWidth-20, startY-15
		ca_4_3 = startX+capWidth-30, startY
	elif(calloutArrow == 12):
		ca_4_1 = startX+(capWidth/2)+10, startY
		ca_4_2 = startX+(capWidth/2), startY-15
		ca_4_3 = startX+(capWidth/2)-10, startY
	elif(calloutArrow == 11):
		ca_4_1 = startX+30, startY
		ca_4_2 = startX+20, startY-15
		ca_4_3 = startX+10, startY
	else:
		ca_4_1 = startX, startY
		ca_4_2 = startX, startY
		ca_4_3 = startX, startY	
	
	captionBubble = tuple(
						upper_left + 
						ca_1_1 +
						ca_1_2 +
						ca_1_3 +
						lower_left + 
						ca_2_1 +
						ca_2_2 +
						ca_2_3 +
						lower_right + 
						ca_3_1 +
						ca_3_2 +
						ca_3_3 +
						upper_right +
						ca_4_1 +
						ca_4_2 +
						ca_4_3 + 
						upper_left)
	#print("Printing this bubble: " + str(captionBubble))
	logging.debug('Printing this bubble: %s ', str(captionBubble))
	draw.polygon(captionBubble, fill=BACKGROUND, outline=OUTLINE)

def writeCaptionToImage(draw, caption, textStartX, textStartY):
	draw.text((textStartX, textStartY), caption, font = font, fill = FOREGROUND)
	#print("Printing text starting at: (" + str(textStartX) + ", " + str(textStartY) + ")" )
	logging.debug('Printing text starting at: (%s, %s) ', str(textStartX), str(textStartY))
	
i = 0;

for caption in captions:
# Open the file to draw on.
	try:
		x = Image.open(INFILE_IMAGENAME)
		draw = ImageDraw.Draw(x)
	except IOError as e:
		logging.error("Error %s: Unable to open %s", e, INFILE_IMAGENAME)
		break
		
	if(caption.__len__() > MAXCAPTIONLENGTH):	
		logging.error('--------FAILED--------------')
		logging.debug(caption)
		logging.error('Length in characters: %s.  That is too long.  Exiting.', str(caption.__len__()))
		
		break	
	else:
		logging.debug('----------------------')
		logging.debug('['+caption+']')
		logging.debug('Length in characters: %s', str(caption.__len__()))
		text_width, text_height = font.getsize((caption))
		logging.debug('TEXT Dimensions are:  %s pixels wide by %s pixels high.', str(text_width), str(text_height))
		#figure out how big to make the box starting from lower left.
		
		lines = textwrap.wrap(caption, width = CAPTIONWRAPWIDTH)			
		longest_line = 0
		total_text_height = 0
		for line in lines:
			# Write the caption to the bubble (kindof.)
			text_width, text_height = font.getsize((line))
			logging.debug('LINE Dimensions are:  %s pixels wide by %s pixels high.', str(text_width), str(text_height))
			total_text_height += text_height+Y_CAPTIONTEXTOFFSET
			if(text_width > longest_line):
				longest_line = text_width
		
		if(START_POINT_ON == "LOWER_RIGHT"):			
			sX = X_BUBBLE_START-(longest_line + (2*X_CAPTIONTEXTOFFSET))
			sY = Y_BUBBLE_START-(total_text_height + (Y_CAPTIONTEXTOFFSET))
			cW = longest_line + (2*X_CAPTIONTEXTOFFSET)
			cH = total_text_height + (Y_CAPTIONTEXTOFFSET)
			y_text = sY + Y_CAPTIONTEXTOFFSET
		elif(START_POINT_ON == "UPPER_RIGHT"):
			sX = X_BUBBLE_START-(longest_line + (2*X_CAPTIONTEXTOFFSET))
			sY = Y_BUBBLE_START+(total_text_height + (Y_CAPTIONTEXTOFFSET))
			cW = longest_line + (2*X_CAPTIONTEXTOFFSET)
			cH = total_text_height + (Y_CAPTIONTEXTOFFSET)
			y_text = sY + Y_CAPTIONTEXTOFFSET
		elif(START_POINT_ON == "UPPER_LEFT"):
			sX = X_BUBBLE_START
			sY = Y_BUBBLE_START
			cW = longest_line + (2*X_CAPTIONTEXTOFFSET)
			cH = total_text_height + (Y_CAPTIONTEXTOFFSET)
			y_text = sY + Y_CAPTIONTEXTOFFSET
		else: #If no value, or improper value, assume UPPER_LEFT
			sX = X_BUBBLE_START
			sY = Y_BUBBLE_START-(total_text_height + (Y_CAPTIONTEXTOFFSET))
			cW = longest_line + (2*X_CAPTIONTEXTOFFSET)
			cH = total_text_height + (Y_CAPTIONTEXTOFFSET)
			y_text = sY + Y_CAPTIONTEXTOFFSET
			
		# Draw the caption bubble to fill in.	
		drawCaptionBubble(draw, sX, sY, cW, cH, CALLOUT_ARROW)
		logging.debug('Bubble size in pixels:  %s pixels wide by %s pixels high.', str(cW), str(cH))

		for line in lines:
			# Write the caption to the bubble (kindof.)
			writeCaptionToImage(draw, line, sX+X_CAPTIONTEXTOFFSET, y_text)
			y_text += text_height+15
			# Save the picture out.
			try:
				logging.debug("Attempting to save %s to %s folder.", OUTFILE_IMAGENAME, FOLDER)
				x.save(FOLDER+"/"+OUTFILE_IMAGENAME+str(i)+OUTFILE_TYPE)
			except IOError as e:
				logging.error("Error %s: Unable to save %s to %s folder.  Aborting the process and calling my mommy.", e, OUTFILE_IMAGENAME, FOLDER)
		
		logging.debug('Text size in pixels (wrapped): %s pixels wide by %s pixels high.', str(longest_line), str(total_text_height))

	i+=1;

	
	
	
