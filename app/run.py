from flask import render_template, Flask, request
from json import load
from random import randint
from time import sleep
import mapPlot

randcode = "gay"
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
        try:
            result = request.form
            mapPlot.gay()
            mapPlot.MapPlot(randcode)
            sleep(1)
        except:
            raise
            pass
        finally:
            return render_template('index.html', elements = {'0':elements}, randcode = randcode)
    if request.method == 'GET':
        return render_template('index.html', elements = {'0':elements})

if __name__ == "__main__":
    for i in jsonlist['Diseases']:
        print (i['Disease'])
    app.run()