from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
import pdfkit


app = Flask(__name__)

app.config["CLIENT_FILE"]="D:\pyspace\nikhil\flask folder\prowizards project"

@app.route('/')
def takeResponse():
   return render_template('donationform.html')

@app.route('/result',methods = ['POST', 'GET'])
def displayResponse():
    if request.method == 'POST':
        result = request.form
        #entering details into pdf and displaying
        config=pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        pdfkit.from_string(str(result.get("Name")).upper() + ", We Thank you for your contribution as " +str(result.get("Type of Donation"))+" of Amount Rs."+str(result.get("amount")), f"{str(result.get('Name'))+' '+str(result.get('Type of Donation'))+' '+str(result.get('amount'))}.pdf",configuration=config)
        app.config["CACHE_TYPE"] = "null"
        return render_template("displayform.html",result = result)


@app.route('/downloads/<filename>')
def download_file(filename):
    pick=f'D:/pyspace/nikhil/flask folder/prowizards project/{filename}.pdf'
    return send_file(pick,as_attachment=True)

if __name__ == '__main__':
   app.run(debug = False, port = 5000)