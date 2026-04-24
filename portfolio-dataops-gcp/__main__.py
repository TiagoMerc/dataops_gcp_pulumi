"""A Google Cloud Python Pulumi program"""

#import pulumi
#from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
#bucket = storage.Bucket('my-bucket', location="US")

# Export the DNS name of the bucket
# pulumi.export('bucket_name', bucket.url)

import pulumi
from pulumi_gcp import storage, bigquery

# 1. O Pulumi vai criar o nosso Data Lake (Bucket exclusivo para o projeto) para os arquivos CSVs brutos, 
# que serão usados para análises futuras. 

data_lake_bucket = storage.Bucket(
    "ecommerce-data-lake-portfolio",
    location="US",
    force_destroy=True,
    uniform_bucket_level_access=True,
)

# 2. Estamos criando o Dataset Raw no BigQuery (para os dados brutos)
raw_dataset = bigquery.Dataset(
    "ecommerce_raw",
    dataset_id="ecommerce_raw",
    location="US",
)

# 3. Estamos criando o Dataset Analytics no BigQuery (para os dados transformados pelo dbt)
analytics_dataset = bigquery.Dataset(
    "ecommerce_analytics",
    dataset_id="ecommerce_analytics",
    location="US",
)

# 4. Faz o upload do arquivo CSV local para dentro do Bucket
# Arquivo de vendas, que inseri como primeiro teste, mas depois adicionei o online_retail.csv para ter mais dados para análise mais concretas!
arquivo_vendas = storage.BucketObject(
"vendas-csv-upload",
bucket=data_lake_bucket.name,
source=pulumi.FileAsset("vendas.csv"),  # Lê o arquivo da nossa pasta
name="vendas.csv" # Nome que o arquivo terá na nuvem
)

# 5. Cria a Tabela Externa no BigQuery
# Detalhe de Portfólio: Tabelas externas não armazenam dados, apenas "leem" o Storage. Economiza custos!
tabela_externa_vendas = bigquery.Table(
"tabela_raw_vendas",
dataset_id=raw_dataset.dataset_id,
table_id="vendas_externa",
external_data_configuration=bigquery.TableExternalDataConfigurationArgs(
source_uris=[pulumi.Output.concat("gs://", data_lake_bucket.name, "/", arquivo_vendas.name)],
source_format="CSV",
autodetect=True, # O BigQuery descobre sozinho o que é número, texto ou data!
)
)

# Adicionando o arquivo online_retail.csv ao Bucket
arquivo_online_retail = storage.BucketObject(
    "online-retail-csv-upload",
    bucket=data_lake_bucket.name,
    source=pulumi.FileAsset("online_retail.csv"),
    name="online_retail.csv"
)

# Criando uma tabela externa para o arquivo online_retail.csv
tabela_externa_online_retail = bigquery.Table(
    "tabela_raw_online_retail",
    dataset_id=raw_dataset.dataset_id,
    table_id="online_retail_ecommerce",
    external_data_configuration=bigquery.TableExternalDataConfigurationArgs(
        source_uris=[pulumi.Output.concat("gs://", data_lake_bucket.name, "/", arquivo_online_retail.name)],
        source_format="CSV",
        autodetect=True,
    )
)

# 6. Exportando os nomes reais que foram gerados na nuvem para o terminal
pulumi.export("nome_do_bucket", data_lake_bucket.name)
pulumi.export("dataset_raw", raw_dataset.dataset_id)
pulumi.export("dataset_analytics", analytics_dataset.dataset_id)