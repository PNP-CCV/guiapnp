---
layout: default
title: "Fluxo geral"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas](/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »](/documentacao/caminho_do_arquivo) 
-->

# {{ page.title }}

A Plataforma Nilo Peçanha (PNP) organiza-se em dois processos complementares: os Ciclos de Coleta e Validação (PNP-CCV) e o Observatório de Dados e Informações (PNP-ODI).

O fluxo geral da PNP tem início com a coleta de dados em sistemas governamentais. Nessa etapa, os dados são extraídos do Sistec (dados acadêmicos), Siape (gestão de pessoas) e Siafi (dados financeiros).

Atualmente, alguns dados não estão disponíveis no Sistec, como raça, renda e forma de ingresso de cada matrícula. Por isso, esses dados também são coletados pelos Ciclos de Coleta e Validação (CCV), um sistema transacional que permite a integração de dados e a aplicação de regras de consistência.

Após a coleta, os dados passam pela etapa de validação, que é crucial para garantir sua integridade e comparabilidade. Nessa etapa são aplicadas regras semânticas e metodológicas para identificar inconsistências, corrigir discrepâncias e alinhar os dados às diretrizes normativas da Rede Federal de Educação Profissional, Científica e Tecnológica (RFEPCT). A validação dos dados é realizada, então, por registradores acadêmicos, pesquisadores institucionais e gestores das áreas acadêmica e de pessoal das instituições da RFEPCT. Uma vez validados, os dados são submetidos à chancela do dirigente máximo de cada instituição.

Com os dados validados, as próximas etapas são realizadas pelo Observatório de Dados e Informações (ODI) da PNP. A primeira delas é a modelagem e orquestração, que organiza os dados em estruturas semânticas e modelos dimensionais que suportam análises avançadas e diferentes visualizações. A modelagem semântica define tabelas, relações e atributos que traduzem os dados em informações. A orquestração de dados é um processo de Extração, Transformação e Carregamento (ETL). Assim, é garantida a integração contínua entre diferentes fontes de dados.

A etapa seguinte, de análise e processamento, aplica técnicas para transformar os dados brutos nas informações da PNP e realiza análises exploratórias para identificar tendências, padrões e comportamentos. Depois do processamento, os dados são preparados para a disseminação.

A disseminação é realizada por meio do painel interativo e microdados, disponíveis no portal oficial da plataforma. O painel se apresenta em formato intuitivo: inclui gráficos, tabelas e mapas, que estão acessíveis ao público em geral e a gestores educacionais. Além disso, os microdados são disponibilizados em arquivos CSV acompanhados de documentação detalhada, permitindo análises personalizadas por parte de usuários externos. O Extrator PNP também oferece arquivos em formato CSV, mas diferencia-se dos microdados por oferecer dados dos indicadores já calculados.

Por fim, a sustentação tecnológica garante a continuidade e a escalabilidade do sistema. Esse ecossistema tecnológico é complementado por estratégias de monitoramento e manutenção que garantem a atualização contínua e o funcionamento eficiente da plataforma.

A figura abaixo ilustra o fluxo geral de dados e informações e a relação entre os processos que compõem a PNP. Nesse fluxo, os dados oriundos de sistemas estruturantes (Sistec, Siape e Siafi) são integrados pela PNP-CCV àqueles extraídos de sistemas setoriais certificados (Rede Integra, Sissa e Observatório de Egressos) e os sistemas institucionais (notadamente Suap e Sigaa). Os dados provenientes das fontes que chegam ao PNP-CCV passam por regras de consistência. Em seguida, são corrigidos e validados, consolidando as informações em um conjunto coerente que subsidia o cálculo dos indicadores. Em seguida, os dados são disponibilizados ao PNP-ODI para cálculo e disseminação dos indicadores, permitindo o monitoramento da RFEPCT, apoiando a tomada de decisões estratégicas e promovendo a transparência.

![Fluxo geral de dados da PNP]({{ site.baseurl }}/assets/img/docs/metodologia_fluxo_geral_defeso.png)

Os dados oriundos das fontes e bases estruturantes e institucionais que chegam à PNP-CCV passam por regras de consistência para a identificação de possíveis inconsistências. São então corrigidos e validados, consolidando as informações da Rede Federal de Educação Profissional, Científica e Tecnológica (RFEPCT) em um conjunto coerente que subsidia o cálculo dos indicadores. Após esse processo, os dados são disponibilizados ao PNP-ODI para cálculo e disseminação dos indicadores. 

A PNP também processa dados de outros domínios, como os dados orçamentários do Tesouro Gerencial e Painel do Orçamento do SIOP, sistemas estruturantes que alimentam de forma automática os panoramas visuais da PNP-ODI, bem como os dados dos sistemas setoriais certificados, a exemplo do Integra. Esses dados também passam por processos de limpeza e transformação para que o conjunto de informação disponibilizado ao público fortaleça a transparência, apoie o monitoramento e o desenvolvimento das políticas nacionais da RFEPCT.
