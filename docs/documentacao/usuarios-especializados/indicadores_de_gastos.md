---
layout: default
title: "Indicadores de Gastos"
toc: true
---

# {{ page.title }}

* TOC
{:toc}


### Gastos correntes por matrícula equivalente (GACM)
</h3>
<table>
  <tr>
    <th colspan="2"><strong><i>
      Gastos correntes por matrícula equivalente (GACM)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      Este indicador apresenta o valor médio investido para cada matrícula equivalente na RFEPCT. Em virtude da impossibilidade de segregar os dados financeiros das Escolas Técnicas Vinculadas às Universidades Federais (ETV-UF), este indicador não considera os dados das ETV-UF.
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
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
    <td>
      <strong>Agregação Mínima:</strong> Instituição.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>GCMeq</mi>
            <mo>=</mo>            
            <mfrac>
                <mi>GC</mi>
                <mi>Meq</mi>
            </mfrac>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>GC - Gasto Corrente.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong> Valor do Gasto Total com as Instituições que compõem a RFEPCT no ano base, excetuando-se gastos com:<ul>
      <li>Inativos e Pensionistas;</li> 
      <li>Investimentos;</li> 
      <li>Inversões Financeiras; e</li> 
      <li>Precatórios.</li></ul>
      <strong>Meq - Matrículas Equivalentes.</strong><br/>
      <strong>Fonte:</strong> PNP (SISTEC / CCV).<br/>
      <strong>Definição:</strong> Número de matrículas que estiveram ativas em pelo menos um dia no ano base, ponderada pelos fatores de equivalência previstos, exceto as matrículas das Escolas Técnicas Vinculadas às Universidades Federais.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Investimentos e inversões (GAIV)

<table>
  <tr>
    <th colspan="2"><strong><i>
      Investimentos e inversões (GAIV)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      Este indicador apresenta o valor dos gastos com grupos de natureza de despesa de investimentos e inversões das Instituições. Tais gastos se relacionam com aquisição de máquinas e equipamentos, realização de obras, aquisição de participações acionárias de empresas, aquisição e imóveis e concessão de empréstimos para investimento. Em virtude da impossibilidade de segregar os dados financeiros das Escolas Técnicas Vinculadas às Universidades Federais (ETV-UF), este indicador não considera os dados das ETV-UF.
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
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
    <td>
      <strong>Agregação Mínima:</strong> Instituição.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>GIV</mi>
            <mo>=</mo>            
            <mo>(</mo>
            <mi>GInv</mi>
            <mo>+</mo>
            <mi>GIF</mi>
            <mo>)</mo>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>GInv – Gastos com Investimentos.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong> Gasto do grupo de natureza de despesa “Investimentos” da Unidade Orçamentária no ano base.
      <br/>&nbsp;<br/>
      <strong>GIF – Gastos com Inversões Financeiras.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong> Gasto do grupo de natureza de despesa “Investimentos” da Unidade Orçamentária no ano base.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Outros Custeios (GAOC)

<table>
  <tr>
    <th colspan="2"><strong><i>
      Outros Custeios (GOC)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      Este indicador apresenta o valor dos gastos com outros custeios das Instituições, entendido como os gastos totais liquidados no exercício, deduzindo-se gastos com pessoal, benefícios, Pis/Pasep, investimentos e inversões financeiras. Em virtude da impossibilidade de segregar os dados financeiros das Escolas Técnicas Vinculadas às Universidades Federais (ETV-UF), este indicador não considera os dados das ETV-UF. 
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
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
    <td>
      <strong>Agregação Mínima:</strong> Instituição.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>GOC</mi>
            <mo>=</mo>
            <mo>(</mo>
            <msub>
              <mi>G</mi>
              <mi>OC</mi>
            </msub>
            <mo>)</mo>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>G<sub>OC</sub> - Gasto com Outros Custeios.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong>  Gasto no grupo de natureza de despesas “Outras despesas correntes” no ano base, com as Instituições que compõem a RFEPCT, deduzindo-se gastos com benefícios pagos aos servidores. 
      </td>
  </tr>
</table>
<p>&nbsp;</p>



### Gastos de Pessoal (GPE)

