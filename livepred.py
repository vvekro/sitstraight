import os                                           #
os.environ["XDG_SESSION_TYPE"] = "xcb"              #
#####################################################

from ultralytics import YOLO

model=YOLO('best.pt')
tempstore = model(source = 0, show=True)
