from PIL import Image, ImageOps
import sys
im = Image.open(sys.argv[1])

im1 = im.crop((515,150,700,330))
ima = ImageOps.mirror(im1)
im.paste(ima,(515,150,700,330))
im2 = im.crop((370,370,797,421))
ima1 = ImageOps.flip(im2)
im.paste(ima1,(370,370,797,421))
im3 = im.crop((0,0,190,200)) #RGB layer frfr
# Make transform matrix, to multiply R by 1.1, G by 0.9 and leave B unchanged
# newRed   = 1*oldRed  +  0*oldGreen    +  0*oldBlue  + constant
# newGreen = 0*oldRed    +  0*OldGreen  +  1*OldBlue  + constant
# newBlue  = 0*oldRed    +  1*OldGreen    +  0*OldBlue  + constant
Matrix = ( 1,   0,  0, 0,
           0,   0,  1, 0,
           0,     1,  0, 0)

# Apply transform and save 
im3 = im3.convert("RGB", Matrix) 
im4 = im.crop((0,200,190,410))
im4 = ImageOps.flip(im4)
im.paste(im3,(0,200,190,400))
im.paste(im4,(0,0))
for i in range(5):
    im3 = im.crop((0,399-i,190,400-i))
    im.paste(im3,(0,400+i,190,401+i))
for i in range(5):
    im3 = im.crop(((0,414-i,190,415-i)))
    im.paste(im3,(0,405+i,190,406+i))
im.show()
im.save('jigsolved.jpg')