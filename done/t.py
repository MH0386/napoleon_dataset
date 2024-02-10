with open('napoleon_prompt_format.jsonl', 'r') as f:
    content = f.read()
    content = content.replace('{\n  ', '{')
    content = content.replace('"\n}', '}')
