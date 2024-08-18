import time
from EnglishRobot import TeachLanguageScript

if not __name__ == '__main__':
    exit()

obj = TeachLanguageScript() 

data = obj.read_data_from_csvfile()

for word, translat in data.items():
    obj.ask_question(text=f'what is means of this {word}', translat=translat)
    a = 50 - len(word)
    s = a*' ' + '|'
    print(word, s, translat)
    time.sleep(5)

print(translat)