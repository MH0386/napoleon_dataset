
new_content = new_content.split('\n')
new_content = list(filter(lambda x: x != '', new_content))
with open('Napoleon3.csv', 'w', newline='') as ff:
    print(new_content)
    for i in new_content:
        ff.write(f'"{i}' + '"\n')
