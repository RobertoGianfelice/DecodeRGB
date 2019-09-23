LarghezzaImg=400
AltezzaImg=500

def setup():
    global immagine
    immagine=loadImage("DivinaCommedia.tiff")

    size(LarghezzaImg,AltezzaImg)

    noLoop()


def draw():
    immagine.loadPixels()
    car=0
    frase=""
    loc=0
    larg=immagine.width
    altez=immagine.height

    while (loc<larg*altez):
        r=red(immagine.pixels[loc])
        g=green(immagine.pixels[loc])
        b=blue(immagine.pixels[loc])
        frase=frase+chr(int(r))+chr(int(g))+chr(int(b))
        if len(frase)>160:
            print (frase)
            frase=""   
        loc+=1
    print("fine")
    image(immagine,0,0)
