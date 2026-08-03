---
layout: default
title: "Processo ODI"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas]({{ site.baseurl }}/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »]({{ site.baseurl }}/documentacao/caminho_do_arquivo) 
-->


# {{ page.title }}

O processo do Observatório de Dados e Informações (PNP-ODI) é uma atividade centralizada na Plataforma Nilo Peçanha (PNP), que visa elevar a maturidade de dados da Rede Federal de Educação Profissional, Científica e Tecnológica (RFEPCT). Esta iniciativa reflete um compromisso com a governança de dados, assegurando a qualidade, a consistência e a acessibilidade das informações, tanto para subsidiar políticas públicas quanto para promover transparência e inovação tecnológica. O PNP-ODI opera por meio de um processo robusto e articulado que engloba modelagem e orquestração dos dados para a disseminação das informações em produtos de valor público.

A modelagem e a orquestração são etapas críticas que organizam os dados validados em estruturas dimensionais e semânticas para o cálculo dos indicadores e disseminação dos dados. Primeiramente, ocorre a modelagem semântica, na qual os dados são estruturados em tabelas e relacionamentos que asseguram sua interoperabilidade. Esse modelo semântico abrange um mapeamento detalhado das dimensões e fatos, tais como unidade, curso, ciclos, entre outros. Essa estrutura é projetada para suportar múltiplos recortes e interpretações, facilitando a análise pela equipe técnica e pelos usuários finais.

Na sequência, a orquestração de dados utiliza etapas para integrar fontes diversas. É utilizada uma ferramenta para integrar e padronizar os dados de diferentes fontes que são consolidadas em um processo conhecido por Extração, Transformação e Carregamento (ETL). Os dados também são enriquecidos com fontes relevantes, como dados orçamentários e de pessoal. Esse processo garante a escalabilidade e a automatização das atualizações necessárias, minimizando a intervenção manual e maximizando a eficiência operacional.

A disseminação de dados é realizada por meio da criação de três produtos principais: [Produto Visual]({{site.baseUrl}}/guiapnp/documentacao/odi/produto_visual "Produto Visual"), [Produto Semântico]({{site.baseUrl}}/guiapnp/documentacao/odi/produto_semantico "Produto Semântico") e [Produto de Dados]({{site.baseUrl}}/guiapnp/documentacao/odi/produto_de_dados "Produto de Dados"). Esses produtos são distribuídos por meio da **PNP Indicadores**, oferecendo uma interface intuitiva para acessar os dados em formatos gráficos e tabulares.

O Produto Visual apresenta gráficos, mapas e diagramas em um painel interativo exibido em uma plataforma web, a **PNP Indicadores**. Já o Produto Semântico consolida e estrutura as diferentes fontes de dados em um modelo dimensional, com tabelas temáticas e relacionamentos, que possibilitam somas, contagens e cálculos de indicadores que são exibidos sob demanda no Produto Visual. Por fim, o Produto de Dados disponibiliza informações em formato CSV, acessíveis para manipulação direta pelos usuários (Microdados PNP e Extrator PNP) e publica os Microdados PNP como dados abertos no portal do MEC, conforme Plano de Dados Abertos (PDA).  

O fluxo de trabalho do Observatório evidencia um grau de complexidade e interdependência entre as etapas. Além das ferramentas tecnológicas, o processo é suportado por uma governança eficiente, composta por um comitê central que garante a padronização e a qualidade dos dados. Essa governança é responsável por monitorar e propor melhorias contínuas no ciclo de dados, promovendo um ecossistema colaborativo.

O Observatório de Dados e Informações, portanto, vai além da disseminação de indicadores, visto que cria um ambiente tecnológico e metodológico que possibilita a democratização do acesso à informação, a formulação de políticas educacionais baseadas em evidências e a transparência na gestão pública.


