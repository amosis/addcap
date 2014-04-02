

python addcap.py -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 620 -fs 60 -sc LOWER_LEFT -ca 9 -o demo0_ -f demo -q "Hello."
python addcap.py -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 620 -fs 30 -tw 25 -sc LOWER_LEFT -ca 8 -o demo1_ -f demo -q "I wrote a little python script to add text and a caption bubble to pictures."
python addcap.py -i "source_1600/cat-like-readiness.jpg" -sx 900 -sy 100 -fs 30 -sc LOWER_LEFT -ca 6 -o demo2_ -f demo -q "Wait, you what?"
python addcap.py -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 620 -fs 30 -tw 25 -sc LOWER_LEFT -ca 8 -o demo3_ -f demo -q "Yeah!  It's a one-liner python script from the CLI that lets you add cartoon style bubbles to pictures."
python addcap.py -i "source_1600/cat-like-readiness.jpg" -sx 900 -sy 100 -fs 30 -sc LOWER_LEFT -ca 6 -o demo4_ -f demo -q "Oh.  Neat!"

python addcap.py -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 620 -fs 30 -tw 25 -sc LOWER_LEFT -ca 8 -o demo5_ -f demo -q "You have 'full' control over where the caption bubble is placed in the picture.  The bubble or the text will probably work."
python addcap.py -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 620 -fs 30 -tw 25 -sc LOWER_LEFT -ca 8 -o demo6_ -f demo -q "Well, it may work."
python addcap.py -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 700 -fs 30 -tw 25 -sc LOWER_LEFT -ca 9 -o demo7_ -f demo -q "If they don't work, you can fiddle with the options until you get it to work.  mostly."

python addcap.py -i "source_1600/cougar.jpg" -sx 200 -sy 800 -fs 30 -sc LOWER_LEFT -ca 2 -o demo8_ -f demo -q "Can I put a caption here?"
python addcap.py -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 700 -fs 30 -tw 25 -sc LOWER_LEFT -ca 9 -o demo9_ -f demo -q "Yes."
python addcap.py -i "source_1600/cougar.jpg" -sx 1150 -sy 170 -fs 25 -sc LOWER_LEFT -ca 7 -o demo10_ -f demo -q "What about here?"
python addcap.py -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 700 -fs 40 -tw 25 -sc LOWER_LEFT -ca 9 -o demo11_ -f demo -q "Yes."
python addcap.py -i "source_1600/cougar.jpg" -sx 0 -sy 1066 -fs 70 -tw 25 -sc LOWER_LEFT -ca 12 -o demo12_ -f demo -q "And if I wanted to, could I put a caption here?"
python addcap.py -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 450 -fs 70 -tw 25 -sc LOWER_LEFT -ca 8 -o demo13_ -f demo -q "ENOUGH"
python addcap.py -i "source_1600/cougar.jpg" -sx 0 -sy 0 -fs 70 -tw 25 -sc LOWER_RIGHT -ca 12 -o demo14_ -f demo -q "This is intentionally off the page for comedic effect."
python addcap.py -i "source_1600/cat-like-readiness.jpg" -sx 0 -sy 0 -fs 70 -tw 25 -sc LOWER_RIGHT -ca 12 -o demo15_ -f demo -q "This is intentionally off the page for comedic effect."

python addcap.py -i "source_1600/cat-like-readiness.jpg" -sx 0 -sy 0 -fs 70 -tw 25 -sc LOWER_RIGHT -ca 12 -o demo15_ -f demo -q "This is intentionally off the page for comedic effect."
python addcap.py -cc 250 -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 700 -fs 30 -tw 25 -sc LOWER_LEFT -ca 9 -o demo16_ -f demo -q "..." "Right now, if you write a long passage, the text and caption will break the bounds of the picture.  I may work it to resize the font and caption until it fits on the page." "If you don't see a caption on your image, then you may have 'gone negative'.  Check your starting corner and caption direction to make sure you are drawing in the right direction." "This script won't modify your original image.  It will create a new one in your same directory, or in a directory you specify." "If you pass multiple quotes in one command, it will handle that too.  Just read the docs."

python addcap.py -cc 250 -i "source_1600/enraged.jpg" -sx 20 -sy 400 -fs 30 -tw 25 -sc UPPER_LEFT -ca 5 -o demo17_ -f demo -q "One question, will the font auto resize to keep the caption bubble small enough to fit within the bounds of the image?"
python addcap.py -cc 250 -i "source_1600/squirrely-smirk.jpg" -sx 800 -sy 700 -fs 30 -tw 25 -sc LOWER_LEFT -ca 9 -o demo18_ -f demo -q "Not yet." "sigh."
python addcap.py -i "source_1600/pugnax.jpg" -sx 580 -sy 290 -fs 30 -tw 25 -sc LOWER_LEFT -ca 5 -o demo19_ -f demo -q "sqkwawk"
