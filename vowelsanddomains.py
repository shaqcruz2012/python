# Write a function that uses a regex expression to return a list with all the words that start with a vowel.
# Exmaple:
# Input: 'Errors should never pass silently. Unless explicitly silenced.'
# Output: ['Errors', 'Unless', 'explicitly']



# Write another function that uses a regex expression to return a list of emails that all have the domain of gmail.com.
# Exmaple:
# Input: 'aa@xyz.com bbb@abc.com cccc@cisco.com'
# Output: ['aa@gmail.com', 'bbb@gmail.com', 'cccc@gmail.com']

#import regular expression module
import re
#define the function that takes in a string as a parameter
def find_vowel_words(string):
    #use re.findall() method to find all words that start with a vowel. Regex pattern [aeiouAEIOU]\w+ match the words that start with a vowel and store the result in a variable words
    words = re.findall(r"[aeiouAEIOU]\w+",string)
    return words
#Test the function by calling it and passing in a sample string
print(find_vowel_words("Errors should never pass silently. Unless explicitly silenced."))
#output should be ['Errors','Unless','explicitly']
#Define the function taking in a string as a parameter
def find_gmail_emails(strings):
    #use re.findall() method to find all emails that have the domain of gmail.com. Use regex pattern "\w+gmail.com" to match emails that have the domain of gmail.com and store the result in a variable called emails
    emails = re.findall(r"\w+gmail.com", string)
    return emails

print(find_gmail_emails("aa@xyz.com bbb@abc.com cccc@gmail.com"))

#The output should be ['cccc@gmail.com']
#If you want to make your function more robust, you can use a pattern like "\w+@[a-zA-Z]+.com" which will match any email that end with .com, or you can use the pattern "\w+@gmail.com" to match only gmail.com
#Note: These regex patterns will match only basic email format. It won't match all possible valid email addresses, if you want to match more complex email address format, you can use more complex regex pattern.