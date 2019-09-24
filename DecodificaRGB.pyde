def setup():
    size(1000,1000)

    global immagine
    immagine=loadImage("Frase.tiff")

    decode()


def decode():
    patchwork=True

    immagine.loadPixels()
    frase=""
    pixel=0
    larg=immagine.width
    altez=immagine.height
    print(larg,altez)
    while (pixel<larg*altez):
        print(pixel)

        r=red(immagine.pixels[pixel])
        g=green(immagine.pixels[pixel])
        b=blue(immagine.pixels[pixel])
        frase=frase+chr(int(r))+chr(int(g))+chr(int(b))
        if len(frase)>160:
            print (frase)
            frase=""   
        
        if patchwork:
            pixel+=100
            if (pixel%larg==0):
                pixel=pixel+larg*99
        else:
            pixel+=1
    
    print (frase)

    image(immagine,0,0)
