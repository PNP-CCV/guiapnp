---
layout: default
title: "Indicadores de Ensino"
toc: true
---

# {{ page.title }}

* TOC
{:toc}


### Índice de eficiência acadêmica (ENIEA)

As matrículas para o cálculo do indicador Índice de Eficiência Acadêmica diferem das matrículas utilizadas em outros indicadores, pois não são considerados apenas os dados do ano-base, mas sim os dados reunidos por “ciclos de matrícula”. Um ciclo de matrícula envolve a oferta de um curso com uma carga horária definida, com mesma data de início e mesma previsão de término, visando englobar um conjunto de matrículas para obtenção de uma mesma certificação ou diploma. A análise dos indicadores “por ciclo” será realizada considerando a situação de matrícula com fim de ciclo previsto para o ano anterior ao de referência.

Considerando o conjunto de estudantes ingressantes no início de um determinado ciclo no momento de análise, cada um poderá se enquadrar em apenas uma das três situações de matrícula:
- **Evadido**: estudante que perdeu o vínculo com a instituição antes da conclusão do curso.
- **Retido**: estudante que permaneceu com situação de matrícula “em curso” por período superior ao tempo previsto para a integralização do curso.
- **Concluinte**: estudante que concluiu com êxito todos os componentes curriculares do curso ou com situação de matrícula “integralizada”, ou seja, que concluiu a carga horária das unidades curriculares mas ainda não pode obter a certificação por não ter concluído estágio, Trabalho de Conclusão de Curso, não ter realizado o Exame Nacional de Desempenho dos Estudantes (Enade), entre outros.
<p/>

<strong><u>Exemplo</u></strong>:<br/>

Um curso Técnico em Edificações Integrado ao Ensino Médio com duração prevista para quatro anos teve quarenta ingressantes em janeiro de 2020, e, portanto, seu “ciclo encerrado” em dezembro de 2023. Neste caso, o método de análise da PNP prevê que, em 31 de dezembro de 2024 (final do ano posterior ao término do ciclo iniciado em 2020), seja realizada a análise da situação de matrícula dos quarenta estudantes ingressantes em janeiro de 2020. Realizada esta análise, os estudantes apresentaram as seguintes situações de matrícula: 
- dezesseis (40%) concluíram todos os componentes curriculares (Formados);
- quatro (10%), todas as unidades curriculares, mas ainda não poderiam receber a certificação (Integralizados).
- oito (20%) perderam o vínculo com a instituição (Evadidos);
- doze (30%) ainda estavam matriculados em alguma das unidades curriculares (Retidos).
<p/>

Com base neste exemplo, a PNP apresentaria os seguintes resultados no ano base 2024: 
- Conclusão por Ciclo = 50% (matrículas concluídas+ integralizadas) 
- Evasão por Ciclo = 20% 
- Retenção por Ciclo = 30%
<p/>

O cálculo do indicador de Eficiência Acadêmica deve avaliar a capacidade de a Rede Federal de Educação Profissional, Científica e Tecnológica (RFEPCT) atingir os resultados previstos em termos de “estudantes certificados” ou “com potencial de certificação” em relação à quantidade total de matrículas, considerando um determinado ciclo de matrículas. Para fazer esta projeção, a PNP identificou o quanto representam os “concluintes (50%)” no total de “concluintes mais evadidos (50% + 20%)”, criando um ponderador que busca projetar o percentual de retidos que provavelmente concluirão seu curso em algum momento posterior ao ano base, multiplicando pela quantidade de retidos.

Dessa forma, com base nos dados do exemplo, o indicador teria como resultado 50 + [(50/(50+20))x30] = 71.42%

