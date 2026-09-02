---
layout: default
title: "Validação referencial"
toc: true
---
# Validação referencial

* TOC
{:toc}

> **Para quem é:** 🔌 integradores externos · 👔 gestores · 🛠️ desenvolvedores

Alguns campos do contrato não guardam um valor qualquer: guardam uma **referência a algo que existe no cadastro da Rede** — um campus, um município, uma área temática do CNPq, o CPF de alguém da instituição. O schema não tem como cobrar isso: `26419.4300604.01.001` é uma `string` perfeitamente válida, mesmo quando é o código de campus de *outro* Instituto.

Quem cobra é a PNP, na validação que roda **depois** do envio. O problema nunca foi a regra — era *quando* o operador descobria: extrair, enviar, esperar a fila e só então ler a rejeição. O Coletor passou a **antecipar a mesma conferência para a extração**, usando os cadastros que ele já sincroniza da própria PNP.

> ℹ️ **Antecipa, não substitui.** A validação que vale continua sendo a da PNP. Esta camada existe para entregar o diagnóstico cedo, com o campo, a linha e o valor em mãos — não para dar a palavra final. Passar aqui não é garantia de passar lá (o cadastro local pode estar desatualizado); ser reprovado aqui é quase certeza de que lá também seria.

## Onde ela entra

A conferência roda **por modelo**, depois de consolidar todas as Configurações de Extração daquele modelo e **antes de gravar o Parquet** — mesmo ponto da validação de schema, pela mesma razão: reprovar antes de escrever evita deixar em disco um arquivo que a PNP rejeitaria dias depois.

| # | Etapa | Onde |
|---|---|---|
| 1 | Schema — colunas e tipos | Coletor, na extração |
| **1.5** | **Referencial — o valor existe no cadastro?** | **Coletor, na extração** |
| 2 | Grava o Parquet | Coletor |
| 3 | Teste do contrato (`quality`) | Coletor, ao fim da extração |
| 4 | Envio à PNP | Coletor |
| 5 | Validação referencial oficial | PNP, depois do envio |

## Os três modos

O comportamento é decidido pela variável de ambiente `VALIDACAO_REFERENCIAL_MODO`:

| Modo | O que faz | Quando usar |
|---|---|---|
| **`bloqueante`** (padrão) | Uma violação de `severidade: erro` reprova a extração do modelo; `severidade: aviso` continua só registrando. | O comportamento normal. |
| **`sombra`** | Confere tudo e registra o resultado no Registro de Extração, mas **nunca reprova** — mesmo o que está declarado como `severidade: erro`. | Diagnóstico: ver o que uma regra apontaria sem travar a coleta de ninguém. |
| **`desligada`** | Não confere nada. | Último recurso, quando nem o registro do apontamento é desejado. |

> 💡 **Quem regula a rigidez é o contrato, não esta variável.** O ajuste fino é a `severidade` declarada **campo a campo** no contrato: `erro` reprova, `aviso` só registra. Quem controla isso é a CCV, e a mudança chega aos institutos pela sincronização de contratos — sem release, sem tocar em nenhuma instalação. É esse o botão a usar quando uma regra se mostra rígida demais.
>
> Os três modos são uma alavanca de emergência da própria CCV, para o caso de um cadastro desatualizado reprovar extração legítima em toda a Rede. Não são configuração de instalação: quem roda o Coletor não tem `.env` nem acesso ao `docker compose`, então o padrão do código é literalmente o que roda em todo mundo — e um padrão que não reprova nada equivale a não ter a validação.

## O que ela consegue conferir

Cada recurso declarado no contrato é conferido contra o cadastro local correspondente — os mesmos que a tela **Dados da PNP** mostra, populados por "Sincronizar com a PNP":

| `recurso:` no contrato | Cadastro local |
|---|---|
| `campi`, `estruturas` | Estruturas |
| `municipios` | Municípios (já vem preenchido, 5.570 linhas) |
| `areas_tematicas_cnpq`, `areas_cnpq` | Áreas Temáticas |
| `subeixos_tecnologicos`, `subeixos` | Subeixos |
| `servidores` | Servidores |
| `matriculas` | Matrículas |
| `pessoas` | Servidores **∪** Matrículas — ver abaixo |

> ⚠️ **Cadastro vazio não reprova.** Instalação que nunca sincronizou tem o cadastro local vazio. Reprovar nesse caso condenaria 100% das linhas por falta de dado **nosso**, não do operador — então a regra é pulada, com um aviso no log pedindo a sincronização. Vale o mesmo para recurso que o Coletor não conhece, chave que o cadastro não expõe e coluna que não veio nos dados: tudo vira registro no log, nunca reprovação.

