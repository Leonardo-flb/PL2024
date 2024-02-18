# TPC 2

## Autor

- Leonardo Filipe Lima Barroso 
- A100984

## Parágrafos 
 Será realizado abaixo um pequeno resumo da forma como foi desenvolvido o exercício

 A ideia geral é substituir as expressões regulares pelas desejadas ao ler o ficheiro

 A primeira expressão (head) substitui do ficheiro onde localizar e devolve uma string com o conteúdo.

 As expressões seguintes em vez de substituir do ficheiro substitui da string criada. 

 Resumindo é uma substituição em cadeia e devido a isso, a ordem das expressões teve que mudar visto que, por exemplo, a expressão das imagens e do link são semelhantes com a exceção de um '!'.

 **Head #+(.*) :** 
 **Bold \*\*([^*]+)\*\* :**
 **Italico \*([^*]+)\*:**
 **Link \[(.+)\]\((.+)\) :**
 **Imagem \!\[(.+)\]\((.+)\) :**
 **Lista Numerda \d+\.\s(.+) :**