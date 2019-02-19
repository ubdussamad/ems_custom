from PIL import Image, ImageDraw, ImageFont
import time



def genrate_recipt(data):
    image = Image.open('resources/recipt_test.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('DejaVuSansMono.ttf',size=11)
    (x, y) = (10, 90)
    color = 'rgb(0, 0, 0)'
    t_id = 'Transaction Id: %s  |  '%(data['Transaction Id'],)
    d = 'Date: %s'%(data['Date'],)
    bb =   '   Billed by: %s    | '%(data['Billed by'],)
    p = 'Payment Type: %s'%(data['Payment Type'])
    head = 'Product    |    Qty    | Unit    | Rate |   Amount'
    hr = '-'*30
    t = "Total amount: %s"%str(data['Total Amount'])
    draw.text((x, y), t_id+d, fill=color, font=font)
    draw.text((x, y+15),bb+p, fill=color, font=font)
    draw.text((x, y+35),head, fill=color, font=font)
    draw.text((x, y+40),'_'*60, fill=color, font=font)
    y = y+70
    stuff = ['  |  '.join(map(str,i)) for i in data['data']]
    stuff = stuff+[hr,t]
    for i in range(len(stuff)):
        draw.text((x, y+i*30), stuff[i], fill=color, font=font)
    img_name = time.ctime()
    image.save(img_name+'.png')
    image.show()
    return(img_name)
if __name__ == '__main__':
    d={'Client': 0,
 'data': [['GREEN_DARK', '1', 'Kg', '50.0', 50.0],
          ['GREEN_NORMAL', '1', 'Kg', 12.0, 12.0]],
 'Payment Type': 'current',
 'Date': 'Sun Feb 17 17:45:00 2019',
 'Total Amount': 62.0, 'Billed by': 'nouman',
 'Transaction Id': 1550405700}
    genrate_recipt(d)
# draw the message on the background

#draw.text((x, y), message, fill=color, font=font)
##(x, y) = (150, 150)
##name = 'Vinay'
##color = 'rgb(255, 0, 255)' # white color
##draw.text((x, y), name, fill=color, font=font)
##
### save the edited image

#image.save('greeting_card.png')
