rept = {"python" : " питон", 
 "anaconda" : "анаконда", 
 "tortoize" : " черепаха" }
 

rept["snake"] = "змея"
print(rept)

rept["tortoise"] = rept["tortoize"]
print(rept)
del rept["tortoize"]
print(rept)

for key in rept:
    print(f"{rept[key]} по-английски будет {key}")