#Temperature Converter
# given a temperature in Fahrenheit calculat the corresponding temperature in Celsius and Kelvin Degrees

#intro to the user
print("Temperature Converter")
print("Give a temperature in F this program will convert it to Celsius and Kelvin ")

#get the temperature in F from the user
TempF = float(input("Enter the temperature in F degrees: "))
#convert the temperature to C using the prodided formula
TempC = (TempF - 32)* 5/9
#convert the temperature to K using the prodided formula
TempK = TempC + 273.15
#display the temperature in C and in K
print("Our temperature in Farenheight is", TempF, "F")
print("Our temperature in Celsius is", round(TempC,2), "C")
print("Our temperature in Kelvin is", round(TempK,2), "K")



