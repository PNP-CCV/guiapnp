---
layout: default
title: "Produto de Dados"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas](/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »](/documentacao/caminho_do_arquivo) 
-->

# {{ page.title }}

O Produto de Dados do CCV é uma solução tecnológica projetada com base em uma arquitetura robusta e flexível, incorporando as melhores práticas da engenharia de software e da análise de dados. Essa modernização visa garantir mais interoperabilidade, escalabilidade e eficiência, considerando a diversidade dos sistemas de gestão de dados existentes na Rede Federal de Educação Profissional, Científica e Tecnológica (RFEPCT). Dentro dessa solução tecnológica, destaca-se o Coletor PNP-CCV.

Concebido para dar suporte à coleta, ajuste, complementação e validação de todos os dados necessários para a PNP, o Produto de Dados do CCV sustenta os subprocessos de coleta e processamento de dados e de conferência, ajuste e validação de dados.

## Coleta e processamento de dados

O subprocesso de coleta e processamento de dados objetiva sistematizar a coleta de dados da RFEPCT, por meio da disponibilização de ferramentas tecnológicas responsáveis pela incorporação de dados oriundos de fontes governamentais e pela extração de dados padronizados de bases institucionais e de sistemas certificados pela Setec/MEC. Esse subprocesso é composto pelas etapas de carga de dados; processamento e validação preliminar dos dados; e *merge* de dados.

## Carga de dados

A etapa da carga de dados tem aspectos diferenciados entre o ciclo de dados acadêmicos e de pessoal e o ciclo de pesquisa e inovação e de extensão. No ciclo de validação de dados acadêmicos e de pessoal, os dados do Sistec são carregados por meio do serviço Olinda – mantido e operacionalizado pela Subsecretaria de Tecnologia da Informação (STIC) do Ministério da Educação –, e os dados do Siape são carregados a partir do fornecimento de uma exportação direta pela Setec/MEC. São carregados, nessa ação, milhares de registros de matrículas de estudantes e dados de pessoal. Cabe ressaltar que, nesse fluxo, cabe à STIC o processamento tanto no início quanto no final dos Ciclos de Coleta e Validação. No ciclo de pesquisa e inovação e de extensão, os dados são extraídos tanto diretamente das bases institucionais quanto de sistemas certificados pela Setec/MEC, por meio do Coletor PNP-CCV, com base nos conjuntos de microdados padronizados, definidos pela Setec/MEC.

Para prover a comunicação com as bases de dados das instituições, o Coletor PNP-CCV – que era conhecido no âmbito do sistema monitor – é implantado diretamente nos sistemas acadêmicos e/ou administrativos internos dos Institutos Federais, Cefets e Colégio Pedro II da RFEPCT, com apoio das equipes institucionais de tecnologia da informação. Uma vez conectado às bases institucionais, o Coletor PNP-CCV executa uma rotina de extração e pré-validação dos dados que serão coletados, e um ambiente de teste de extração é disponibilizado para que as equipes de tecnologia da informação das instituições possam realizar testes em ambientes seguros e confiáveis, previamente à extração definitiva. Caso seja detectado algum erro de consistência nos dados, o extrator alerta a equipe de tecnologia da informação para que proceda com a correção na fonte original da instituição. Esse processo de integração automatizado evita que as instituições precisem manter a informação em dois sistemas diferentes.

A comunicação entre o Coletor PNP-CCV e os sistemas/bases institucionais e/ou os sistemas certificados pela SETEC ocorre de três formas: por meio de planilhas, de consultas diretas a banco de dados usando Structured Query Language (SQL) e de Application Programming Interface (API) fornecida pelos sistemas. Em todos os casos, os dados devem ser organizados seguindo o modelo de microdados definido para cada conjunto solicitado. No uso de planilhas, deverão ser usadas planilhas hospedadas em serviços como Google Docs/Microsoft Office 365 ou disponibilizadas em área de armazenamento de arquivo em que o Coletor PNP-CCV possa realizar a leitura. No caso do uso do SQL, a consulta deverá retornar todos os dados(colunas) já com a nomenclatura estabelecida no conjunto de microdados. Além disso, na aplicação Coletor PNP-CCV, a instituição deverá configurar a conexão do banco de dados para permitir a correta execução da consulta. Por fim, na extração usando API, o processo ocorre semelhante ao das consultas SQL, com a diferença de que a estrutura de resposta da API deve estar no formato Javascript Object Notation (JSON).

## Processamento e validação preliminar dos dados

