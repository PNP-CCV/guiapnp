---
layout: default
title: "Situações de matrícula e matrícula atendida"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas]({{ site.baseurl }}/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »]({{ site.baseurl }}/documentacao/caminho_do_arquivo) 
-->

# {{ page.title }}

Alguns indicadores usam o número de matrículas. A fonte desse dado é o cadastro gerenciado pelo Sistec. Ao ser adicionado um estudante em um ciclo, o *status* dessa matrícula é automaticamente atribuído como “em curso”. Contudo, dependendo da trajetória do estudante no ciclo, esse status pode receber atualizações. Na PNP, foram criadas categorias de situação de matrícula, baseadas no nome da situação oriunda dos Ciclos de Coleta e Validação, conforme exibido no quadro abaixo.

<div style="overflow-x: auto;">
<table style="border-collapse: collapse; width: 100%; table-layout: fixed;">
  <thead>
    <tr>
      <th style="width: 25%; word-wrap: break-word;">Categoria da situação de matrícula</th>
      <th style="width: 25%; word-wrap: break-word;">Nome da situação de matrícula</th>
      <th style="width: 50%; word-wrap: break-word;">Descrição do <em>status</em> no Sistec</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Em curso</td>
      <td>Em curso</td>
      <td>Aplica-se ao estudante quando matriculado.</td>
    </tr>
    <tr>
      <td rowspan="2">Concluintes</td>
      <td>Concluída</td>
      <td>Aplica-se ao estudante que concluiu todo o curso com êxito.</td>
    </tr>
    <tr>
      <td>Integralizada</td>
      <td>Aplica-se ao estudante que concluiu a parte teórica<br>do curso, mas falta estágio obrigatório, TCC,<br>monografia, dissertação ou tese.</td>
    </tr>
    <tr>
      <td rowspan="4">Evadidos</td>
      <td>Desligada</td>
      <td>Aplica-se ao estudante que solicita formalmente<br>o cancelamento da sua matrícula.</td>
    </tr>
    <tr>
      <td>Abandono</td>
      <td>Aplica-se ao estudante que evadiu o curso.</td>
    </tr>
    <tr>
      <td>Transf. externa</td>
      <td>Aplica-se ao estudante transferido para<br>outra unidade acadêmica.</td>
    </tr>
    <tr>
      <td>Transf. interna</td>
      <td>Aplica-se ao estudante que muda de curso,<br>dentro da mesma unidade acadêmica.</td>
    </tr>
  </tbody>
</table>
</div>

<p>&nbsp;</p>

Na PNP, uma fórmula é utilizada para contabilizar todas as matrículas que estavam ativas no ano base, seja porque os alunos ainda estão cursando ou porque a mudança de situação –como conclusão ou desligamento ocorreu durante o ano base. Assim, é necessário analisar o nome da situação e a data da situação. A data da situação é a data que constava originalmente no “mês de ocorrência” do Sistec. 

Ambos os dados, data de situação e o nome da situação, podem ter sido corrigidos durante os Ciclos de Coleta e Validação (CCV). Por isso, é importante salientar que o CCV considera o dado que foi informado nos anos anteriores no CCV também. Por exemplo, matrículas que foram alteradas no CCV para situações finais, não serão recarregadas para análise de inconsistências pois já alcançaram uma situação terminativa. Apenas as matrículas que estavam “em curso” na edição anterior do CCV e as que não estavam presentes na base de dados do CCV é que serão consideradas para verificação de matrícula atendida do ano corrente. 

Por exemplo, cursos, ciclos ou matrículas que foram excluídas ou validadas pela Instituição nas edições anteriores do CCV com situação de integralizada, desligada, abandono, reprovada, concluída ou transferida não serão consideradas na análise do ciclo vigente, mesmo que no Sistec permaneçam erroneamente em curso, visto que a Instituição atualizou no CCV mas não as atualizou no Sistec. O quadro abaixo exemplifica as situações de matrícula e a explicação acerca do cômputo como matrícula atendida após correções de inconsistências no CCV para o ano base 2024. 

<div style="overflow-x: auto;">
<table style="border-collapse: collapse; width: 100%; table-layout: fixed;">
  <thead>
    <tr>
      <th style="width: 15%; word-wrap: break-word;">Data de matrícula</th>
      <th style="width: 20%; word-wrap: break-word;">Nome da Situação em <br>25/01/2025</th>
      <th style="width: 15%; word-wrap: break-word;">Data da situação</th>
      <th style="width: 50%; word-wrap: break-word;">Matrícula atendida?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>01/03/2018</td>
      <td>Em curso</td>
      <td>01/03/2018</td>
      <td>Sim, porque está "Em curso" no ano de referência – 2024 e foi ratificada a retenção crítica no CCV – retidos há mais de um ano.</td>
    </tr>
    <tr>
      <td>25/04/2019</td>
      <td>Concluída</td>
      <td>04/01/2024</td>
      <td>Sim, porque embora não esteja "Em curso", a mudança de situação ocorreu no ano de referência – 2024.</td>
    </tr>
    <tr>
      <td>20/02/2023</td>
      <td>Desligada</td>
      <td>30/12/2024</td>
      <td>Sim, porque embora não esteja "Em curso", a mudança de situação ocorreu no ano de referência – 2024.</td>
    </tr>
    <tr>
      <td>05/01/2025</td>
      <td>Em curso</td>
      <td>05/01/2025</td>
      <td>Não, porque embora esteja "Em curso", a data da situação não ocorreu no ano de referência.</td>
    </tr>
    <tr>
      <td>15/04/2023</td>
      <td>Concluída</td>
      <td>31/12/2023</td>
      <td>Não, porque a mudança de situação não ocorreu no ano de referência.</td>
    </tr>
  </tbody>
</table>
</div>

<p>&nbsp;</p>

As situações descritas no quadro acima são verificadas em dois momentos: no processo de merge e após a conclusão da edição do CCV. Dessa forma, as alterações nas datas de ocorrência das matrículas durante o CCV podem interferir no corte final usado na disseminação. Além das situações descritas no quadro acima, caso a matrícula seja excluída ou substituída, após o CCV, a matrícula deixará de ser atendida. A mesma situação acontece com todas as matrículas vinculadas a cursos e ciclos excluídos durante o CCV.
