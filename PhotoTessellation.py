from PIL import Image

#Program works best for Black and White pictures over colored pics... Will work on improvement - perhaps mode of colors instead of average?


im = Image.open("bridgenight.jpg").convert("RGB")

im.show()

(width,height) = im.size #in pixels
total_images = 100*100

#row is y and col is x
#makes a 2D Array with values of each pixel.

#we want to have total_images in the tesselation so take each image and divide by sqrt(total_images)
sm_width = int((width/(total_images**(.5))))
sm_height = int((height/(total_images**(.5))))

im_matrix = im.load()

tess_color_matrix = [[]]

for pic_r in range(0,int(round(total_images**(.5)))):
    for pic_c in range(0,int(round(total_images**(.5)))):

        avg_r = 0
        avg_g = 0
        avg_b = 0

        #processes average rgb per smaller image
        for col in range(0,sm_width):
            for row in range(0,sm_height):
                count = col*sm_height+row
                (r,g,b) = im_matrix[col+pic_c*sm_width,row+pic_r*sm_height]
                avg_r = int((avg_r*count+r)/(count+1))
                avg_g = int((avg_g*count+g)/(count+1))
                avg_b = int((avg_b*count+b)/(count+1))

        tess_color_matrix.append((avg_r,avg_b,avg_g))



new_width = int(width*(total_images**(.5)))
new_height = int(height*(total_images**(.5)))

new_im = Image.new('RGB', (new_width,new_height))
for y in range(0,new_height,height):
    for x in range(0,new_width,width):
        color = tess_color_matrix.pop()

        layer = Image.new('RGB',(width,height), color) # This will be the tint (remove for only blur)
        output = Image.blend(im, layer, 0.8)     # This will tint the image to the correct hue (remove for only blur)
        # larger numbers (close to 1) here  ^  make the image sharper and appear less blurry
        #box is (left,upper,right,lower) which means upperleft coordinate lowerright
        new_im.paste(output,(x,y,x+width,y+height))#change output for color if you only want the blur

#up to this point the program just return the image with a slight blur added to it


new_im.rotate(180).show()

print("Finished!")
