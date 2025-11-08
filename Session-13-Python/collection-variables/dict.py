my_dict={
    "name":"sonam soni",
    "age":35,
    "city":"Mumbai",
    "expertise":["DevOps","JAVA FSD","MEAN","MERN","GenAI"]
}
# print(my_dict)
# Access only city
print("City: ",my_dict["city"])
# add new value
my_dict["manager"]="Test Manager"
my_dict["age"]=37 # update existing

# iterate using loop
for key in my_dict:
    print(key,": ",my_dict[key])
    
# Removal
my_dict.pop("age") # remove based in key
my_dict.popitem() # remove last pair
print(my_dict)