# For this project, you will import the **json** module.

# Write a class named NobelData that reads the nobels.json file and allows the user to search that data.

# Your class should have:
# * an init method that reads the file and stores it in whatever data member(s) you prefer. Any data members of the NobelData class must be **private**.
# * a method named search_nobel that takes as parameters a year and a category, and returns a sorted list (in normal English dictionary order) of the surnames for the winner(s) in that category for that year (up to three people can share the prize). The year will be a string (e.g. "1975"), not a number. The categories are: "chemistry", "economics", "literature", "peace", "physics", and "medicine".

# For example, your class could be used like this:

# nd = NobelData()
# nd.search_nobel("2001", "economics")


import json

class NobelData:
    def __init__(self):
        with open('nobels.json') as f:
            self.__data = json.load(f)
    def search_nobel(self, year, category):
        results = []
        for prize in self.__data["prizes"]:
            if prize["year"] == year and prize["category"] == category:
                for laureate in prize["laureates"]:
                    results.append(laureate["surname"])
        results.sort()
        return results
nd = NobelData()
print(nd.search_nobel("2001","economics"))

# Begin by reading the prompt and understanding the task at hand. The prompt is asking to create a class named NobelData that reads the nobels.json file and allows the user to search the data in it.
# Next, notice that the prompt is asking for two methods in the NobelData class: an init method and a search_nobel method.
# The init method is required to read the file and store it in whatever data member(s) you prefer. Any data members of the NobelData class must be private.
# The search_nobel method takes as parameters a year and a category and returns a sorted list of the surnames for the winner(s) in that category for that year.
# Since we are working with json data, import the json module to parse the json data.
# Create the class NobelData.
# Create the init method. This method will read the json file and parse it using json.loads().
# Create a data member, such as self._data, to store the json data.
# Create the search_nobel method. This method will take in two parameters: year and category.
# Use a for loop to iterate through the json data, searching for the year and category passed in as parameters.
# If a match is found, extract the surnames of the winners and store them in a list.
# Return the list of surnames sorted in normal English dictionary order.