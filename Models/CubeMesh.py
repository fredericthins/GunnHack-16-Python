import math.Vector3
class CubeMesh(Mesh):
	def __init__(sidelength, vertices):
		self.s = sidelength
		self.vertices = {
			s/2, -s/2, s/2,		  
			-s/2, -s/2, s/2,	
			-s/2, s/2, s/2,		
			s/2, s/2, s/2,		
			-s/2, s/2, -s/2,		
			s/2, s/2, -s/2,		
			s/2, -s/2, -s/2,		
			-s/2,-s/2, -s/2	
		}
		self.faceSet = { 
			{1,0,2},	
			{0,3,2},	
			{0,6,5},	
			{0,5,3},	
			{2,3,5},	
			{2,5,4},	
			{1,2,4},	
			{7,1,4},	
			{1,0,6},	
			{1,6,7},	
			{7,6,4},	
			{6,5,4}		
		}
		self.normal = {
			new Vector3(0,0,1),
			new Vector3(0,0,1),	
			new Vector3(1,0,0), 
			new Vector3(1,0,0),
			new Vector3(0,1,0), 
			new Vector3(0,1,0), 
			new Vector3(-1,0,0), 
			new Vector3(-1,0,0), 
			new Vector3(0,-1,0), 
			new Vector3(0,-1,0), 
			new Vector3(0,0,-1),
			new Vector3(0,0,-1)	
		}