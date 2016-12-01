"""
Kei Imada
20161124
Finds the synonyms from thesaurus.com
"""
import lxml
from lxml import html
import requests

def main():
    session_requests = requests.session()
    word = raw_input("word: ")
    url = "http://www.thesaurus.com/browse/" + word
    result = session_requests.get(url)
    tree = html.fromstring(result.text)
    synonyms = tree.xpath('//div[@id="synonyms-0"]//div[@class="relevancy-list"]//span[@class="text"]/text()')
    wordId = tree.xpath('//div[@id="synonyms-0"]//div[@class="relevancy-list"]//a/@data-category')
    for index in range(len(wordId)):
        wordId[index] = eval(wordId[index])
    wordList = []
    for word in zip(wordId, synonyms):
        wordTemp = word[0]
        wordTemp.update({"word":word[1]})
        wordList.append(wordTemp)
    showWord = []
    for word in wordList:
        if word["name"] == "relevant-3":
            showWord.append(word["word"])
    for word in showWord:
        print word
    if len(showWord) == 0:
        print "no relevant synonyms found"
    print
    if word != "":
        main()
if __name__ == "__main__":
    main()
