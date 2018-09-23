class Parent():


	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last Name - "+self.last_name)
		print("Eye color - "+self.eye_color)

class Child(Parent):


	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	def show_info(self):
		print("Last Name - "+self.last_name)
		print("Eye Color - "+self.eye_color)


kevin_j = Parent("Smith", "blue")
kevin_j.show_info()

joseph = Child("Smith", "blue", 5)
joseph.show_info()

print(joseph.last_name)
print(joseph.number_of_toys)



class Toys():

	def __init__(self, var1, var2, var3, var4):
		print("Parent Constructor")
		self.name = var1
		self.address = var2
		self.good = var3

	def show_information(self):
		print(self.name, self.address)


class Legos(Toys):
	
	def __init__(self, var1, var2, fish_count):
		print("Child Constructor")
		Toys.__init__(self, var1, var2)
		self.fish_count = fish_count

Lego = Toys("Cam", "Gene", "Cookie", "nice")

Star_Wars_Set = Legos("good", "fish", "7")