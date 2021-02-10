

with open('main.tex', 'r') as file:
    text = file.read()

citacoes = [m.start() for m in re.finditer('cite{', text)]

citados = [text[i+5:].split('}')[0] for i in citacoes ]
citados = [i.split(',') for i in citados]
citados = [i for  j in citados for i in j]

CitadosUnique = []
for i in citados:
  if i not in CitadosUnique:
    CitadosUnique.append(i)
  else:
    continue

BibSeparada= text[text.find('thebibliography'):text.find('end{thebibliography}')].split('bibitem')

biblioordenada = []
for j in CitadosUnique:
  for k in BibSeparada:
    if j in k[0:len(j)+1]:
      biblioordenada.append(k)
      
bib = ''
for i in biblioordenada: bib = bib + "\\bibitem" +i[:-2]
     

textfinal = text.replace( text[text.find('thebibliography')+20:text.find('end{thebibliography}')-1], bib)

with open('mainfinal.tex', 'w') as file:
    file.write(textfinal)