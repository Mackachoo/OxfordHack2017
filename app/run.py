from flask import render_template, Flask, request
from json import load
from random import randint
import os, sys, subprocess

jsonlist = load(open("output.json", "r"))
app = Flask(__name__)
elements = []
for key in jsonlist:
    try:
        elements = elements + [jsonlist[key]]
    except:
        raise
        continue
diseaseList = []
for i in range(len(elements)):
    diseaseList = diseaseList + elements[i]["DiseaseList"]
diseaseList = list(set(diseaseList))
print(diseaseList)
raceList = []
for i in range(len(elements)):
    try:
        raceList = raceList + [elements[i]["Race"]]
    except:
        continue
raceList = list(set(raceList))

@app.route('/',methods=['GET', 'POST'])
def print_form():
    if request.method == 'POST':
        
        randcode = randint(0,20)
        static = os.path.abspath('./' + 'static' )
        randcodesvg = static + '/' + str(randcode) + '.svg'
        randcodepng = static + '/' + str(randcode) + '.png'
        sys.path.append(randcodesvg)
        sys.path.append(randcodepng)
        print (randcode)

        result = dict(request.form)
        results = []
        for key in result:
            if result[key] == '':
                continue
            else:
                results = results + result[key]
        result = []
        for i in range(0, len(results)):
            
            if results[i] != '':
                result = result+[results[i]]
        print(result)
        bashCommand = str("python2 mapPlot.py " + str(randcode) + " " + str(result))
        ps = subprocess.call(bashCommand.split())
        return render_template('index.html', elements = {'0':elements}, randcode = randcode, randcodesvg = randcodesvg, diseases = diseaseList, races = raceList, randcodepng = randcodepng)
    if request.method == 'GET':
        return render_template('index.html', elements = {'0':elements}, diseases = diseaseList, races = raceList)

if __name__ == "__main__":
    #for i in jsonlist['Diseases']:
        #print (i['Disease'])
    app.run()