<table>
  <tr>
    <th colspan="2"><strong><i>
      Gastos de Pessoal (GPE)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      Este indicador diz respeito ao total de gastos com pessoal na RFEPCT. Apresenta o valor dos gastos com o grupo de natureza de despesa “pessoal” e as naturezas de despesa relativas a auxílios e congêneres. Em virtude da impossibilidade de segregar os dados financeiros das Escolas Técnicas Vinculadas às Universidades Federais (ETV-UF), este indicador não considera os dados das ETV-UF.
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
      <strong>Agregação máxima:</strong> Rede Federal.
    </td>
    <td>
      <strong>Agregação Mínima:</strong> Instituição.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>GPE</mi>
            <mo>=</mo>            
            <mo>(</mo>
            <mi>GFP</mi>
            <mo>+</mo>
            <mi>GaB</mi>
            <mo>)</mo>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>GFP - Gasto com remuneração de servidores.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong> Gasto com remuneração de ativos e aposentados no ano base, com as Instituições que compõem a RFEPCT. 
      <br/>&nbsp;<br/>
      <strong>GaB – Gastos com benefícios pagos aos servidores.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong> Gasto com pagamento de benefícios de ativos e aposentados no ano base, com as Instituições que compõem a RFEPCT.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Gasto com precatórios (GPRE)

<table>
  <tr>
    <th colspan="2"><strong><i>
      Gasto com precatórios (GPRE)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      Este indicador apresenta o valor de precatórios judiciais durante o ano base. 
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
      <strong>Agregação máxima:</strong> RFEPCT.
    </td>
    <td>
      <strong>Agregação Mínima:</strong> Instituição.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>GPRE</mi>
            <mo>=</mo>
            <mo>∑</mo>
            <mi>GPrec</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>GPrec = Gastos com precatórios.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong> Valor correspondente aos pagamentos de requisições judiciais (precatórios) realizados. Refere-se às liquidações totais (exercício + RAP), cujo elemento de despesa é o código “91” (sentenças judiciais).
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Gastos com inativos e pensionistas (GIP)

<table>
  <tr>
    <th colspan="2"><strong><i>
      Gastos com inativos e pensionistas (GIP)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      Este indicador apresenta o valor relativo aos gastos com pessoal, exclusivamente com servidores inativos e pensionistas.
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
      <strong>Agregação máxima:</strong> RFEPCT.
    </td>
    <td>
      <strong>Agregação Mínima:</strong> Instituição.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>GIP</mi>
            <mo>=</mo>
            <mo>∑</mo>
            <mi>Inat</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>Inat – Inativos e pensionistas.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong> Valor com Inativos, que compreende o conjunto de servidores aposentados, instituidores de pensão e seus respectivos pensionistas, cujos gastos são identificados pelos códigos de ação orçamentária “0181”.
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Gastos correntes (GC)

<table>
  <tr>
    <th colspan="2"><strong><i>
      Gastos correntes (GC)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      Este indicador apresenta o valor de gastos totais, excluindo precatórios, gastos com inativos e pensionistas, investimentos e inversões financeiras.
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
      <strong>Agregação máxima:</strong> RFEPCT.
    </td>
    <td>
      <strong>Agregação Mínima:</strong> Instituição.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>GC</mi>
            <mo>=</mo>
            <mo>∑</mo>
            <mi>Gasto corrente</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>GC - Gasto Corrente.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong> Valor do Gasto Total com as Instituições que compõem a RFEPCT no ano base, excetuando-se gastos com:<ul>
      <li>Inativos e Pensionistas;</li> 
      <li>Investimentos;</li> 
      <li>Inversões Financeiras; e</li> 
      <li>Precatórios.</li></ul>
    </td>
  </tr>
</table>
<p>&nbsp;</p>



### Gastos totais (GT)

<table>
  <tr>
    <th colspan="2"><strong><i>
      Gastos totais (GT)
    </i></strong></th>
  </tr>
  <tr>
    <td colspan="2">
      Este indicador apresenta o valor total de liquidações de gastos correntes, excluindo valores relacionados ao Pis-Pasep. 
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
      <strong>Agregação máxima:</strong> RFEPCT.
    </td>
    <td>
      <strong>Agregação Mínima:</strong> Instituição.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <strong>Modelo matemático:</strong><br/>
      <p style="text-align:center">
        <math style="font-size: 1.2rem;" display="block">
          <mrow>
            <mi>GT</mi>
            <mo>=</mo>
            <mo>∑</mo>
            <mi>Gasto totais</mi>
          </mrow>
        </math>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p style="text-align:center"><strong>Variáveis</strong></p>
      <strong>Gastos totais.</strong><br/>
      <strong>Fonte:</strong> SIAFI.<br/>
      <strong>Definição:</strong>  Valor total de liquidações de gastos correntes, excluindo valores relacionados ao Pis-Pasep.
    </td>
  </tr>
</table>