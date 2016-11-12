import math.Vector3
class CubeMesh(Mesh):
	def __init__(self, s):
		vertices = {-s/2, s/2, s/2,   #F-U-L
					s/2, s/2, s/2,    #F-U-R
					s/2, -s/2, s/2,   #F-D-R
					-s/2, -s/2, s/2,  #F-D-L
					s/2, -s/2, -s/2,  #B-D-R
					-s/2, -s/2, -s/2, #B-D-L
					-s/2, s/2, -s/2,  #B-U-L
					s/2, s/2, -s/2}   #B-U-R

		faces = {{0, 3, 2}, #Front Left
				 {0, 2, 1}, #Front Right
				 {2, 4, 7}, #Right Right
				 {2, 7, 1}, #Right Left
				 {4, 6, 7}, #Back Right
				 {4, 5, 6}, #Back Left
				 {6, 0, 3}, #Left Left
				 {6, 3, 5}, #Left Right
				 {3, 2, 4}, #Bottom Right
				 {3, 4, 5}, #Bottom Left
				 {0, 1, 7}, #Top Right 
				 {0, 7, 6}} #Top Left
				 
		normal = {Vector3(0, 0, 1),  #Front Left
				  Vector3(0, 0, 1),  #Front Right
				  Vector3(1, 0, 0),  #Right Right
				  Vector3(1, 0, 0),  #Right Left
				  Vector3(0, 0, -1), #Back Right
				  Vector3(0, 0, -1), #Back Left
				  Vector3(-1, 0, 0), #Left Left
				  Vector3(-1, 0, 0), #Left Right
				  Vector3(0, -1, 0), #Bottom Right
				  Vector3(0, -1, 0), #Bottom Left
				  Vector3(0, 1, 0),  #Top Right
				  Vector3(0, 1, 0)}  #Top Left