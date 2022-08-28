# GestureControlled_PPT_Markup_And_Navigation
Markup and navigate ppts using hand gestures.

Navigating and writing on ppts can be a tedious task for lazy people like me. Sometimes we don't have a touchscreen device or a writing tablet, because they can be too costly. So I thought why can't I make something which solves both purposes, and makes you feel as if you are using a touchscreen device.

This program uses your hand gestures to change the slides and uses your fingers to point and mark on those slides.

What this program basically does is that it uses 3D landmarks using cvzone's HandTrackingModule to detect and track the users hand and identify postion of the fingers.

After identifying the position of certain fingures(like index, thumb etc.) the program switches between slides, moves a pointer on a slide, and write in the file.

### Modules and Dependencies:

```import os
from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np
```



### Challenges faced:
1)The program works only on each slide downloaded as an image. It can not directly work on .ppt files.

2)Initially two completely diffrent drawings would join automatically, i.e. a line will automatically appear between the end point of the previous drawing and the starting point of the next one. **Fix:** store every drawing as a separate array.

3)The drawings from the previous slides will remain on the window even after slides change. **Fix:** Clearing out the next slide by restarting the list of annotations/drawings on every slide.

### Gestures used:

1) **Index finger and middle finger:** Using the pointer.
2) **Index finger:** For markup.
3) **Pinky finger:** For going to the next slide.
4) **Thumbs:** To move to the previous slide.
5) **First Three fingers:** Erasing. The last annotation goes first.

### Reference:
https://www.youtube.com/watch?v=CKmAZss-T5Y
