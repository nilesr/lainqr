import PIL.Image
base = PIL.Image.open("base.png")
star = PIL.Image.open("star-ripped.png")
overlay = PIL.Image.new("RGBA", (base.width * star.width, base.height * star.height), (0,0,0,255))
for x in range(overlay.width):
    for y in range(overlay.height):
        basecolor = base.getpixel((int(x/star.width), int(y/star.height)))
        if basecolor == (255,0,0):
            bow = 0 # Hard black (red)
            color = (94,71,103,240)
        elif basecolor == (0,0,255):
            bow = 1 # Hard white (blue)
            color = (233,229,222,240)
        elif basecolor == (0,0,0):
            bow = 2 # Soft black
            color = (94,71,103, 255 - star.getpixel((x % star.width, y % star.height))[0])
        else:
            bow = 3 # Soft white
            color = (233,229,222, 255 - star.getpixel((x % star.width, y % star.height))[0])
        overlay.putpixel((x,y), color)

overlay.save("overlay.png")
