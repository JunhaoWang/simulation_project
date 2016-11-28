from lxml import etree
from bs4 import BeautifulSoup as Soup
import numpy as np
import math
import time
import matplotlib.pyplot as plt
import random

def genSin(avg , amp, angfre, pha, num):
	"""
	generate array of sinwave values from:
	1. average of siwave values (avg)
	2. amplitude of sinwave (amp)
	3. angular frequency - radians/second (angfre)
	4. phase - radians (pha)
	5. number of data points (num)
	"""
	result = []
	for i in range(num):
		result.append(avg + amp * math.sin(angfre * i + pha))
	return result

def genMultiSin(avg = 20, amp = 10, angfre = 0.1, num= 100, complexity = 10):
	"""
	generate a concatenation of sinwaves to approximate random variation from:
	1. all inputs except for pha in genSin()
	2. number of sinwaves (complexity)
	"""
	amp *= complexity/2
	allW = []
	for i in range(complexity):
		newangfre = angfre * random.random()
		allW.append(genSin(avg, amp * random.random(), newangfre, newangfre * random.random() * complexity, num))
	result = allW[0]
	for i in allW[1:]:
		for ind, j in enumerate(i):
			result[ind] += j
	return [i/complexity for i in result]

def genPoint(name, loc, speed):
	"""
	generate a wayPoint from:
	1. name of point (name)
	2. location of point (loc)
	3. max speed of point (speed)
	"""
	defPoint = """
	<wayPoint id="WayPoint_1">
      <translation>
         <vector jtype="java_lang_Float" size="2">
            <entry>2.2045</entry>
            <entry>-0.35273</entry>
            <entry>6925</entry>
         </vector>
      </translation>
      <speed>730.9434</speed>
   </wayPoint>
	"""
	soup = Soup(defPoint,'xml')
	soup.wayPoint['id'] = name
	soup.findAll('entry')[2].string = str(loc)
	soup.speed.string  = str(speed)
	[s.extract() for s in soup('?xml')]
	return soup.wayPoint


def plotSpeed(x, y):
	plt.plot(x, y)
	plt.xlabel('location')
	plt.ylabel('speed')
	plt.savefig('speed_profile.png')
	plt.close()

def insertPoints(soup, points):
	for i in soup.find('traffic').find('vehicle').findAll('wayPoint'):
		i.replaceWith('')
	for p in points:
		soup.find('traffic').find('vehicle').wayPoints.append(p)
	return soup


soup = Soup(open('/Users/juwang/Desktop/simulation_project/driving_simulation/opends_2.0_bin/assets/DrivingTasks/Projects/HighTraffic.1/scenario.xml'),'xml')

sinW = genMultiSin(num=6950)

plotSpeed(range(6950),sinW)

points = [genPoint('WayPoint_'+str(i), 6950 - i, sinW[i]) for i in range(0,6950,20)]

soup = insertPoints(soup, points)

f = open('/Users/juwang/Desktop/simulation_project/driving_simulation/opends_2.0_bin/assets/DrivingTasks/Projects/HighTraffic.1/scenario.xml', "w")
f.write(str(soup))
f.close()

print 'DONE'
