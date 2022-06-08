def old_text(text):
    if not 'абв' in text:
        return True 
text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
text_list = text.lower().split()
new_text = filter(old_text,text_list)
print(list(new_text))