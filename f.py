with open('data2.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    new_content = content[:]

    for i in range(len(content)):
        if new_content[i] == ' ' and new_content[i - 1] == '.':
            new_content = f'{new_content[:i]}.{new_content[i + 1:]}'

    for i in range(len(content)):
        if new_content[i] == '.':
            new_content = new_content[:i] + '\n' + new_content[i + 1:]

    for i in content:
        if i in ['"', "'"]:
            new_content = new_content.replace(i, ' ')

new_content = new_content.split('\n')
new_content = list(filter(lambda x: x != '', new_content))
with open('Napoleon2.csv', 'w', newline='') as ff:
    print(new_content)
    for i in new_content:
        ff.write(f'"{i}' + '"\n')
