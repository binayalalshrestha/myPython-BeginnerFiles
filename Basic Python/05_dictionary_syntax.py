myDict = {
    "bls": "Binay Lal Shrestha",
    "as": "Adity Shrestha",
    "marks": [45, 32, 46, 41],
    "anotherDict":{ #nestedDictionary
        "nds": "Nima Devi Shrestha"
    }

}

print(myDict["bls"])

myDict["bls"]="Basu Lal Shrestha" #changable
print(myDict["bls"])

print(myDict["anotherDict"]["nds"])