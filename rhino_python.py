# randomcubes.rhino

import rhinoscriptsyntax as rs
from Rhino import Geometry
import random

# seed_factor variable defined in grasshopper
random.seed(seed_factor)

# create a point
somePoint = rs.coerce3dpoint(startPoint)

# a list to store points
x = []


# Create a box

def  boxgen(somePoint, recursion):
	
	x.append(somePoint)

	# size variable defined in gh
	move_x = random.uniform(-size*factor, size*factor)
	move_y = random.uniform(-size*factor, size*factor)

	# create stacked boxes 
	while recursion < 5 :

		# move the point in z
		zPoint = somePoint + Point3d(0, size, size)
		# create an instance
		boxgen(somePoint, recursion + 1)
		
		if (abs(move_x) > size * 0.5) & (abs(move_y) > 0.5 * size):  

			# move the point in y
			yPoint = somePoint + Point3d(-move_x, -move_y, size)
			# create an instance
			boxgen(somePoint, recursion + 1)
	

# create an instance
result = boxgen(somePoint, 0)

# then boxes
boxgen(result)


### animation ###

import scriptcontext as sc 

# refer to the document
sc.doc = ghdoc # grasshopper document

# define the location, inputs in the gh gui
loc = rs.coerce3dpoint(location)
target = rs.coerce3dpoint(target)

viewport = sc.doc.Views.Active.ActiveViewport

viewport.SetCameraLocation(cameraLocation=loc, updateTargetLocation=False)
viewport.SetCameraDirection(target - loc, updateTargetLocation=False)


import Rhino

while active:
	for i in range(len(geo)):
		
		geo_id = geo[i]

		# switch to gh context
		sc.doc = ghdoc
		doc_object = rs.coercerhinoobject(geo_id)
		geometry = doc_object.Geometry
		attributes = doc_object.Attributes

		# switch to rhino context, and migrate the geom
		sc.doc = Rhino.RhinoDoc.ActiveDoc
		todo = sc.doc.Objects.Add(geometry, attributes)

		# change the layer
		rs.ObjectLayer(todo, layer)

	else:
		break

# end of the script