<table>
  <tr>
    <th colspan="2"><strong><i>
      Índice de eficiência acadêmica (ENIEA)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede o percentual de estudantes que concluíram o curso com êxito dentro do período previsto ou até o dia 31 de dezembro do ano posterior ao término do ciclo iniciado, acrescido de um percentual (projeção) dos estudantes retidos no ano base que poderão concluir o curso. São considerados apenas os estudantes matriculados em ciclos de matrícula com término previsto para o ano anterior ao ano base. Para este cálculo é empregado o conceito de matrícula, e não de matrícula equivalente. 
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Ciclo.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
            <mrow>
              <mi>ENIEA [%]</mi>
              <mo>=</mo>
              <mrow>
                <mi>CCiclo</mi>
                <mo>+</mo>
                <mrow>
                  <mo>[</mo>
                  <mrow>
                    <mo>(</mo>
                    <mfrac>
                      <mrow>
                        <mi>CCiclo</mi>
                      </mrow>
                      <mrow>
                        <mi>CCiclo</mi>
                        <mo>+</mo>
                        <mi>EvCiclo</mi>
                      </mrow>
                    </mfrac>
                    <mo>)</mo>
                    <mo>&#xD7;</mo>
                    <mi>RCiclo</mi>
                  </mrow>
                  <mo>]</mo>
                </mrow>
                <mo>&#xD7;</mo>
                <mn>100</mn>
              </mrow>
            </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>CCiclo [%] - Conclusão por Ciclo</strong><br/>
      <strong>Fonte:</strong> PNP.<br/>
      <strong>Definição:</strong> Percentual de CONCLUINTES (definido pelos status “Concluído” ou “Integralizado em fase escolar”), em relação às matrículas vinculadas aos ciclos concluídos no ano anterior ao ano base.
      <br/>&nbsp;<br/>
      <strong>EvCiclo [%] - Evasão por Ciclo</strong><br/>
      <strong>Fonte:</strong> PNP.<br/>
      <strong>Definição:</strong> Percentual de EVADIDOS, em relação às matrículas vinculadas aos ciclos concluídos no ano anterior ao ano base.
      <br/>&nbsp;<br/>
      <strong>RCiclo [%] - Retenção por Ciclo</strong><br/>
      <strong>Fonte:</strong> PNP.<br/>
      <strong>Definição:</strong> Percentual de matriculados que são classificados como RETIDOS por terem ultrapassado o período previsto para integralização do curso (acrescido de um ano) em relação às matrículas vinculadas aos ciclos concluídos no anterior ao Ano base.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Índice de verticalização (ENIV)

O indicador é calculado em nível de Eixo Tecnológico, com seu modelo matemático expresso na ficha a seguir de acordo com essa configuração. A representação do Índice de Verticalização em formas agregadas superiores (Unidade, Instituição) na PNP é baseada no cálculo da média das formas agregadas imediatamente inferiores.

Nesse indicador, avalia-se a verticalização sobre dois aspectos:
<ol type="a">
  <li><strong>Análise vertical</strong>: Verifica se uma mesma unidade ofereceu vagas, no ano base, em cursos de diferentes “níveis” dentro do mesmo Eixo Tecnológico;</li>
  <li><strong>Análise horizontal</strong>: Verifica se a unidade ofereceu mais vagas nos “níveis mais básicos” quando se analisam as quatro categorias duas a duas.</li>
</ol>

A partir destas possibilidades, emprega-se um percentual de prioridades:
<table>
  <tr>
    <th><strong>Categoria</strong></th>
    <th><strong>Prioridade</strong></th>
    <th><strong>Classificação</strong></th>
  </tr>
  <tr>
    <td>Qualificação Profissional – Técnico</td>
    <td>39,7%</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Técnico – Graduação</td>
    <td>36,5%</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Graduação - Pós-graduação</td>
    <td>9,5%</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Qualificação Profissional - Graduação</td>
    <td>8,9%</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Técnico – Pós-graduação</td>
    <td>2,8%</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Qualificação Profissional – Pós-Graduação</td>
    <td>2,6%</td>
    <td>6</td>
  </tr>
</table>

