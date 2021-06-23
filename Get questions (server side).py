import requests
from bs4 import BeautifulSoup

number = int(input('Number of questions: '))

page = requests.get("https://www.gkseries.com/general-knowledge/geography/regional-geography/multiple-choice-questions-and-answers-on-indian-geography-8")

x = 1


def getQuestion():
    print('\n')
    global x
    y = x - 1
    z = 4*y;
    soup = BeautifulSoup(page.content, 'html.parser')
    question = soup.find_all("div", class_="question-content")[y].get_text()
    question = question[12:].strip()
    print(question)
    optionA = soup.find_all("div", class_="option")[z].get_text()
    optionA = 'A. '+ (optionA[1:].strip())
    optionB = soup.find_all("div", class_="option")[z+1].get_text()
    optionB = 'B. '+ (optionB[1:].strip())

    optionC = soup.find_all("div", class_="option")[z+2].get_text()
    optionC = 'C. '+ (optionC[1:].strip())
    optionD = soup.find_all("div", class_="option")[z+3].get_text()
    optionD = 'D. '+ (optionD[1:].strip())

    print(optionA)
    print(optionB)
    print(optionC)
    print(optionD)
    print('\n')

    correct_answer = soup.find_all("blockquote", class_="blockquote")[0].get_text()
    print(correct_answer.strip())


    x = x + 1

for i in range(number):
    getQuestion()

