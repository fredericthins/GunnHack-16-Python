import numpy as np
from math import *

class Quaternion:

	"""
		Constructor given four dimensions

		Arguments:
			w: w dimension
			x: x dimension
			y: y dimension
			z: z dimension
	"""
	def __init__(self,w,x,y,z):
		self.w = w
		self.x = x
		self.y = y
		self.z = z

	"""
		Constructor given 3D vector and fourth dimension

		Arguments:
			w: w dimension
			vector: 3D Vector with x,y,z dimensions
	"""
	def __init__(self,w,vector):
		self.w = w;
		self.x = vector.x
		self.y = vector.y
		self.z = vector.z

	"""
		Constructor given a matrix

		Arguments:
			matrix: matrix with w,x,y,z dimensions
	"""
	def __init__(self,matrix):
		self.w = matrix[1,1]
		self.x = matrix[2,1]
		self.y = matrix[3,1]
		self.z = matrix[4,1]

	"""
		Convert quaternion to readable string format

		return: string format of quaternion
	"""
	def toString(self):
		return "[" + self.w + ", " + self.x + ", " + self.y + ", " + self.z + "]";

	"""
		Scale quaternion by size

		Arguments: 
			size: scale factor

		return: scaled quaternion
	"""
	def scale(self,size):
		return Quaternion(self.w*size, self.x*size, self.y*size, self.z*size)

	"""
		Conjugate quaternion

		return: conjugated quaternion
	"""
	def conj(self):
		return Quaternion(self.w, self.x*-(1), self.y*(-1), self.z*(-1))

	"""
		return: magnitude of quaternion
	"""
	def abs(self):
		return sqrt(Quaternion.Multiply(self, self.conj()).w)

	"""
		return: normalized quaternion
	"""
	def norm(self):
		return self.scale(1/self.abs());

	"""
		return: inverse of quaternion
	"""
	def inverse(self):
		return self.conj().scale(1/(self.abs()*self.abs()))

	"""
		return: matrix form of quaternion
	"""
	def mat(self):
		return np.matrix([
			[w],
			[x],
			[y],
			[z]
			])

	"""
		return: matrix to perform Q*p, where Q is self and p is another quaternion
	"""
	def matPrimary(self):
		return np.matrix([
			[self.w, self.x*(-1), self.y*(-1), self.z*(-1)],
			[self.x, self.w, self.z*(-1), self.y],
			[self.y, self.z, self.w, self.x*(-1)],
			[self.z, self.y*(-1), self.x, self.w]
			])

	"""
		return: matrix to perform p*Q, where Q is self and p is another quaternion
	"""
	def matSecondary(self):
		return np.matrix([
			[self.w, self.x*(-1). self.y*(-1), self.z*(-1)],
			[self.x, self.w, self.z, self.y*(-1)],
			[self.y, self.z*(-1), self.w, self.x],
			[self.z, self.y, self.x*(-1), self.w]
			])

	"""
		For quaternion Q on vector v, give quaternion for Q*v*(Q^-1)

		return matrix that represents quaternion rotation
	"""
	def matRot(self):
		return self.matPrimary() * self.conj().matSecondary()

	"""
		I don't know what this method does

		Arguments:
			vect1: inital vector
			vect2: final vector
	"""
	@staticmethod
	def fromTo(vect1, vect2):
		m = sqrt(2 + 2*Vector3.Dot(vect1, vect2))
		return Quaternion(0.5*m, Vector3.cross(vect1,vect2).scale(1/m))

	"""
		return: sum of the two quaternions

		Arguments:
			quat1: quaternion 1
			quat2: quaternion 2
	"""
	@staticmethod
	def Add(quat1, quat2):
		return Quaternion(quat1.w + quat2.w, quat1.x + quat2.x, quat1.y + quat2.y, quat1.z + quat2.z)

	"""
		return: product of two quaternions

		Arguments:
			quat1: quaternion 1
			quat2: quaternion 2
	"""
	@staticmethod
	def Multiply(quat1, quat2):
		return Quaternion(quat1.matPrimary()*quat2.mat())

	"""
		return: a float which is the Dot of all 4 dimesions

		Arguments:
			quat1: quaternion 1
			quat2: quaternion 2	
	"""
	@staticmethod
	def Dot(quat1, quat2):
		return quat1.w*quat2.w+quat1.x*quat2.x+quat1.y*quat2.y+quat1.z*quat2.z

	"""
		return: w dimension
	"""
	def getW(self):
		return self.w

	"""
		return: x dimension
	"""
	def getX(self):
		return self.x

	"""
		return: y dimension
	"""
	def getY(self):
		return self.y

	"""
		return: z dimension
	"""
	def getZ(self):
		return self.z

	"""
		set new w value

		Arguments:
			w: new w dimesion
	"""
	def setW(self, w){
		self.w = w
	}

	"""
		set new x value

		Arguments:
			x: new x dimesion
	"""
	def setX(self, x){
		self.x = x
	}

	"""
		set new y value

		Arguments:
			y: new y dimesion
	"""
	def setW(self, y){
		self.y = y
	}

	"""
		set new z value

		Arguments:
			z: new z dimesion
	"""
	def setZ(self, z){
		self.z = z
	}











