from PIL import Image
# img link
img = Image.open(f"./logo.png")
dimensions = [192,512,192,512,60,76,120,152,180,16,32,144,150]
names = ['android-chrome-','android-chrome-','android-chrome-maskable-','android-chrome-maskable-','apple-touch-icon-','apple-touch-icon-','apple-touch-icon-','apple-touch-icon-','apple-touch-icon-','favicon-','favicon-','msapplication-icon-','mstile-']

for i in range(0,13):
    newsize = (dimensions[i],dimensions[i]) 
    img_resize = img.resize(newsize) 
    img_resize.save(f'./icons/{names[i]}{dimensions[i]}x{dimensions[i]}.png')
    
img = Image.open(f"./logo.png")
newsize = (60,60) 
img_resize = img.resize(newsize) 
img_resize.save(f'./icons/apple-touch-icon.png')