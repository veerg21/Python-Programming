# meanings={"apple":"fruit", "bing":"search engine"}
# word=input("Enter a word: ")
# print(meanings[word])
import json
data=json.load(open("dictionary.json"))
# print(data)
def translator(w):
    # print(w)
    w=w.lower()
    if w in data:
        # print(data[w])
        return data[w]

word=input("Enter the word you want to search in the dictionary: ")
output=translator(word)
# print(output)
if output==None:
    print("The word which you wrote is not present in the dictionary. Please check your spelling or write another word.")
else:
    print(output)