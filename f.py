
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(':\n', ': ')
content = content.replace('“', '"')
content = content.replace('”', '"')
content = content.replace('’', "'")
content = content.replace('—', ' ')
content = content.replace('–', ' ')
content = content.replace('."', '".')
content = content.replace(',"', '",')
content = content.replace(".'", "'.")
content = content.replace(",'", "',")
content = content.replace('  ', ' ')
content = content.replace('\n\n', '\n')
content = content.replace('. ', '.')
content = content.replace('.', '.\n')
content = content.replace('.\n\n', '.\n')

content = content.lower()

for i in range(len(content)):
    if content[i] == '"' and content[i - 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        content = content[:i] + ' '

with open('data.txt', 'w', encoding='utf-8') as f:
    f.write(content)