<br/>
<table>
  <tr>
    <th colspan="2"><strong><i>
      Índice de verticalização (ENIV)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador busca verificar a condição de verticalização dos cursos oferecidos por uma mesma unidade acadêmica em um mesmo eixo tecnológico, considerando vagas de ingresso ofertadas em 04 categorias possíveis: Curso de Qualificação Profissional (QP); Curso Técnico (CT); Curso de Graduação (CG) e Curso de Pós-Graduação (PG).  
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Eixo Tecnológico.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Eixo Tecnológico.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
            <mrow>
              <mi>ENIV</mi>
              <mo>=</mo>
              <mrow>
                <mo>[</mo>
                <mrow>
                  <mo>(</mo>
                  <mfrac>
                    <mi>VQP</mi>
                    <mi>VCT</mi>
                  </mfrac>
                  <mo>)</mo>
                  <mo>&#xD7;</mo>
                  <mn>0,397</mn>
                </mrow>
                <mo>]</mo>
              </mrow>
              <mo>+</mo>
              <mrow>
                <mo>[</mo>
                <mrow>
                  <mo>(</mo>
                  <mfrac>
                    <mi>VCT</mi>
                    <mi>VCG</mi>
                  </mfrac>
                  <mo>)</mo>
                  <mo>&#xD7;</mo>
                  <mn>0,365</mn>
                </mrow>
                <mo>]</mo>
              </mrow>
              <mo>+</mo>
              <mrow>
                <mo>[</mo>
                <mrow>
                  <mo>(</mo>
                  <mfrac>
                    <mi>VCG</mi>
                    <mi>VPG</mi>
                  </mfrac>
                  <mo>)</mo>
                  <mo>&#xD7;</mo>
                  <mn>0,095</mn>
                </mrow>
                <mo>]</mo>
              </mrow>
              <mo>+</mo>
              <mrow>
                <mo>[</mo>
                <mrow>
                  <mo>(</mo>
                  <mfrac>
                    <mi>VCT</mi>
                    <mi>VPG</mi>
                  </mfrac>
                  <mo>)</mo>
                  <mo>&#xD7;</mo>
                  <mn>0,089</mn>
                </mrow>
                <mo>]</mo>
              </mrow>
            </mrow>
          </math>
          <math style="font-size: 1.2rem;" display="block">
            <mrow>
              <mo linebreak="goodbreak">+</mo>
              <mrow>
                <mo>[</mo>
                <mrow>
                  <mo>(</mo>
                  <mfrac>
                    <mi>VQP</mi>
                    <mi>VCG</mi>
                  </mfrac>
                  <mo>)</mo>
                  <mo>&#xD7;</mo>
                  <mn>0,028</mn>
                </mrow>
                <mo>]</mo>
              </mrow>
              <mo>+</mo>
              <mrow>
                <mo>[</mo>
                <mrow>
                  <mo>(</mo>
                  <mfrac>
                    <mi>VQP</mi>
                    <mi>VPG</mi>
                  </mfrac>
                  <mo>)</mo>
                  <mo>&#xD7;</mo>
                  <mn>0,026</mn>
                </mrow>
                <mo>]</mo>
              </mrow>
            </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>VQP - Vagas Qualificação Profissional</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de Vagas ofertadas em cursos de Qualificação Profissional.
      <br/>&nbsp;<br/>
      <strong>VCT - Vagas Cursos Técnicos</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de Vagas ofertadas em cursos Técnicos, considerando os cursos Integrados, Subsequentes e Concomitantes.
      <br/>&nbsp;<br/>
      <strong>VCG - Vagas Curso Graduação</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de Vagas ofertadas em cursos de Graduação, considerando os cursos de Tecnologia, Bacharelados e Licenciaturas.
      <br/>&nbsp;<br/>
      <strong>VPG - Vagas Pós-Graduação </strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de Vagas ofertadas em cursos de Pós-Graduação, considerando Especialização <i>Lato Sensu</i>, Mestrados e Doutorados.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de concluintes (ENCT)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de concluintes (ENCT)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número total de matrículas concluídas no ano base, considerando todos os cursos e modalidades ofertados.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Ciclo.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENCT</mi>
            <mo>=</mo>
            <mi>CT</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>CT</strong> = Número total de matrículas concluídas no ano base.<br/>
      <strong>Fonte:</strong> PNP (CCV).<br/>
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de cursos (ENC)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de cursos (ENC)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número total de cursos ofertados no ano base, considerando todos os tipos e modalidades.  
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Estrutura com matrícula.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENC</mi>
            <mo>=</mo>
            <mo>∑</mo>
            <mi>TC</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>Tipos de cursos ofertados (TC):</strong><br/>
      <ul>
        <li>ABI - Área Básica de Ingresso</li>
        <li>Educação Infantil</li>
        <li>Ensino Fundamental I</li>
        <li>Ensino Fundamental II</li>
        <li>Ensino Médio</li>
        <li>Qualificação Profissional (FIC)</li>
        <li>Técnico</li>
        <li>Especialização Técnica</li>
        <li>Bacharelado</li>
        <li>Licenciatura</li>
        <li>Tecnologia</li>
        <li>Especialização (Lato Sensu)</li>
        <li>Mestrado</li>
        <li>Mestrado Profissional</li>
        <li>Doutorado</li>
        <li>Doutorado Profissional</li> 
      </ul>
      <strong>Fonte:</strong> PNP (CCV).<br/>
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de estruturas com matrícula (ENEMA)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de estruturas com matrícula (ENEMA)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número de estruturas, de diferentes tipos, que possuem matrícula vinculada no ano base.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Estrutura com matrícula.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENEMA</mi>
            <mo>=</mo>
            <mo>∑</mo>
            <mi>TEMA</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>Tipos de estrutura com matrícula (TEMA):</strong><br/>
      <ul>
        <li>Campi</li>
        <li>Centros de Referência</li>
       <li>Escolas Técnicas vinculadas às universidades</li>
      </ul>
      <strong>Fonte:</strong> PNP (CCV).<br/>
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de evadidos (ENEV)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de evadidos (ENEV)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número total de matrículas evadidas no ano base.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto menor, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Estrutura com matrícula.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENEV</mi>
            <mo>=</mo>
            <mi>EV</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>EV</strong> = Número total de matrículas evadidas no ano base.<br/>
      <strong>Fonte:</strong> PNP (CCV).<br/>
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de ingressantes (ENING)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de ingressantes (ENING)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número total de matrículas que ingressaram no ano base, considerando todos os cursos e modalidades ofertados. 
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Ciclo.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENING</mi>
            <mo>=</mo>
            <mi>ING</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>ING</strong> = Número de matrículas cuja data de início ocorreu no ano base.<br/>
      <strong>Fonte:</strong> PNP (CCV).<br/>
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de inscritos (ENIC)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de inscritos (ENIC)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número total de candidatos inscritos nos processos de ingresso da instituição no ano base, considerando todos os cursos e modalidades ofertados.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Ciclo.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENIC</mi>
            <mo>=</mo>
            <mi>IC</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>IC</strong> = Número de candidatos que se inscreveram para concorrer às vagas ofertadas pela instituição no ano base.<br/>
      <strong>Fonte:</strong> PNP (CCV).<br/>
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de matrículas (ENM) 
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de matrículas (ENM)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número total de matrículas no ano base, considerando todos os cursos e modalidades ofertados.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Ciclo.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENM</mi>
            <mo>=</mo>
            <mi>M</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>M</strong> = O conceito de matrícula consiste no número total de estudantes que estiveram matriculados no ano base por pelo menos um dia.<br/>
      <strong>Fonte:</strong> PNP (CCV).<br/>
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de matrículas equivalentes (ENME)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de matrículas equivalentes (ENME)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador converte o número de Matrículas de todos os tipos de cursos e modalidades de oferta em Matrículas Equivalentes, mediante o ajuste por fatores de equiparação de carga horária e de esforço do curso.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Ciclo.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENME</mi>
            <mo>=</mo>
            <mo>(</mo>
            <mi>M</mi>
            <mo>&#xD7;</mo>
            <mi>FECH</mi>
            <mo>&#xD7;</mo>
            <mi>FEC</mi>
            <mo>)</mo>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>M - Matrículas</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de estudantes que estiveram com matrícula ativa em pelo menos um dia no ano base.
      <br/>&nbsp;<br/>
      <strong>FECH - Fator de Equiparação de Carga Horária</strong><br/>
      <strong>Fonte:</strong> Anexo II da Portaria nº 146/2021.<br/>
      <strong>Definição:</strong> Calculado pela razão entre a carga horária mínima regulamentada do curso e carga horária padrão de 800 horas anuais. Para os demais cursos, o fator de equiparação de carga horária será igual a 1 (um).
      <br/>&nbsp;<br/>
      <strong>FEC - Fator de Esforço de Curso </strong><br/>
      <strong>Fonte:</strong> Anexo II da Portaria nº 146/2021.<br/>
      <strong>Definição:</strong> Ajusta a contagem de matrículas-equivalentes para cursos que demandem, para o desenvolvimento de suas atividades, uma menor relação matrículas por professor.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de unidades acadêmicas (ENUND)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de unidades acadêmicas (ENUND)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número total de unidades acadêmicas.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Não definido.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Instituição.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENUND</mi>
            <mo>=</mo>
            <mo>∑</mo>
            <mi>Unidades</mi>
            <mtext>, nos diferentes níveis de agregação</mtext>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>Unidades</strong><br/>
      <strong>Fonte:</strong> PNP (CCV).<br/>
      <strong>Definição:</strong> estrutura que possui ato normativo de autorização de funcionamento, expedido pelo Ministério da Educação, tendo finalidade acadêmica. São consideradas unidades: Campus, Campus Avançado, Escola Técnica Vinculada a Universidade Federal, Polo de Inovação, Sede e Uned.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Número de vagas (ENV)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Número de vagas (ENV)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número total de vagas disponibilizadas no ano base, considerando todos os cursos e modalidades ofertados.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Ciclo.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENV</mi>
            <mo>=</mo>
            <mi>V</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>V</strong> = Número total de vagas. As vagas representam a capacidade da instituição de ensino em receber novos alunos e estão diretamente relacionadas à sua infraestrutura, corpo docente e recursos pedagógicos, sendo geralmente definidas por critérios quantitativos e qualitativos e previstos no Plano de Desenvolvimento Institucional.<br/>
      <strong>Fonte:</strong> PNP (CCV).<br/>
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Percentual de conclusão por ciclo (ENCC)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Percentual de conclusão por ciclo (ENCC)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede o percentual de concluintes em um ciclo de matrícula. Para este cálculo é empregado o conceito de matrícula, e não de matrícula equivalente. 
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Quanto maior, melhor.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Curso.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENCC [%]</mi>
            <mo>=</mo>
            <mrow>
              <mfrac>
                <mi>CCiclo</mi>
                <mi>MCiclo</mi>
              </mfrac>
              <mo>&#xD7;</mo>
              <mn>100</mn>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>CCiclo – Concluintes no Ciclo</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de estudantes com status “Concluído” (alunos que concluíram com êxito todos os componentes curriculares do curso no ano base, fazendo jus à certificação), e o número de alunos com situação “Integralizados em fase escolar” (alunos que concluíram a carga horária da unidades curriculares e ainda não podem receber a certificação por não terem concluído componentes como Estágio, TCC e ENADE), considerando apenas as matrículas vinculadas a ciclos de matrícula com término previsto para o ano anterior ao Ano base.
      <br/>&nbsp;<br/>
      <strong>MCiclo - Matrículas no Ciclo</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas efetuadas no início do ciclo de matrícula.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Percentual de evasão anual (ENEVA)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Percentual de evasão anual (ENEVA)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede o percentual de matrículas que perderam o vínculo com a instituição no ano base sem a conclusão do curso em relação ao total de matrículas. Para este cálculo é empregado o conceito de matrícula e não de matrícula equivalente.  
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> 10% - derivado da análise das estratégias 11.11 e 12.3 previstas na Lei 13.005/2014.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Quanto menor, melhor.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Curso.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENEVA [%]</mi>
            <mo>=</mo>
            <mrow>
              <mfrac>
                <mi>Ev</mi>
                <mi>M</mi>
              </mfrac>
              <mo>&#xD7;</mo>
              <mn>100</mn>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>Ev – Evadidos</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas que perderam vínculo com a instituição antes da conclusão do curso.
      <br/>&nbsp;<br/>
      <strong>M – Matrículas</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de estudantes que estiveram com matrícula ativa em pelo menos um dia no ano base.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Percentual de evasão por ciclo (ENEC)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Percentual de evasão por ciclo (ENEC)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede o percentual de evadidos em um ciclo de matrícula. Para este cálculo é empregado o conceito de matrícula, e não de matrícula equivalente.  
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Quanto menor, melhor.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Curso.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENEC [%]</mi>
            <mo>=</mo>
            <mrow>
              <mfrac>
                <mi>EvCiclo</mi>
                <mi>MCiclo</mi>
              </mfrac>
              <mo>&#xD7;</mo>
              <mn>100</mn>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>EvCiclo – Evadidos no Ciclo</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de estudantes que perderam vínculo com a instituição antes da conclusão do curso, considerando apenas as matrículas vinculadas a ciclos com término previsto para o ano anterior ao ano base.
      <br/>&nbsp;<br/>
      <strong>MCiclo - Matrículas no Ciclo</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas efetuadas no início do ciclo de matrícula.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Percentual de retenção por ciclo (ENREC)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Percentual de retenção por ciclo (ENREC)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede o percentual de retidos em um ciclo de matrícula. Para este cálculo é empregado o conceito de matrícula, e não de matrícula equivalente.  
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Quanto menor, melhor.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Curso.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENREC [%]</mi>
            <mo>=</mo>
            <mrow>
              <mfrac>
                <mi>RCiclo</mi>
                <mi>MCiclo</mi>
              </mfrac>
              <mo>&#xD7;</mo>
              <mn>100</mn>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>RCiclo – Retidos no Ciclo</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de estudantes que permaneceram matriculados por período superior ao tempo previsto para a integralização do curso (acrescido de um ano), considerando apenas as matrículas vinculadas a ciclos de matrícula com término previsto para o ano anterior ao ano base.
      <br/>&nbsp;<br/>
      <strong>MCiclo - Matrículas no Ciclo</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas efetuadas no início do ciclo de matrícula.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Relação de inscritos por vagas (ENRIV)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Relação de inscritos por vagas (ENRIV)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede a relação entre o número de candidatos inscritos e o número de vagas disponibilizadas. 
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Não há meta prevista em instrumento normativo.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Quanto maior, melhor.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Curso.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ENRIV</mi>
            <mo>=</mo>
            <mrow>
              <mfrac>
                <mi>I</mi>
                <mi>V</mi>
              </mfrac>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>I – Inscritos</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de candidatos que concorreram às vagas disponibilizadas para a fase inicial dos cursos, em suas diversas formas de ingresso, no ano base.
      <br/>&nbsp;<br/>
      <strong>V – Vagas</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de vagas disponibilizadas para a fase inicial dos cursos, em suas diversas formas de ingresso, no ano base.
    </td>
  </tr>
