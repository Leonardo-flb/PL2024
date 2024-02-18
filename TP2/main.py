import sys,re

head = r'#+(.*)'
bold = r"\*\*([^*]+)\*\*"
italico = r"\*([^*]+)\*"
link = r'\[(.+)\]\((.+)\)'
imagem = r'\!\[(.+)\]\((.+)\)'
list = r'\d+\.\s(.+)'

file=sys.stdin.read()

new = re.sub(head,r'<h1>\1</h1>',file)
new = re.sub(bold,r'<b>\1</b>',new)
new = re.sub(italico,r'<i>\1</i>',new)
new = re.sub(imagem, r'<img src="\2" alt="\1"/>', new)
new = re.sub(link, r'<a href="\2">\1</a>', new)
new = re.sub(list, r'<li>\1</li>', new, flags=re.MULTILINE)
new = re.sub(r'((<li>.+</li>\n?)+)',r'<ol>\n\1\n</ol>',new)

f = open("teste.html", "w")
f.write(new)