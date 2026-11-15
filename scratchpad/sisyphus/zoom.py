import os, sys
from PIL import Image
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "sisyphus-frames")) + "/"
ids=[int(x) for x in sys.argv[1:]]
Z=14
W=60
sheet=Image.new("RGB",(W*Z*2+10,(36*Z//1)*((len(ids)+1)//2)//1//1 if False else 36*Z*((len(ids)+1)//2)),(170,170,170))
for k,i in enumerate(ids):
    im=Image.open(OUT+f"sisyphus-frame-{i}.png")
    # crop around man
    px=im.load()
    xs=[x for x in range(100) for y in range(36) if px[x,y][3]>0 and y<28]
    c=im.crop((0,0,W,36)) if i<3 else im.crop((max(0,i*7-6),0,max(0,i*7-6)+W,36))
    c=c.resize((W*Z,36*Z),Image.NEAREST)
    sheet.paste(c,((k%2)*(W*Z+10),(k//2)*36*Z),c)
sheet.save("zoom.png")
