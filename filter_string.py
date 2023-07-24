def filter_string(string, to_delete):
    string = list(string)
    for _ in range(len(string)):
        try:
            string.remove(to_delete)
        except:
            pass
    print(''.join(string))


text = 'If I look back I am lost'
filter_string(text, 'I')  # 'f  look back  am lost'
filter_string(text, 'o')  # 'If I lk back I am lst'
