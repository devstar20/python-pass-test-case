def blood_pressure(systolic, diastolic):
	risk_level = 1.0
	mean_pressure = (systolic +  2.0 * diastolic) / 3.0 
	if systolic > 180 or diastolic > 120:
		risk_level = 1.4
	elif systolic >= 140 or diastolic >= 90:
		risk_level = 1.3
	elif systolic >= 130 and systolic < 140 or  diastolic >= 80 and diastolic < 90:
		risk_level = 1.2
	elif systolic >= 120 and systolic < 130 and diastolic < 80:
		risk_level = 1.1
	elif systolic < 120 and diastolic < 80:
		risk_level = 1.0
	return round(risk_level * mean_pressure, 2)	

def standard_BMI(weight, height, ISU):
	if ISU == False:
		weight = weight / 35
		height = height * 0.025
	return round(weight / (height ** 2), 2)

def BMI_chart(weight, height, age, gender):
	BMI = standard_BMI(weight, height, True)
	if age >= 18:
		if BMI < 18.5:
			return ("underweight")
		elif BMI <= 25:
			return ("normal")
		elif BMI <= 30:
			return ("overweight")
		else:
			return ("obese")
	if gender == "female":
		boundry = [15, 20, 23]
	else:
		boundry = [14, 19, 22]
	if BMI < boundry[0]:
		return ("underweight")
	elif BMI <=boundry[1]:
		return ("normal")
	elif BMI <= boundry[2]:
		return ("overweight")
	else:
		return ("obese")

def HCT(red_cells, total_cells, age, gender):
	if total_cells < 1000000:
		return False
	if age < 18:
		up = 40.0
		bottom = 36.0
	elif gender == "male":
		up = 50.3
		bottom = 40.7
	else:
		up = 44.3
		bottom = 36.1
	percent = red_cells / total_cells * 100.0
	if percent >= bottom and percent <= up:
		return True
	else :
		return False

def LDL(total, HDL, trig, age, gender):
	k = 0.2
	if trig < 11.3 or trig > 43.5:
		k = 0.0
	if total > 250 and trig > 43.5:
		k = 0.19 - int((total - 250) /10) * 0.01
	LDL = total - HDL - k * trig
	if age < 18:
		if LDL < 100:
			return 0
		risk = 1 + int((LDL - 100) / 15)
		if risk > 5:
			return 5
		return risk
	else:
		if LDL < 120:
			risk = 0
		else:
			risk =1 + int((LDL - 120) / 20)
		if risk > 5:
			risk = 5
		if gender == "male" and HDL < 40 or gender =="female" and HDL < 50:
			risk = risk + 1
		if HDL > 70:
			risk = risk - 1
		if risk < 0:
			return 0
		if risk > 5:
			return 5
		return risk
