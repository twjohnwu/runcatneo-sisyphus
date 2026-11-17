from PIL import Image, ImageChops
import os, sys
V = sys.argv[1] if len(sys.argv) > 1 else 'sisyphus'
O = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # repo root
fr=[Image.open(f'{O}/{V}-frames/{V}-frame-{i}.png').convert('RGBA') for i in range(18)]
for i,f in enumerate(fr):
    px=list(f.getdata())
    bad=[p for p in px if p[3]>0 and p[:3]!=(0,0,0)]
    top=[f.getpixel((x,0)) for x in range(f.width) if f.getpixel((x,0))[3]>0]
    print(i,f.size,'nonblack',len(bad),'tl',f.getpixel((0,0))[3],'toprow',len(top),'opaque',sum(1 for p in px if p[3]>0))
for i in range(18):
    j=(i+1)%18
    if fr[i].tobytes()==fr[j].tobytes(): print('IDENT',i,j)
a=Image.open(O+f'/{V}-preview.png')
print(a.size,a.format,a.n_frames,a.info.get('interlace'),getattr(a,'is_animated',None))
for n in range(a.n_frames):
    a.seek(n); d=a.convert('RGBA')
    if d.tobytes()!=fr[n].tobytes(): print('APNG mismatch',n)
print('apng done')
