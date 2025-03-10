def assign_grade(score):
	if 0 <= score <=100:
		if 90 <= score <=100:
			print ("Grade: A")
		elif 80 <= score <= 89:
			print ("Grade: B")
		elif 70 <= score <=79:
			print ("Grade: C")
		elif 60 <= score <=69:
			print ("Grade: D")
		else:
			print ("Grade: F")
	else:
		print ("Invalid score. Please input a value between 0 and 100")
		
assign_grade (99)
assign_grade (89)
assign_grade (79)
assign_grade (69)
assign_grade (0)