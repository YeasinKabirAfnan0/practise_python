Fruit_name = "  Apple,Banana,  Jackfruit  "

# upper,lower,find where the banana is,title,remove unnecessary spaces from both sides and also for over all
# replace n with m,search if monkey is there or not, prove grapes are not there

print(Fruit_name)

print("lower case", Fruit_name.lower())
print("Upper Case", Fruit_name.upper())
print("the banana is located at the position of string :",
      Fruit_name.find("Banana"))
print(Fruit_name.strip())
print(Fruit_name.lstrip())
print(Fruit_name.rstrip())
print(Fruit_name.replace("n", "m"))
print("monkey" in "Fruit_name")
print("grapes" not in "Fruit_name")
