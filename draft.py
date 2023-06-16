import ast

a = "{'anger': 0.6, 'disappointment': 0.3, 'neutral': 0.1, 'fear': 0.0, 'joy': 0.0}"


a = ast.literal_eval(a)

if type(a) is dict:
    print('yes')
else:
    print('no')

string = 'hi, how can i help you?'

print('Hi' in string)




def hi(text):
    while True:
        a = input('bede byad')

        try:
            a = a.split()
        except:
            continue

    print(a)

    #test
    # test
    # test
