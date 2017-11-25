import csv, sys, os
from BeautifulSoup import BeautifulSoup
from random import randint

disease = {}
svgPath = os.path.abspath('.' + '/static' + '/USmap.svg')
svg = open(svgPath, 'r').read()
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
paths = soup.findAll('path')

pathStyle = "font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:"
count = 0

for p in paths:
    
    if p['id'] not in ['State_Lines', 'separator']:
        count = (count+4)%254
        p['style'] = pathStyle + ('#' + hex(count)[2:] + '0000;')

print( soup.prettify() )
