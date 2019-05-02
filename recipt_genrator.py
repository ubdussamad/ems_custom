# Recipt Genrator for EMS | CUSTOM
# Author: ubdussamad <ubdussamad@gmail.com>

# TODO:
# 1. Genrate temp HTML files
# 2.schedule them for printing

class Render_html:
    def __init__ (self, data , ttype = False ):
        self.data = data;
        self.ttype = ttype;
    def embed_content(self,text):
        prefix_string = '''<html><head><title> Recipt #12345678 </title>
<style>
@font-face {
  font-family: "Kimberley";
  src: url(resources/fake_receipt.ttf) format("truetype");
}
body {width:400px;font-family: "Kimberley", sans-serif }
table {width:400px;}
td,th {padding-right:10px;word-wrap: break-word;
max-width: 100px;}
</style>
</head><body>'''
        postfix_string = '''
<br/>
<b>GRAND TOTAL: </b>%s₹
<p style=\'font-size:10px;\'><b>Note:</b> The grand total amt is inclusive of all taxes.</br>
Incase of any glitch in amount,tax,etcetera, contact the seller.</p>
</body></html>'''%self.data['Total Amount']
        return ( ''.join([prefix_string,text,postfix_string]) )

    
    def render(self):
        prefix = '<h3 align=\'center\'>Nouman Colors</h3>'
        meta_headers = ''.join([''.join(['<h8><b>',keys,'</b></h8>:  ',values,'<br/>']) for keys,values in self.data.items() if keys != 'data'])
        infix = '<br/><table><tr><th>'
        formatter = '<tr><td>'+'</td></tr><tr><td>'.join([ '</td><td>'.join(i) for i in self.data['data']])+'</td></tr>'
        postfix = '</td></tr></table>'
        if not self.ttype:
            head = 'Product</th><th>HSN</th><th>Qty(U)</th><th>Rate/U</th><th>Tax</th><th>Total</th></tr>'
        else:
            head = 'Product</th><th>Qty(U)</th><th>Rate/U</th><th>Total</th></tr>'
        k = ''.join([prefix,meta_headers,infix,head,formatter,postfix])
        z = self.embed_content(k)
        with open('recipt.html','w') as fobj:
            fobj.write(z)
        return(True)
        
  
d={'Client': '0',
 'data': [['TEST', 'ABCDEF', '210.35 Kg', '50.0', '5000.50' , '55000.0' ],
          ['TEST', 'DEF', '1.0 Kg', '12.0', '1.2' ,'13.2' ]],
 'Payment Type': 'current',
 'Date': 'Sun Feb 17 17:45:00 2019',
 'Total Amount': '62.0', 'Billed by': 'nouman',
   'Transaction Id': '1550405700'}

def genrate_recipt(data,ttype = 0):
    rendrer = Render_html(data,ttype)
    rendrer.render()

if __name__ == '__main__':
    print("Unit-Testing: Recipt Generation")
    rendrer = Render_html(d)
    rendrer.render()
    print("Test Completed Sucessfully.")
    print("Result: Passed!")
