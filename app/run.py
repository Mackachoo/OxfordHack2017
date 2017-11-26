from flask import render_template, Flask, request
from json import load
from random import randint
import os, sys, subprocess

randcode = randint(0,20)
static = os.path.abspath('./' + 'static' )
randcodestat = static + '/' + str(randcode) + '.svg'
sys.path.append(randcodestat)
print (randcode)
jsonlist = load(open("template.json", "r"))
app = Flask(__name__)
elements = []
for elem in jsonlist['Diseases']:
    try:
        elements = elements + [elem]
    except:
        raise
        continue

@app.route('/',methods=['GET', 'POST'])
def print_form():
    if request.method == 'POST':
        result = request.form
        bashCommand = str("python2 mapPlot.py " + str(randcode))
        ps = subprocess.call(bashCommand.split())
        return render_template('index.html', elements = {'0':elements}, randcode = randcode, randcodestat = randcodestat)
    if request.method == 'GET':
        return render_template('index.html', elements = {'0':elements})

if __name__ == "__main__":
    #for i in jsonlist['Diseases']:
        #print (i['Disease'])
    app.run()