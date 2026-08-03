---
layout: default
title: "Produto Semântico"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas]({{ site.baseurl }}/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »]({{ site.baseurl }}/documentacao/caminho_do_arquivo) 
-->


# {{ page.title }}

O fornecimento de informações sob demanda para o Produto Visual é estruturado a partir de uma organização semântica de um modelo de dados, de forma dimensional e que possibilite a consolidação das diversas fontes de dados. Categoriza-se o **Produto Semântico** nos seguintes contextos de dados e respectivas tabelas:

* Contexto acadêmico - dados relativos a curso, ciclos, situação de matrícula, renda de estudantes, raça de estudantes, oferta de vagas e fatos referentes a matrícula do ano corrente, matrículas para fins de eficiência acadêmica e avaliação dos cursos e instituição por meio do Inep.
* Contexto pessoal – dados relativos à situação funcional, jornada de trabalho, escolaridade, cargos, funções, tempo de serviço e carreira de servidores e fatos relativos a vínculos de servidores a unidades organizacionais, cargos e funções.
* Contexto financeiro – dados relativos à esfera, resultado primário, fonte de recursos, natureza de despesa, plano de trabalho e fatos de eventos orçamentários e financeiros (disponibilidades e indisponibilidades orçamentárias, bem como empenho, liquidação e pagamento de despesas no exercício e em restos a pagar).
* Contexto rede – dados relativos às instituições e unidades, bem como as tabelas de ligação entre instituições, órgãos orçamentários e unidades gestoras executoras e as instituições e as unidades organizacionais do Siape.
* Contexto visual – tabelas que organizam os elementos visuais da PNP, como as listas de filtros, ícones, brasões, medidas e parâmetros de campo.

A relação entre as tabelas é definida por meio de chaves que são atributos compartilhados entre as tabelas e podem ter valores de um sistema de origem (número da unidade organizacional no Siafi, por exemplo) ou criadas sistematicamente em função da ausência de unicidade no contexto necessário (chave de curso, por exemplo). Eles podem ser do tipo um para muitos ou muitos para muitos (neste caso, implementados por meio de uma tabela de ligação que tem um par de chaves um para muitos e muitos para um).
