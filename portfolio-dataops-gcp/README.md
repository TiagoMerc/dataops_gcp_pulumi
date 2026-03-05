# Modelo de Bucket de Armazenamento do Google Cloud Storage com Pulumi para GCP em Python

Um modelo Pulumi minimalista para provisionar um bucket do Google Cloud Storage usando Python.

Este modelo ajuda você a começar a usar o Pulumi e o provedor `pulumi-gcp` para criar um bucket de armazenamento simples e exportar sua URL.

## Quando usar

- Você precisa de um exemplo rápido de como usar o Pulumi com o Google Cloud em Python.

- Você quer gerenciar um bucket do Google Cloud Storage como código.

- Você está procurando uma estrutura mínima para construir uma infraestrutura do GCP mais complexa.

## Pré-requisitos

- Uma conta do Google Cloud e um projeto GCP de destino.

- Autenticação configurada via `gcloud auth login` ou a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS`.

- Python 3.7 ou posterior instalado em sua máquina.

- Pulumi CLI instalado e com login feito em sua conta Pulumi.

## Uso

Execute o seguinte comando para criar um novo projeto a partir deste modelo:

 ```bash
 pulumi new gcp-python
 ```

Siga as instruções interativas:

- **Nome do Projeto**: O nome do seu projeto.
- **Descrição do Projeto**: Uma breve descrição do seu projeto.
- **gcp:project**: O ID do projeto do Google Cloud onde os recursos serão criados.

Após a geração do projeto, acesse o diretório do projeto e faça a implantação:

 ```bash
 cd <project-name>
 pulumi up
 ```

 Confirme as alterações para provisionar seu bucket de armazenamento.

 ## Project Layout

 ```
 .
 ├── __main__.py        # Recursos de definição do programa Pulumi
 ├── Pulumi.yaml        # Configuração do projeto e metadados do modelo
 └── requirements.txt   # Dependências do Python para Pulumi e GCP
 ```

 ## Configuration

 - **gcp:project**: (Obrigatório) O ID do projeto do Google Cloud onde os recursos serão criados.

 ## Resources Created

 - **Storage Bucket** (`pulumi_gcp.storage.Bucket`):Um bucket de localização.

 ## Outputs

 - **bucket_name**: A URL do bucket de armazenamento criado.

 ## Next Steps

 -Modifique o arquivo `__main__.py` para personalizar o bucket:
- Altere o nome do bucket.
- Ajuste o `location` ou adicione rótulos e políticas do IAM ao bucket.
- Adicione mais recursos do GCP, como tópicos do Pub/Sub, instâncias do Compute Engine ou conjuntos de dados do BigQuery.
- Integre com pipelines de CI/CD usando `pulumi preview` e `pulumi up --yes`.
- Consulte a [Documentação do Provedor GCP do Pulumi](https://www.pulumi.com/registry/packages/gcp/) para obter mais exemplos.

 ## Need Help?

 - Pulumi Docs: https://www.pulumi.com/docs/
 - GCP Provider Docs: https://www.pulumi.com/registry/packages/gcp/
 - Community Slack: https://slack.pulumi.com/
 - GitHub Issues: https://github.com/pulumi/pulumi/issues