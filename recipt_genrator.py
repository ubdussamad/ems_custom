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
body {text-align:center;font-family: "Fake Receipt", sans-serif }
td,th {padding-right:10px;word-wrap: break-word;max-width: 150px;}
</style>
</head><body align=\'center\'>'''
        postfix_string = '''
<br/><br/>
<b>GRAND TOTAL: </b>%s Rupees
<p align=\'center\' style=\'font-size:10px;\'><b>Note:</b> The grand total amt is inclusive of all taxes.</br>
Incase of any glitch in amount,tax,etcetera, contact the seller.</p>
</body></html>'''%self.data['Total Amount']
        return ( ''.join([prefix_string,text,postfix_string]) )

    
    def render(self):
        #heads = ['data'] if not self.ttype else ['data',] 
        prefix = '''<h3 align=\'center\'>Nordex Dyestuff</h3>
        <p align=\'center\'>Colours, Threads & Chemicals <br/>
        nordex.help@gmail.com |  <b>+91 8707497350</b><br/>
        <b>GSTIN</b>-09BRPPN2I23QIZ4 <br/>
        299/2B Akbari Gate Chowk Lane, Lucknow</p><hr/>'''
        meta_headers = ''.join([''.join(['<h8><b>',keys,'</b></h8>:  ',str(values),
            '<br/>']) for keys,values in self.data.items() if keys != 'data'])
        infix = '<br/><hr/><table align=\'center\'><tr><th>'
        if self.ttype:
            objects = [ [k for j,k in enumerate(i) if j not in [1,4]] for i in self.data['data']]
        else:
            objects = self.data['data']
        print(objects)
        formatter = '<tr><td>'+'</td></tr><tr><td>'.join([ '</td><td>'.join(i) for i in objects])+'</td></tr>'
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
 'data': [['TEST', 'ABCDEFSDFGHJKLDFGJKL', '210.35 Kg', '50.0', '5000.50' , '55000.0' ],
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
