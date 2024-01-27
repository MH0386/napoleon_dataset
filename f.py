f = open('data.txt', 'r', encoding='utf-8')
content = f.read()
new_content = content[:]

for i in range(len(content)):
    if new_content[i] == ' ' and new_content[i - 1] == '.':
        new_content = new_content[:i] + '.' + new_content[i + 1:]

for i in range(len(content)):
    if new_content[i] == '.':
        new_content = new_content[:i] + '\n' + new_content[i + 1:]

for i in content:
    if i == '"' or i == "'":
        new_content = new_content.replace(i, ' ')

f.close()

new_content = new_content.split('\n')
new_content = list(filter(lambda x: x != '', new_content))
ff = open('Napoleon.csv', 'w', newline='')
print(new_content)
for i in new_content:
    ff.write('"'+i+'",\n')

ff.close()