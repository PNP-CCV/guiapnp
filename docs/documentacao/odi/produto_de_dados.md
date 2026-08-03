---
layout: default
title: "Produto de Dados"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas]({{ site.baseurl }}/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »]({{ site.baseurl }}/documentacao/caminho_do_arquivo) 
-->


# {{ page.title }}

Além de apresentar os dados agregados no painel visual, o Observatório de Dados e Informações (ODI) oferece a possibilidade de acessar e salvar diretamente os dados, seja por meio do **Extrator PNP** ou pela manipulação direta dos **Microdados PNP**.

Os microdados, juntamente com o dicionário de dados do Extrator PNP, tornam possível a reprodutibilidade dos indicadores calculados pela PNP, facilitando o acompanhamento interno das instituições que desejam monitorar seu desempenho. Assim, são produtos essenciais para apoiar a tomada de decisões baseadas em evidências. Paralelamente, esses produtos de dados reforçam o compromisso da PNP com a transparência, que é elemento fundamental para o monitoramento das políticas públicas e fortalecimento da confiança da sociedade na RFECPT.

## Extrator PNP

O Extrator PNP é uma ferramenta que permite a obtenção de informações estruturadas sobre os mesmos contextos apresentados no produto visual, quer seja os Dados Educacionais ou os Dados Orçamentários. Por meio da ferramenta, os conjuntos de dados podem ser acessados e salvos, facilitando análises e cruzamentos de informações.

A ferramenta disponibiliza um dicionário de dados em cada contexto, garantindo clareza sobre a estrutura e o significado dos campos extraídos. Fornece subsídios para quem deseja realizar análises em outras ferramentas, já tendo os indicadores calculados, em conformidade com o exibido no produto visual. Além disso, traz uma documentação com as fórmulas utilizadas para o cálculo, a partir do modelo de dados, facilitando a compreensão da lógica dos cálculos dos indicadores ao permitir que os usuários repliquem ou ajustem essas métricas em suas próprias análises, assegurando a consistência e precisão nos resultados. A figura abaixo apresenta a página inicial do Extrator PNP, que pode ser acessado [aqui](https://moduloextratorpnp.mec.gov.br/){:target="_blank"}.

![Fluxo geral de dados da PNP]({{ site.baseurl }}/assets/img/docs/ode_produto_dados_01.png)

## Microdados PNP

Outro produto de destaque da PNP é a disponibilização de microdados, fornecidos em menor nível de desagregação, no âmbito do Plano de Dados Abertos do Ministério da Educação (MEC), publicados no Portal de Dados Abertos do MEC.

A cada edição da PNP, são disponibilizados quatro arquivos de microdados principais:

* **Microdados de Matrículas**: representa o conjunto de dados relacionados às matrículas (matrícula, aluno, ciclo de matrícula, curso, unidade de ensino, instituição). Possui uma linha para cada matrícula que esteve ativa em pelo menos um dia no ano base.
* **Microdados Financeiros**: representa o conjunto de dados para as variáveis relacionadas ao financeiro, incluindo informações sobre orçamento, despesas e investimentos das instituições da RFEPCT.
* **Microdados de Eficiência Acadêmica**: representa o conjunto de dados necessários para o cálculo dos Indicadores disponíveis no painel “Eficiência Acadêmica”. Assim como os microdados de matrículas, este arquivo também está relacionado às matrículas (matrícula, aluno, ciclo de matrícula, curso, unidade de ensino, instituição), contudo possui uma linha para cada matrícula de ciclos que estavam previstos para terminar no ano anterior ao ano de referência.
* **Microdados de Servidores**: representa o conjunto de dados relacionados aos servidores docentes e técnico-administrativos, incluindo informações sobre vínculos, cargos, funções e titulações.

A disponibilização de microdados nesse nível de detalhamento é a garantia da democratização de dados educacionais, contrapondo-se a outras bases de dados nacionais que oferecem informações agregadas. Desse modo, qualquer pessoa interessada pode explorar e analisar os dados da Rede Federal de Educação Profissional, Científica e Tecnológica (RFEPCT) de forma autônoma.

Nos microdados de matrículas cada linha representa o registro de uma matrícula específica, com informações detalhadas sobre a instituição, o nome do curso, o eixo tecnológico, o tipo de curso, a modalidade de oferta, entre outros aspectos. Adicionalmente, os microdados incluem dados sobre a pessoa vinculada à matrícula, como sexo, idade, raça, renda familiar e forma de acesso (cotas ou ampla concorrência).

