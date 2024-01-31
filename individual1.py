def hyphen_reducer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = '-'.join(part for part in result.split('-') if part)
        return result
    return wrapper

@hyphen_reducer
def to_lat(s):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
         'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
         'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
         'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
         'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    
    s = s.lower()
    result = ''
    
    for char in s:
        if char.isalpha():
            result += t.get(char, char)
        elif char in "!?:;.,_":
            result += '-'
        else:
            result += char
    
    return result

# Пример использования:
input_string = "Как тебя зовут! Меня, Ильяс?"
output_string = to_lat(input_string)
print(output_string)
