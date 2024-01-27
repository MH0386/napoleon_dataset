with open('all_data.txt', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('“', '"')
content = content.replace('”', '"')
content = content.replace('’', "'")
content = content.replace('—', '')
content = content.replace('."', '".')
content = content.replace(',"', '",')
content = content.replace(".'", "'.")
content = content.replace(",'", "',")
content = content.replace('  ', ' ')
content = content.replace('\n\n', '\n')
content = content.replace('. ', '.')
#content = content.replace('.', '.\n')

content = content.lower()

with open('all_data.txt', 'w', encoding='utf-8') as f:
    f.write(content)