A etapa de processamento e validação preliminar dos dados consiste na qualificação dos dados coletados dos sistemas governamentais, bases institucionais e sistemas certificados pela Setec/MEC. Nessa etapa, os dados recebidos são analisados e testados para verificar se estão completos, consistentes, íntegros e em formato adequado. Caso sejam identificadas falhas nessa etapa, soluções de contorno são exploradas para que ao final os dados estejam prontos para a etapa seguinte. Esta etapa é conduzida por meio de uma aplicação que permite a automatização de inúmeros procedimentos, organizando as categorias de análise e dando celeridade e confiabilidade às estatísticas produzidas. Quando o padrão de erro detectado permite a correção de forma automatizada, é aplicada uma correção em lote. Nos casos que demandam intervenção manual, são realizadas as correções individuais dos registros.

## Merge dos dados

Com os dados processados, é realizada a etapa de *merge* dos dados, que consiste na combinação dos dados carregados no ciclo atual com os já validados em ciclos de edições anteriores da PNP. Anualmente, os novos dados lançados no Sistec se somam aos registros já existentes, mas nem sempre esses dados são devidamente atualizados após a publicação da PNP, o que pode comprometer a precisão e a consistência das informações divulgadas. Essa situação criaria a obrigação de a PNP-CCV refazer a validação a cada ano, o que resultaria em (re)trabalho excessivo e desnecessário. Com a criação de regras de comparação entre a base extraída do Sistec e a base final da PNP do ciclo anterior, as correções e complementações realizadas anteriormente são aproveitadas, evitando retrabalho dos atores institucionais. Assim, quando um dado é informado numa edição da PNP, as edições subsequentes já incorporam essa informação, sem demandar uma nova intervenção da instituição. Cabe destacar que na versão atual da PNP, o processo de *merge* se aplica à situação da matrícula do estudante, de forma que seja refletida a situação mais atual, comparando os dados do Sistec e da PNP. A figura abaixo ilustra o fluxo da etapa de *merge*.

![Fluxo da etapa de merge]({{ site.baseurl }}/assets/img/docs/ccv_produto_de_dados_01.png "Fluxo da etapa de merge")

Por exemplo, matrículas que tiveram o status corrigido para integralizada, abandono, desligamento ou transferências ficam armazenadas com esse novo status no banco de dados. Por isso, mesmo que no Sistec a Instituição tenha esquecido de atualizá-las, nas edições subsequentes da PNP as matrículas não serão mais consideradas nas inconsistências, pois já foram corrigidas para estados terminativos durante o ciclo da PNP.

## Conferência, ajuste e validação de dados

O subprocesso de conferência, ajuste e validação de dados objetiva promover a consistência dos dados sobre a RFEPCT. Esse subprocesso ocorre fundamentalmente com a participação ativa de um conjunto de atores institucionais das estruturas que compõem a RFEPCT:

* Registradores Acadêmicos (RA) e Executores Acadêmicos (EA): tratam as inconsistências nos dados acadêmicos.
* Pesquisador Institucional (PI): supervisiona a conferência e os ajustes e realiza a pré-validação dos dados acadêmicos.
* Gestor de Pessoal, Gestor de Pesquisa e Inovação e Gestor de Extensão: tratam as inconsistências e realizam a pré-validação dos dados de pessoal, de pesquisa e inovação e de extensão, respectivamente.
* Dirigente máximo da instituição: chancela e valida os dados da instituição.

Esse subprocesso se desenvolve por meio de correção e complementação de dados, pré-validação de dados e validação final dos dados.

A etapa de correção e complementação dos dados permite que os dados sejam ajustados, complementados e justificados pelos atores institucionais. A operacionalização dessa etapa fica a cargo de uma aplicação Web que promove o processamento desses dados por meio da aplicação de regras de consistência e subsequente resolução das inconsistências identificados pela ação dos atores institucionais. Essa aplicação segue as diretrizes da Subsecretaria de Tecnologia da Informação (STIC) do Ministério da Educação, no que diz respeito à arquitetura tecnológica e aos padrões de desenvolvimento, além do uso do *design system*  do Governo Federal na implementação da interface com os usuários. Vale observar que a justificativa de uma inconsistência só é possível quando a correção do dado é momentaneamente inviabilizada, de modo que a inconsistência será representada no próximo ciclo daquele conjunto de dados, até que seja definitivamente corrigida. Um exemplo dessa situação é a forma de ingresso, caso a cota correspondente da matrícula seja apenas justificada (não informada), a inconsistência retornará no próximo ciclo.

