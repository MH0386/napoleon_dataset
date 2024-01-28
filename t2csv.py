f = open('data.txt', 'r', encoding='utf-8')
content = f.read()
content = content.split('\n')
content = list(filter(lambda x: x != '', content))
with open('napoleon.csv', 'w', newline='') as ff:
    print(content)
    for i in content:
        ff.write(f'"{i}' + '"\n')
