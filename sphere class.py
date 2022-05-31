#class which has diffrent difinitions of the same method and finds the area ,volume and circumfreance of a sphere
class Sphere:#class name
    def __init__(self,radius):#constructor
        self.radius=radius
    def area(self):#method for area
        return 4*3.14*(self.radius**2)#returns the area of the sphere
    def volume(self):#method for volume
        return (4/3)*3.14*(self.radius**3)
    def circumference(self):#method for circumference
        return 2*3.14*self.radius#returns the circumference of the sphere
#the object of the class prints the results totwo decimal palces


object1=Sphere(5)#object of the class
print("the area of the sphere is",object1.area())#prints the area of the sphere
print("the volume of the sphere is",object1.volume())#prints the volume of the sphere
print("the circumfrence of the sphere is",object1.circumference())#prints the circumfrence of the sphere
