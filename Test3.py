from encodings import utf_8

parasites = { 1:'«Ну,', 2:'короче.', 3:'короче,',4:'В',5:'общем,',6:'говоря,',7:'кажется,',
              8:'кажется.', 9:'Ну,эээ,', 10:'Как', 11:'бы', 12:'эээээ….', 13:'Ясен',14:'ясен',
              15:'пень', 16:'Кстати,', 17:'Ээээ...короче,', 18:'ээээ…', 19:'короче', 20:'пень.',
              21:'общем.',}

def parasites_clear(text, dictionary):
    new_text = text.copy()
    for i in range (len(text)):
        for key in dictionary.keys():
            if text[i] == dictionary[key]:
                new_text.remove(text[i])   
    return new_text

with open('file.txt', 'r', encoding=('utf-8')) as text:
    bad_text = text.read().split()
print(bad_text)
new_text = ' '.join(parasites_clear(bad_text, parasites))
print(new_text)  