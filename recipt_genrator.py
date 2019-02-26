from PIL import Image, ImageDraw, ImageFont
import time

# Config Style
#Font Location|size|
with open('resources/recipt.config') as file:
    font_data = file.read()
    font_data = font_data.strip('\n').split('|')
def f(x):
    try:
        return('%.1f'%float(x))
    except:
        return( (x+' '*13)[:14] if len(x) > 4 else x)
def genrate_recipt(data ,ttype  = 0):
    image = Image.open('resources/recipt_test.png')
    draw = ImageDraw.Draw(image)
    print(font_data[0])
    font = ImageFont.truetype(font_data[0] , size = int(font_data[1]))
    (x, y) = (10, 90)
    color = 'rgb(0, 0, 0)'
    t_id = 'Transaction Id: %s  | '%(data['Transaction Id'],)
    d = 'Date: %s'%(data['Date'],)
    bb =   '   Billed by: %s    | '%(data['Billed by'],)
    p = 'Payment Type: %s'%(data['Payment Type'])
    head = 'Product        |  HSN  | Qty(U) | Rate/U | Tax | Total '
    if ttype:
        head = 'Product        |  Qty  | Rate | Total '
    hr = '-'*30
    t = "Grand total amount: %s"%data['Total Amount']
    draw.text((x, y), t_id+d, fill=color, font=font)
    draw.text((x, y+15),bb+p, fill=color, font=font)
    draw.text((x, y+35),head, fill=color, font=font)
    draw.text((x, y+40),'_'*60, fill=color, font=font)
    y = y+70
    stuff = ['    '.join(map(f,i)) for i in data['data']]
    dec = 'Note: The grand total amt is inclusive of all taxes.'
    dec1 = 'Incase of any glitch in tax, contact the seller.'
    stuff = stuff+[hr,t,dec,dec1]
    for i in range(len(stuff)):
        draw.text((x, y+i*30), stuff[i], fill=color, font=font)
    img_name = str(data['Transaction Id'])
    image.save(img_name+'.png')
    if int(font_data[4]):
        image.show()
    return(img_name)
if __name__ == '__main__':
    d={'Client': 0,
 'data': [['GREEN_DARK', '1', 'Kg', '50.0', '5' , '55.0' ],
          ['GREEN_NORMAL', '1', 'Kg', '12.0', '1.2' ,'13.2' ]],
 'Payment Type': 'current',
 'Date': 'Sun Feb 17 17:45:00 2019',
 'Total Amount': 62.0, 'Billed by': 'nouman',
 'Transaction Id': 1550405700}
    genrate_recipt(d)
