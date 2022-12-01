myDict = {
    "bls": "Binay Lal Shrestha",
    "as": "Adity Shrestha",
    "marks": [45, 32, 46, 41],
    "anotherDict":{
        "nds": "Nima Devi Shrestha"
    },
    1: 2

}

# Dictionary Methods
print(myDict.keys()) #prints the keys of the dictionary

print(type(myDict.keys())) #type 

print(myDict.values()) #prints the values of the dictionary

print(myDict.items()) #prints the (key,value) for all contents of the dictionary

print(myDict) 
updateDict={
    "language": "newari",
    "address": "soalteemode",
    "bls": "Basu Lal Shrestha", #changes the value of the main dictionary as well
}
myDict.update(updateDict) #updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("bls")) #prints value assiciated with key "bls"
# the (.get) method returns NONE if the content is not present in the-
# dictionary whereas printing the unpresent key returns an error