De acordo com os perfis disponíveis, os atores institucionais da PNP-CCV realizam as operações de correção ou complementação de dados diretamente na aplicação, tanto de forma individualizada para cada inconsistência (uma a uma), quanto por meio da importação de arquivos. A importação de arquivos permite a correção de alguns tipos de inconsistência em lote, ação especialmente útil no caso das operações que envolvem um grande volume de registros.

A etapa de pré-validação de dados é realizada ao final do saneamento de todas as inconsistências pelo respectivo gestor institucional.

A realização das correções ou justificativas de dados acadêmicos cabe aos Registradores Acadêmicos e Executores Acadêmicos, com confirmação ou ajustes adicionais pelo Pesquisador Institucional. Para os dados de pessoal, essas atividades são realizadas pelo Gestor de Pessoal. Os dados de pesquisa e inovação e de extensão, quando incorporados à PNP, serão submetidos a um processo de validação equivalente, pelo Gestor de Pesquisa e Inovação e pelo Gestor de Extensão, de modo a garantir a qualidade e confiabilidade dos dados.

A figura abaixo apresenta o *print* de uma tela de correção de inconsistências de dados acadêmicos, disponibilizada na aplicação PNP-CCV. Nessa tela, os dados inconsistentes são apresentados, por meio de status de validação e de um esquema de cores de sombreamento das colunas. O status de validação (situação) é utilizado para comunicar internamente se o dado está inconsistente, se foi atualizado pelo EA ou pelo RA, se foi pré-validado pelo PI, ou se foi validado pelo dirigente máximo da instituição. O esquema de cores de sombreamento é utilizado para demonstrar se o dado inconsistente já foi validado em edições anteriores da PNP (em amarelo), dispensando novo ajuste, ou se precisa efetivamente de correção com uma nova informação (em vermelho).

![Exemplo de tela de correção de inconsistências de dados acadêmicos]({{ site.baseurl }}/assets/img/docs/ccv_produto_de_dados_02.png "Exemplo de tela de correção de inconsistências de dados acadêmicos")

Nesse exemplo, dados de cor/raça e renda per capita já foram informados em ciclos anteriores e por isso a situação é “alterado RA”. É possível restaurar o dado e corrigir ou apenas validá-lo. Já a forma de ingresso apresenta dois campos em vermelho na situação inconsistente RA, em que é preciso informar o dado. As situações/estados das inconsistências estão associadas aos três níveis de validação existentes nas inconsistências de ensino. O primeiro nível é o RA, o segundo PI e por último o RE. No caso das inconsistências de gestão de pessoas, são dois níveis de validação, denominados GP e RE. A figura abaixo apresenta a máquina de estados no subproduto de conferência, ajuste e validação dos dados.

![Máquina de estados no subproduto de conferência, ajuste e validação dos dados]({{ site.baseurl }}/assets/img/docs/ccv_produto_de_dados_03.png "Máquina de estados no subproduto de conferência, ajuste e validação dos dados"){:style="display: block; margin: 0 auto;"}

Com todas as pré-validações do ciclo cumpridas, o conjunto de dados institucionais é submetido à chancela do dirigente máximo da instituição na etapa de validação final dos dados, finalizando o subprocesso de conferência, ajuste e validação, bem como o ciclo de dados ativo no âmbito da instituição. Os dados validados passam, então, a ser tratados pelo processo PNP-ODI.

Nas etapas de pré-validação e validação final dos dados podem ocorrer situações adversas específicas relatadas por instituições da RFEPCT, como por exemplo a ausência de dados que a instituição alega que deveriam estar presentes. Nesse contexto, o Produto de Dados também apoia a Setec/MEC na resolução de tais situações adversas. No apoio à solução, cada relato é minuciosamente investigado e compreendido, e tais informações são repassadas à Setec/MEC para uma deliberação. Se a deliberação envolver alguma ação com relação aos dados, elas são devidamente realizadas e informadas à instituição.

O Produto de Dados PNP-CCV está em constante evolução, em consonância com as definições da Setec/MEC. A cada execução de um ciclo de coleta e validação é realizada uma avaliação dos resultados obtidos, das ocorrências reportadas e das devolutivas recebidas das instituições durante a execução do ciclo. Essa avaliação suscita propostas de melhoria de funcionalidades existentes e de inclusão de novas funcionalidades que são apresentadas à Setec/MEC e, após aprovação, são implementadas no contexto do processo PNP-CCV.