### `pessoas` não é uma tabela

Não existe cadastro único de pessoas na PNP: existem **dois** — `servidores` e `matriculas`. O alias `recurso: pessoas`, mantido por compatibilidade embora nenhum contrato atual o use, resolve a referência pela **união** dos dois cadastros: a pergunta que essa regra faz é "esse CPF pertence a alguém da instituição?", e a união responde exatamente isso.

A união é deliberadamente frouxa: ela aceita o CPF de um estudante numa linha marcada como `docente`. Os contratos atuais adotam a conferência estrita descrita a seguir: [Ações de Extensão]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/acoes_de_extensao) e [Projetos de Pesquisa]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/projetos_de_pesquisa) roteiam a chave composta `[cpf, matricula]` conforme a categoria, e [Produção Intelectual]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/producao_intelectual) confere todas as autorias no cadastro de servidores.

## A gramática `referencia_pnp`

É uma extensão da PNP, fora da especificação do Data Contract — o motor de teste do contrato ignora a chave, e é a validação referencial que a lê.

### Forma simples

```yaml
estrutura:
  type: string
  referencia_pnp:
    recurso: campi
    tipo: codigo
    severidade: erro
```

Sem `chave`/`chaves` declarados, a chave é `codigo` e o valor conferido é o do **próprio campo** — `estrutura` casa com o `codigo` do cadastro de estruturas.

### Forma com roteamento

Uma **lista**, em que cada entrada carrega o próprio filtro de categoria. É o que resolve o caso em que o mesmo campo aponta para tabelas diferentes conforme o tipo de vínculo — matrícula SIAPE de servidor contra matrícula do sistema acadêmico de aluno:

```yaml
matricula:
  type: string
  referencia_pnp:
    - recurso: servidores
      tipo: chave_composta
      chaves: [cpf, matricula]
      filtro_categoria_campo: categoria
      categorias_validar: ["docente", "TAE"]
      severidade: erro
    - recurso: matriculas
      tipo: chave_composta
      chaves: [cpf, matricula]
      filtro_categoria_campo: categoria
      categorias_validar: ["estudante"]
      severidade: erro
```

A lista **é** o roteamento: cada entrada só se aplica às categorias que declara. Uma categoria ausente de todas as entradas — `externo`, que não está em cadastro nenhum — simplesmente não é conferida, sem virar erro.

As duas formas convivem: Ações de Extensão, Projetos de Pesquisa e Produção Intelectual usam a lista de regras para participantes, enquanto os demais campos continuam na forma simples.

### `chave_composta` confere a tupla

`chaves: [cpf, matricula]` confere o **par**, não os dois campos em separado. A diferença não é cosmética: conferir cada um por si aceitaria o CPF de uma pessoa com a matrícula de outra, já que os dois valores existem — em pessoas diferentes.

### Quando as colunas têm outro nome

`chaves` nomeia as colunas do **cadastro**; por padrão, assume-se que o modelo usa os mesmos nomes. Quando não usa, `colunas` faz a ponte. Nenhum contrato precisa dela hoje — Produção Intelectual chegou a chamar `cpf_autoria`/`matricula_autoria` e voltou aos nomes do cadastro —, mas a chave existe para um modelo cujos campos não possam ser renomeados:

```yaml
matricula_do_autor:
  type: string
  referencia_pnp:
    - recurso: servidores
      tipo: chave_composta
      chaves: [cpf, matricula]
      colunas: [cpf_do_autor, matricula_do_autor]
      filtro_categoria_campo: categoria
      categorias_validar: ["docente", "TAE"]
      severidade: erro
```

Sem a ponte, a regra procura colunas que o modelo não tem, registra o aviso e é pulada — uma validação declarada que não valida nada é pior do que não declarar.

### Campos aceitos

| Campo | Obrigatório | Significado |
|---|---|---|
| `recurso` | sim | Nome do cadastro da PNP (tabela acima). Desconhecido → registro no log, regra pulada |
| `tipo` | não | `codigo`, `chave_simples`, `chave_composta`, `array_codigo`. Documental: quem determina o comportamento é `chave`/`chaves` |
| `chave` | não | Chave única a conferir (ex.: `cpf`). Padrão: `codigo` |
| `chaves` | não | Lista de chaves — dispara a conferência por tupla |
| `colunas` | não | Colunas do modelo que alimentam cada chave, quando não têm o mesmo nome |
| `severidade` | não | `erro` (padrão) ou `aviso`. Só tem efeito no modo `bloqueante` |
| `filtro_categoria_campo` | não | Coluna que diz a categoria da linha |
| `categorias_validar` | não | Categorias a que esta entrada se aplica |

