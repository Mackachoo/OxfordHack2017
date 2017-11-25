import csv, sys, os
from BeautifulSoup import BeautifulSoup
from random import randint

disease = {}
svgPath = os.path.abspath('.' + '/static' + '/USmap.svg')
svg = open(svgPath, 'r').read()
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
paths = soup.findAll('path')

pathStyle = "font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:"


for p in paths:
    
    if p['id'] not in ['State_Lines', 'separator']:
        p['style'] = pathStyle + ('#' + hex(randint(0,255))[2:] + hex(randint(0,255))[2:] + hex(randint(0,255))[2:] + ';')

print( soup.prettify() )
