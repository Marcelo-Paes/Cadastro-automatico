# Cadastro-automatico
Este aplicativo automatiza o processo de cadastro de empresas em um site de contabilidade. Aqui está o que cada parte do código faz:

1. **Navegação até o Site**: Utiliza o Selenium para abrir o navegador Google Chrome e navegar até o site "https://contabilidade-devaprender.netlify.app/".

2. **Login**: Preenche o formulário de login com um e-mail e senha pré-definidos.

3. **Preenchimento de Dados**: Utiliza os dados de uma planilha Excel chamada "empresas.xlsx" para preencher os campos de cadastro de empresas no site. Os dados são extraídos da planilha e inseridos nos campos correspondentes no formulário da página web.

4. **Clicar em Cadastrar**: Após preencher os campos com os dados de uma empresa, o código clica no botão "Cadastrar" para enviar o formulário e cadastrar a empresa no sistema.

5. **Repetição para Cada Empresa**: Todo esse processo é repetido para cada linha de dados na planilha, até que todas as empresas tenham sido cadastradas.

Este aplicativo é útil para automatizar tarefas repetitivas de inserção de dados em formulários web, economizando tempo e esforço ao realizar múltiplos cadastros de empresas de uma só vez. O Selenium é uma ferramenta poderosa para automatizar interações com páginas da web, permitindo que o desenvolvedor simule ações humanas em navegadores web.
