O que são Registros de Decisão de Arquitetura ADRs?


ADRs (Architecture Decision Records) são documentos concisos que servem como um diário das escolhas estruturais mais importantes feitas no projeto de software. Cada registro captura o contexto que levou à decisão, a própria decisão tomada, e as consequências esperadas (tanto positivas quanto negativas). O principal objetivo é estabelecer uma memória institucional, permitindo que a equipe e futuros colaboradores entendam a trajetória e os motivos por trás da arquitetura atual.

Metodologia de Registro das Decisões:
Para gerenciar e padronizar esses documentos, utilizamos a ferramenta adr-tools. Essa abordagem agiliza o processo de documentação. Todos os ADRs criados estão localizados no diretório doc/adr e são rastreados pelo Git, garantindo que o histórico de decisões esteja sempre versionado e alinhado com o código-fonte do projeto.

A criação de um novo registro é feita de forma simples, utilizando o comando adr new, que gera automaticamente um arquivo Markdown já formatado.

A Importância das Decisões Fundamentais:
As escolhas de arquitetura registradas neste repositório são pilares para a robustez e a evolução do projeto:

Arquitetura em Camadas (0002-escolha-de-arquitetura-em-camadas.md): Esta decisão estabelece uma fronteira clara entre a apresentação, o processamento da lógica de negócio e a persistência de dados. Isso resulta em um sistema mais modular, fácil de testar e simples de manter.

Banco de Dados PostgreSQL (0003-escolha-de-banco-de-dados-postgresql.md): Optamos pelo PostgreSQL, um sistema relacional, devido à necessidade de armazenar dados de forma estruturada. Além disso, o conhecimento prévio da equipe em SQL e os recursos avançados deste banco facilitam tanto o desenvolvimento quanto a administração dos dados.

Integração Contínua com GitHub Actions (0004-integracao-continua-com-github-actions.md): A implementação do GitHub Actions é essencial para automatizar nosso fluxo de trabalho. Essa automação permite que testes sejam executados e o código seja preparado para implantação (deploy) automaticamente a cada commit, assegurando a qualidade e a rapidez na entrega contínua do software.