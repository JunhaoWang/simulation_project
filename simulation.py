from bs4 import BeautifulSoup as Soup
import math
import matplotlib.pyplot as plt
import random
import os

##################### Parameters #########################

# lead vehicle only or not
leadonly = False

# average speed of lead vehicle
average = 60

# amplitude of change for the speed of lead vehicle
amplitude = 10

# average speed of side vehicle
oaverage = 40

# amplitude of change for the speed of side vehicle
oamplitude = 20

#########################################################


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

def genMultiSin(avg, amp, angfre = 0.1, num= 6950, complexity = 10):
	"""
	generate a concatenation of sinwaves to approximate random variation from:
	1. all inputs except for pha in genSin()
	2. number of sinwaves (complexity)
	"""
	amp *= complexity/2.5
	allW = []
	for i in range(complexity):
		newangfre = angfre * random.random()
		allW.append(genSin(avg, amp * random.random(), newangfre, newangfre * random.random() * complexity, num))
	result = allW[0]
	for i in allW[1:]:
		for ind, j in enumerate(i):
			result[ind] += j
	return [i/complexity for i in result]

def genPoint(name, loc, speed, lead = True):
	"""
	generate a wayPoint from:
	1. name of point (name)
	2. location of point (loc)
	3. max speed of point (speed)
	"""
	if lead:
		defPoint = """
		<wayPoint id="WayPoint_">
	      <translation>
	         <vector jtype="java_lang_Float" size="2">
	            <entry>{}</entry>
	            <entry>{}</entry>
	            <entry>6925</entry>
	         </vector>
	      </translation>
	      <speed>730.9434</speed>
	   </wayPoint>
		""".format(2.2045, -0.35273)
	else:
		defPoint = """
		<wayPoint id="WayPoint_0">
	      <translation>
	         <vector jtype="java_lang_Float" size="2">
	            <entry>{}</entry>
	            <entry>{}</entry>
	            <entry>6925</entry>
	         </vector>
	      </translation>
	      <speed>730.9434</speed>
	   </wayPoint>
	""".format(-1.1, -0.35273057)

	soup = Soup(defPoint,'xml')
	soup.wayPoint['id'] += str(name)
	soup.findAll('entry')[2].string = str(loc)
	soup.speed.string  = str(speed)
	[s.extract() for s in soup('?xml')]
	return soup.wayPoint


def plotSpeed(x, y, lead = True):
	"""
	plot speed profile for lead vehicle
	"""
	plt.plot(x, y)
	plt.xlabel('location')
	plt.ylabel('speed')
	if lead:
		plt.savefig('speed_profile_lead.png')
		plt.close()
	else:
		plt.savefig('speed_profile_side.png')
		plt.close()

def insertPoints(soup, points, lead = True):
	"""
	insert points related to the speed profile 
	"""
	if lead:
		for i in soup.find('traffic').findAll('vehicle')[0].findAll('wayPoint'):
			i.replaceWith('')
		for p in points:
			soup.find('traffic').findAll('vehicle')[0].wayPoints.append(p)
	else:
		for i in soup.find('traffic').findAll('vehicle')[1].findAll('wayPoint'):
			i.replaceWith('')
		for p in points:
			soup.find('traffic').findAll('vehicle')[1].wayPoints.append(p)
	return soup

if __name__ == "__main__":

	soup = Soup(open(os.path.abspath('opends_2.0_bin/assets/DrivingTasks/Projects/HighTraffic.1/scenario.xml')),'xml')

	sinW = genMultiSin(average, amplitude)
	osinW = genMultiSin(oaverage, oamplitude)

	plotSpeed(range(6950),sinW, True)
	plotSpeed(range(6950),osinW, leadonly)

	points = [genPoint(i, 6950 - i, sinW[i], True) for i in range(0,6950,20)]
	soup = insertPoints(soup, points, True)

	if leadonly:
		opoints = [genPoint(i, 6950 - i, 0, False) for i in range(0,6950,20)]
		soup = insertPoints(soup, opoints, False)
	else:
		opoints = [genPoint(i, 6950 - i, osinW[i], False) for i in range(0,6950,20)]
		soup = insertPoints(soup, opoints, False)

	f = open(os.path.abspath('opends_2.0_bin/assets/DrivingTasks/Projects/HighTraffic.1/scenario.xml'), "w")
	f.write(str(soup))
	f.close()
	print 'DONE'
