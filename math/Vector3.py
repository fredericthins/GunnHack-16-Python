import

class Vector3:
	

	

	def __init__(self,x,y,z):
		"""
		initializing variables
		Aguments:
			x: x axis
			y: y axis
			z: z axis
		"""
		self.x = x
		self.y = y
		self.z = z

	def __init__(self, mat):
		"""
		Converts matrix to vector
		Aguments:
			matrix
		"""
		lastValue = m.item(0,3)
		self.x = mat.item(0,0) / lastValue
		self.y = mat.item(0,1) / lastValue
		self.z = mat.item(0,2) / lastValue

	def toString(self):
		"""
		Converts Vector to String
		"""
	def abs(self):
		"""
		Returns the magnitude of a vector
		"""
	def scale(self, size):
		"""
		Returns a vector that is scaled by a value of scalar
		Arguments:
			size: represents the scale
		"""
	def norm(self):
		"""

		Return a nomarlized version of the current Vector3
		"""
	def homogeneous(self):
		"""
		Return homogeneous version of the vector
		"""
	def rotate(self, Quaternion):
		"""
		Returns a vector that is rotated by quaternion q4
		Arguments:
			q4: Quaternion that represents the rotation
		"""
	@staticmethod
	def add(self, v1, v2):
		"""
		Return the resulting Vector of the addition of two vectors
		Arguments:
			v1: the first Vector
			v2: the second Vector
		"""
	@staticmethod
	def dot(self, v1, v2):
		"""
		Return the resulting Vector of the dot product of two vectors
		Arguments:
			v1: the first Vector
			v2: the second Vector
		"""
	@staticmethod
	def cross(self, v1, v2):
		"""
		Return the resulting Vector of the cross product of two vectors
		Arguments:
			v1: the first Vector
			v2: the second Vector
		"""
	@staticmethod
	def project(self, v1, v2):
		"""
		Return the resulting Vector of the projection of one vector onto another
		Arguments:
			v1: the first Vector
			v2: the second Vector
		"""
