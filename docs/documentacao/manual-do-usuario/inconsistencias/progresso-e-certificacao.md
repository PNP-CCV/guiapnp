---
layout: default
title: "Progresso e Certificação de Conclusão das Inconsistências"
toc: true
---
# Progresso e Certificação de Conclusão das Inconsistências

Esta tela mostra quanto da correção das inconsistências de uma instituição
já chegou ao fim, em barras de progresso, e emite o **certificado de
conclusão** quando todas foram concluídas pelo Reitor. Junta as
[inconsistências de ensino]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-ensino) e as de
[gestão de pessoas]({{site.baseurl}}/documentacao/manual-do-usuario/inconsistencias/inconsistencias-de-gestao-de-pessoas).

No menu, a tela fica em **Inconsistências → Progresso e Certificação de
Conclusão das Inconsistências**, e o card de mesmo nome no Painel também
leva a ela. Aparece para Pesquisador Institucional, Reitor, Administrador,
Gestor CCV e Suporte CCV. Ao contrário das telas de correção, ela não
depende do período de correção.

## Escolher a instituição

O Pesquisador Institucional e o Reitor veem direto a própria instituição.
O Administrador, o Gestor CCV e o Suporte CCV escolhem a instituição no
filtro **Instituição** e usam **Filtrar**. Até escolher, a tela mostra só o
aviso.

![A tela com a instituição escolhida, concluída]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/progresso-e-certificacao/instituicao.png)

## As barras de progresso

O bloco da instituição tem uma barra para cada grupo de inconsistência:
**Ciclo**, **Curso** e **Matrícula**, do ensino, e **Unidade
Organizacional** e **Servidor**, da gestão de pessoas.

Cada barra é dividida pelas situações das inconsistências daquele grupo,
com as cores da **Legenda** acima dela. A legenda traz as situações de
cada etapa (RE, PI, RA e GP) e **Sem Inconsistências**, a cor da barra
de um grupo que não tem nenhuma. Passar o mouse sobre um trecho mostra o
nome da situação. O percentual aparece dentro do trecho quando ele ocupa
mais de 15% da barra. Inconsistências de linhas excluídas não entram na
conta.

Quando todas as inconsistências da instituição estão em *Validado RE*, as
barras ficam inteiras no verde do *Validado RE* e a tela avisa que a
instituição concluiu todas as correções. Enquanto falta alguma, ou se a
instituição não tem nenhuma inconsistência, a tela
avisa que o certificado só pode ser gerado depois da conclusão de todas as
inconsistências, e os botões **Validar Certificado** e **Certificado de
Conclusão** ficam desabilitados.

## Ver uma unidade

Escolhida a instituição, o filtro **Unidade** lista as unidades dela.
Escolha uma e use **Filtrar**: o bloco **Unidade**, mais abaixo, mostra as
barras de Ciclo, Curso e Matrícula daquela unidade. A unidade tem só as
barras do ensino.

O botão **Detalhar Instituição** abre uma página com as barras da
instituição e, abaixo, um bloco para cada unidade. A **Busca** dessa
página filtra as unidades pelo nome.

![Detalhe da instituição: um bloco de barras por unidade]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/progresso-e-certificacao/unidades.png)

## O certificado de conclusão

Com a instituição concluída, o botão **Certificado de Conclusão** abre o
certificado da edição do ano corrente: o nome da instituição, a edição, o
**código de validação** e a data de emissão. **Baixar Certificado** salva
o certificado em PDF.

![Certificado de conclusão de uma instituição]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/progresso-e-certificacao/certificado.png)

A plataforma só emite o certificado quando todas as inconsistências da
instituição naquela edição estão concluídas pelo Reitor. Se ainda falta
alguma, a página mostra **Certificado indisponível** no lugar do
certificado.

O certificado não fica guardado: a plataforma o monta a cada vez que a
página é aberta. A data de emissão muda a cada abertura. O código de
validação, não: ele é sempre o mesmo para a mesma instituição e edição.

## Validar um certificado

O botão **Validar Certificado** confere se um código de validação é
verdadeiro. Informe o **Ano de Edição** e o **Código de Validação**, os
dois obrigatórios, e use **Validar**. A plataforma confere o código contra
a instituição escolhida na tela e o ano informado, e responde *O
certificado é válido.* ou *O certificado é inválido.*

![Validação de um código de certificado]({{site.baseurl}}/assets/img/docs/manual-do-usuario/inconsistencias/progresso-e-certificacao/validar.png)
