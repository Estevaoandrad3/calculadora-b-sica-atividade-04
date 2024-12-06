# calculadora-b-sica-atividade-04
//OBJETIVO: Este projeto tem como objetivo desenvolver uma calculadora simples para realizar operações matemáticas básicas (soma, subtração, multiplicação e divisão). O objetivo é praticar conceitos de programação, controle de versão com Git, e organização de projetos de software.

//FUNCIONALIDADES: A calculadora terá as seguintes funcionalidades:

Soma: Permitir ao usuário somar dois ou mais números.
Subtração: Permitir ao usuário subtrair um número de outro.
Multiplicação: Calcular o produto entre dois ou mais números.
Divisão: Dividir um número por outro, com tratamento de erro para divisão por zero.
Interface simples no terminal: O usuário poderá selecionar a operação desejada por meio de um menu.
Validação de entrada: Garantir que o usuário insira apenas números válidos.

//CRONOGRAMA: 
Etapa/    Descrição.    Prazo Estimado
Configuração Inicial/    Criar o repositório no GitHub e configurar o projeto.    1 dia
Estrutura Base/    Criar o arquivo principal calculadora.py.    1 dia
Implementar/ Funções    Desenvolver funções para soma, subtração, multiplicação e divisão.    2 dias
Menu Interativo/    Criar o menu para que o usuário selecione operações.    1 dia
Validação de Dados/    Implementar verificações para entrada e divisão por zero.    1 dia
Testes/    Testar todas as operações e corrigir possíveis erros.    1 dia
Documentação/    Adicionar documentação ao código e ao repositório.    1 dia
Finalização/    Realizar o commit final e enviar os arquivos para o GitHub.    1 dia

# **Documentação do Projeto - Calculadora de Operações Básicas**

## **Desafios Enfrentados**
1. **Conflitos de Merge**:
   - Durante o desenvolvimento, ocorreram conflitos ao tentar fazer o merge das branches `menu-interativo` e `validacao-dados` na branch principal (`main`). 
   - **Como resolvemos:** Analisamos manualmente os trechos conflitantes no código e ajustamos as alterações para manter a consistência.

2. **Tratamento de Erros na Divisão**:
   - Houve dificuldade inicial em implementar uma validação para evitar a divisão por zero.
   - **Solução:** Implementamos uma mensagem de erro clara e retornamos ao menu principal caso o usuário tentasse dividir por zero.

3. **Organização de Funcionalidades**:
   - Ao adicionar novas funcionalidades (ex.: validação de dados), o código começou a ficar menos organizado.
   - **Solução:** Refatoramos o código, separando funções em blocos lógicos.

---

## **Como o Git Ajudou no Gerenciamento**
1. **Controle de Alterações**:
   - Usamos commits frequentes com mensagens descritivas, permitindo rastrear facilmente quais mudanças foram feitas e quando.
   - Exemplo de mensagem: `"Implementa validação para divisão por zero"`.

2. **Trabalho em Branches**:
   - Cada funcionalidade foi desenvolvida em uma branch separada (ex.: `soma`, `menu-interativo`), permitindo trabalhar em paralelo sem afetar a branch principal (`main`).
   - Isso foi essencial para evitar bugs em funcionalidades já concluídas.

3. **Histórico de Desenvolvimento**:
   - O histórico do Git serviu como uma documentação automática do projeto, permitindo revisar decisões anteriores e corrigir erros.

4. **Facilidade no Colaborativo**:
   - Mesmo sendo um projeto individual, o uso do Git simulou um fluxo de trabalho colaborativo, com merge de branches e resolução de conflitos.

---

### **Conclusão**
O uso do Git proporcionou uma organização melhor no desenvolvimento, minimizou erros e permitiu uma abordagem estruturada para implementar funcionalidades. Esse fluxo será útil em projetos futuros, especialmente ao trabalhar em equipe.

