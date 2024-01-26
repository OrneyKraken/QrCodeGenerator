import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size =15,border=2)

qr.add_data("https://www.youtube.com/watch?v=APHXbkXHdy0")
qr.make(fit= True)

img = qr.make_image(fill_color= "red",back_color = "black")
img.save("Mr_beast_again.png")