## Formato não é violação

Uma reprovação indevida é pior do que não validar: ensina o operador a ignorar o aviso. A fonte institucional e o cadastro da PNP raramente escrevem a mesma coisa do mesmo jeito, então a comparação normaliza os dois lados antes de decidir:

| Chave | Normalização | Resolve |
|---|---|---|
| `cpf` | Só dígitos, preenchido a 11 | Máscara `123.456.789-01`; zero à esquerda que a planilha comeu ao tratar o campo como número |
| `matricula` | Sem zeros à esquerda, **dos dois lados** | `0001234` no cadastro e `1234` no dado extraído, ou o inverso |
| demais (códigos) | Espaços e caixa apenas | Espaço sobrando, maiúscula/minúscula |

> ⚠️ **Pontuação de código é significativa.** Nos códigos, a pontuação **não** é removida: `26419.4300604.01.001` é o formato real do código de estrutura, e descartar os pontos aproximaria códigos distintos. O mesmo código sem os pontos é outro código.

Valor **ausente** também não é violação referencial: quem cobra preenchimento é o `required` do campo ou uma regra `quality`. Aqui, ausente é "nada a conferir".

## O que o operador vê

A conferência aparece em **duas telas**, sempre que a última extração do modelo apontou alguma coisa:

- **Modelos → o modelo**, junto do erro de extração e da rejeição da PNP;
- **Extrações → o registro**, que é onde se investiga uma extração específica.

O bloco é **âmbar** quando apenas aponta e **vermelho** quando reprovou. A diferença importa: um apontamento de `severidade: aviso` não impediu nada, e sem dizer isso o aviso seria lido como falha, mandando o operador procurar um erro que não existe.

> ⚠️ **Sem essa tela, o que só avisa é invisível.** Um apontamento que não reprova (`severidade: aviso`, ou qualquer regra no modo sombra) não muda status nenhum. Se existisse apenas dentro do JSON de detalhes, seria na prática indistinguível de a conferência não ter rodado.

O dado bruto continua nos detalhes do **[Registro de Extração]({{ site.baseurl }}/documentacao/coletor/glossario#registro-de-extracao)** do modelo, sob a chave `validacao_referencial`:

```json
{
  "modo": "bloqueante",
  "violacoes": [
    {
      "campo": "estrutura",
      "recurso": "campi",
      "chaves": ["codigo"],
      "severidade": "erro",
      "efeito": "reprova",
      "total": 20,
      "amostras": ["26419.4300604.01.001"]
    }
  ]
}
```

`severidade` é o que o contrato **declarou**; `efeito` é o que de fato aconteceu nesta execução. Os dois divergem no modo sombra, que rebaixa todo `erro` a `aviso` sem apagar a severidade declarada — é assim que se lê "isto teria reprovado".

No modo bloqueante, o motivo do erro do Registro de Extração replica o formato da mensagem da PNP, para o operador reconhecer o mesmo texto dos dois lados:

```text
Extração rejeitada para o modelo acoes_extensao. Validação referencial
reprovada — (campi, campo 'estrutura'): 20 com codigo inexistente em
'campi': '26419.4300604.01.001'
```

Só as **cinco primeiras** amostras entram na mensagem: o suficiente para reconhecer o padrão do erro sem transformar o motivo da falha num despejo de dados pessoais.

## Por que não é uma regra `quality`

Seria natural escrever isso como um check do próprio contrato. Não dá, por dois motivos independentes:

1. **O motor de teste roda em modo restrito**, sem acesso a nada fora dos Parquets do contrato — e afrouxar isso para alcançar o banco desligaria a proteção em silêncio, sem erro e sem aviso. É caro demais para pagar por uma conferência.
2. **Os cadastros não estão em Parquet.** Eles vivem no banco do Coletor, não no diretório de extrações que o motor lê.

Por isso a conferência é um passo próprio, em Python, fora do motor de teste do contrato.

## Veja também

- [Validação e qualidade]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/validacao_e_qualidade) — as outras camadas
- [Anatomia do YAML]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/anatomia_yaml)
- [Sincronização com a PNP]({{ site.baseurl }}/documentacao/usuarios-especializados/contratos/sincronizacao_pnp) — o que popula os cadastros locais
- [Quando algo falha]({{ site.baseurl }}/documentacao/coletor/quando_algo_falha)