</table>
<p>&nbsp;</p>


### Taxa de Ocupação
<table>
  <tr>
    <th colspan="2"><strong><i>
      Este indicador foi removido da PNP para reanálise de seu modelo matemático.
    </i></strong></th>
  </tr>
</table>

<!-- OMITIDOS NO AJUSTE DO DIA 22 DE AGOSTO DE 2026

### Reserva de vagas (RV)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Reserva de vagas (RV)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o percentual de vagas ofertadas por cotas nos cursos técnicos e de graduação, conforme classificações definidas na Lei das Cotas (Lei 12.711/2012) e alterações. 
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> 50% - Art. 1º da Lei 12.711/2012, com redação dada pelas Leis 14.723/2023 e 14.945/2024.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Crescente (quanto maior, melhor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Curso.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>RV</mi>
            <mo>=</mo>
            <mo>(</mo>
            <mrow>
              <mfrac>
                <mi>VC</mi>
                <mrow>
                  <mi>VAC</mi>
                  <mo>+</mo>
                  <mi>VC</mi>
                </mrow>  
              </mfrac>
              <mo>)</mo>
              <mo>&#xD7;</mo>
              <mn>100</mn>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>VC - Vagas de Cotas</strong><br/>
      <strong>Fonte:</strong> PNP (CCV).<br/>
      <strong>Definição:</strong> Número de vagas disponibilizadas para a fase inicial dos cursos e reservadas para que estudantes de escolas públicas, estudantes negros, pardos, indígenas, quilombolas, pessoas com deficiência e estudantes oriundos de famílias com renda per capita inferior a 1 salário mínimo tenham acesso ao ensino técnico e de graduação, conforme disposto na Lei 12.711/2012 e alterações.
      <br/>&nbsp;<br/>
      <strong>VAC - Vagas de Ampla Concorrência</strong><br/>
      <strong>Fonte:</strong> PNP (CCV).<br/>
      <strong>Definição:</strong> Número de vagas disponibilizadas para a fase inicial dos cursos e destinadas para acesso ao público geral, no ano base. Consideram-se apenas as vagas nos cursos técnicos e de graduação.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Formas de Ingresso (FIng)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Formas de Ingresso (FIng)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador apresenta o número de matrículas classificadas por forma de ingresso, conforme categorias definidas na Lei das Cotas (Lei 12.711/2012) e alterações. 
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> 50% - Art. 1º da Lei 12.711/2012, com redação dada pela Lei 14.723/2023.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> não se aplica.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação mínima:</strong> Rede Federal.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático: *</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>FIng</mi>
            <mo>=</mo>
            <mo>[</mo>
            <mrow>
              <mi>AC</mi>
              <mo>, </mo>
              <msub><mi>LB</mi><mi>EP</mi></msub>
              <mo>, </mo>
              <msub><mi>LB</mi><mi>PCD</mi></msub>
              <mo>, </mo>
              <msub><mi>LB</mi><mi>PPI</mi></msub>
              <mo>, </mo>
              <msub><mi>LB</mi><mi>Q</mi></msub>
              <mo>, </mo>
              <msub><mi>LI</mi><mi>EP</mi></msub>
              <mo>, </mo>
              <msub><mi>LI</mi><mi>PCD</mi></msub>
              <mo>, </mo>
              <msub><mi>LI</mi><mi>PPI</mi></msub>
              <mo>, </mo>
              <msub><mi>LI</mi><mi>Q</mi></msub>
              <mo>, </mo>
              <mi>ND</mi>
            </mrow>
            <mo>]</mo> 
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>Formas de ingresso</strong><br/>
      <ul>
        <li><strong>AC</strong>: número de matrículas de ingressantes por ampla concorrência.</li>
        <li><strong>LB<sub>EP</sub></strong>: número de matrículas de ingressantes com renda familiar bruta per capita igual ou inferior a 1 salário mínimo que tenham cursado integralmente o ensino fundamental ou médio (conforme o nível de ingresso) em escolas públicas.</li>
        <li><strong>LB<sub>PCD</sub></strong>: número de matrículas de ingressantes com deficiência, que tenham renda familiar bruta per capita igual ou inferior a 1 salário mínimo e que tenham cursado integralmente o ensino fundamental ou médio (conforme o nível de ingresso) em escolas públicas.</li>
        <li><strong>LB<sub>PPI</sub></strong>: número de matrículas de ingressantes autodeclarados pretos, pardos ou indígenas, com renda familiar bruta per capita igual ou inferior a 1 salário mínimo e que tenham cursado integralmente o ensino fundamental ou médio (conforme o nível de ingresso) em escolas públicas.</li>
        <li><strong>LB<sub>Q</sub></strong>: número de matrículas de ingressantes autodeclarados quilombolas, com renda familiar bruta per capita igual ou inferior a 1 salário mínimo e que tenham cursado integralmente o ensino fundamental ou médio (conforme o nível de ingresso) em escolas públicas.</li>
        <li><strong>LI<sub>EP</sub></strong>: número de matrículas de ingressantes que, independentemente da renda, tenham cursado integralmente ensino fundamental ou médio (conforme o nível de ingresso) em escolas públicas.</li>
        <li><strong>LI<sub>PCD</sub></strong>: número de matrículas de ingressantes com deficiência, independentemente da renda, que tenham cursado integralmente o ensino fundamental ou médio (conforme o nível de ingresso) em escolas públicas.</li>
        <li><strong>LI<sub>PPI</sub></strong>: número de matrículas de ingressantes autodeclarados pretos, pardos ou indígenas, independentemente da renda, que tenham cursado integralmente o ensino fundamental ou médio (conforme o nível de ingresso) em escolas públicas.</li>
        <li><strong>LI<sub>Q</sub></strong>: número de matrículas de ingressantes autodeclarados quilombolas, independentemente da renda, que tenham cursado integralmente o ensino fundamental ou médio (conforme o nível de ingresso) em escolas públicas.</li>
        <li><strong>ND</strong>: número de matrículas de ingressantes sem informação da forma de ingresso.</li>
      </ul>
      <strong>Fonte:</strong> PNP (CCV).<br/>
      <strong>Definição:</strong> A classificação segundo formas de ingresso desdobra-se em dez categorias, conforme informado nos registros de ingresso dos estudantes.<br/>
      * Para alunos ingressantes até o ano base 2023, será utilizada a classificação descrita na Lei 12.711/2012, antes das alterações.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Matrículas Equivalentes em Cursos Técnicos (ALMTEC)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Matrículas Equivalentes em Cursos Técnicos (ALMTEC)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede o percentual de matrículas equivalentes vinculadas a Cursos Técnicos. É aplicável apenas aos Institutos Federais. 
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Mínimo de 50% - Art. 8º da Lei 11.892/2008.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Ultrapassado o mínimo estabelecido, quanto mais próximo do centro da meta, melhor.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Estrutura.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>Técnicos [%]</mi>
            <mo>=</mo>
            <mrow>
              <mfrac>
                <mi>MeqCT</mi>
                <mi>Meq</mi>
              </mfrac>
              <mo>&#xD7;</mo>
              <mn>100</mn>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>MeqCT – Matrículas Equivalentes em Cursos Técnicos</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas em cursos técnicos que estiveram ativas em pelo menos um dia no ano base, ponderada pelos fatores de equivalência previstos.
      <br/>&nbsp;<br/>
      <strong>Meq - Matrículas Equivalentes</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas que estiveram ativas em pelo menos um dia no ano base, ponderada pelos fatores de equivalência previstos.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Percentual de matrículas equivalentes em cursos de formação de professores (ALMPROF)

Os cursos de formação de professores incluídos neste indicador são aqueles classificados no eixo tecnológico “Desenvolvimento Educacional e Social”, que abrange áreas relacionadas à educação e ao desenvolvimento humano. O indicador considera apenas matrículas sem financiamento externo. Como tipos de cursos, são considerados licenciatura, qualificação profissional e pós-graduação.

<table>
  <tr>
    <th colspan="2"><strong><i>
      Percentual de matrículas equivalentes em cursos de formação de professores (ALMPROF)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede o percentual de matrículas equivalentes vinculadas à formação de professores. É aplicável apenas aos Institutos Federais.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Mínimo de 20% - Art. 8º da Lei 11.892/2008.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Ultrapassado o mínimo estabelecido, quanto mais próximo do centro da meta, melhor.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Estrutura.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>Formação de professores [%]</mi>
            <mo>=</mo>
            <mrow>
              <mfrac>
                <mi>MeqFP</mi>
                <mi>Meq</mi>
              </mfrac>
              <mo>&#xD7;</mo>
              <mn>100</mn>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>MeqFP - Matrículas Equivalentes em Formação de Professores.</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas em cursos destinados à formação de professores que estiveram ativas em pelo menos um dia no ano base, ponderada pelos fatores de equivalência previstos.
      <br/>&nbsp;<br/>
      <strong>Meq - Matrículas Equivalentes.</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas que estiveram ativas em pelo menos um dia no ano base, ponderada pelos fatores de equivalência previstos.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Percentual de matrículas equivalentes em cursos de educação de jovens e adultos articulada à educação profissional e tecnológica (ALMEJA)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Percentual de matrículas equivalentes em cursos de educação de jovens e adultos articulada à educação profissional e tecnológica (ALMEJA)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede o percentual de matrículas equivalentes na modalidade EJA, tanto nos cursos de Formação Inicial e Continuada de Trabalhadores (FIC) quanto nos cursos de educação profissional técnica de nível médio contemplados no programa nacional de integração da educação profissional com a educação básica na modalidade EJA (PROEJA / EJA Integrado). É aplicável apenas aos Institutos Federais.   
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> Mínimo de 10% - §1º do Art. 2º do Decreto 5.840/2.006.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Ultrapassado o mínimo estabelecido, quanto mais próximo do centro da meta, melhor.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Estrutura.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ALMEJA [%]</mi>
            <mo>=</mo>
            <mrow>
              <mfrac>
                <mi>MeqEJA</mi>
                <mi>Meq</mi>
              </mfrac>
              <mo>&#xD7;</mo>
              <mn>100</mn>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>MeqEJA - Matrículas Equivalentes em Educação de Jovens e Adultos.</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas em curso FIC ou técnico contemplado pelo programa PROEJA que estiveram ativas por pelo menos um dia no ano base, ponderada pelos fatores de equivalência previstos.
      <br/>&nbsp;<br/>
      <strong>Meq - Matrículas Equivalentes.</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas que estiveram ativas em pelo menos um dia no ano base, ponderada pelos fatores de equivalência previstos.
    </td>
  </tr>
</table>
<p>&nbsp;</p>




### Percentual de oferta de vagas em cursos de graduação noturna presencial (ALVGN)
<table>
  <tr>
    <th colspan="2"><strong><i>
      Percentual de oferta de vagas em cursos de graduação noturna presencial (ALVGN)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Definição:</strong> Este indicador mede o percentual de vagas de ingresso oferecidas nos cursos de graduação presencial para o turno noturno, em relação ao total de vagas de ingresso oferecidas nos cursos de graduação presencial.  
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Meta:</strong> 33,3% - Estratégia 12.3 da Lei 13.005/2014.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Polaridade:</strong> Ultrapassado o mínimo estabelecido, quanto mais próximo do centro da meta, melhor.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Agregação Mínima:</strong> Curso.
    </td>
    <td>
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>ALVGN [%]</mi>
            <mo>=</mo>
            <mrow>
              <mfrac>
                <mi>VGPN</mi>
                <mi>VGP</mi>
              </mfrac>
              <mo>&#xD7;</mo>
              <mn>100</mn>
            </mrow>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>VGPN – Vagas para cursos de graduação na modalidade presencial em turno noturno.</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de vagas de ingresso oferecidas no ano base para cursos de graduação na modalidade presencial no turno noturno.
      <br/>&nbsp;<br/>
      <strong>VGP – Total de vagas para cursos de graduação na modalidade presencial.</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de vagas de ingresso oferecidas no ano base para cursos de graduação na modalidade presencial.
    </td>
  </tr>
</table>
<p>&nbsp;</p>

-->