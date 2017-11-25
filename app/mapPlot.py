
def MapPlot(code):
    import csv, sys, os
    from BeautifulSoup import BeautifulSoup
    from random import randint

    disease = {"North Slope, AK" : 1,"Winston, AL": 10, "Sdgdsgdfgdfg" : 1}
    totalnum = 0
    svgPath = os.path.abspath('.' + '/static' + '/USmap.svg')
    svg = open(svgPath, 'r').read()
    soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
    paths = soup.findAll('path')
    pathStyle = "font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:"
    count = 0

    for key in disease:
        print (key)
        totalnum = totalnum + disease[key]
    print ("totalnum = " + str(totalnum))


    for p in paths:
    
        if p['id'] not in ['State_Lines', 'separator']:
            try:
                num = disease[p['inkscape:label']]
            except:
                continue
            x =  (hex(255 - int(25500*num/totalnum)/100)[2:])
            p['style'] = pathStyle + ('#' + x + x + x + ';')    

    write = open((str(code) + '.svg'), 'w+')
    write.write(soup.prettify())
    write.close()

def gay():
    print ("hello\n")
