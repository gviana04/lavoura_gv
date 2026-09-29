Projeto de Geolocalização de Lavouras — AP1 (Projeto Cloud)
Link da API Publicada na AWS Elastic Beanstalk: Lavouragv-env.eba-wgk8qfna.us-east-2.elasticbeanstalk.com

📌 Sobre o Projeto
Este projeto consiste em uma API Rest desenvolvida em Django Rest Framework para gerenciamento e geolocalização de áreas agrícolas e lavouras. A solução foi projetada como parte da avaliação AP1 da disciplina de Projeto de Cloud / Banco de Dados e Cloud Computing.

O sistema permite o cadastro, consulta e controle espacial de lavouras ligadas a propriedades rurais, armazenando dados como tipo de cultura, área cultivada e coordenadas geográficas (latitude e longitude).

🛠️ Arquitetura e Modelagem dos Dados
A API é estruturada em torno de duas entidades principais com relacionamento (
1
:
N
):

Fazenda (Fazenda)

nome: Nome da propriedade/fazenda.
produtor: Nome do responsável/produtor rural.
cidade: Município de localização.
uf: Estado (sigla).
Lavoura (Lavoura)

fazenda: Chave estrangeira relacionando a lavoura à respectiva Fazenda.
tipo_cultura: Opções de culturas agrícolas (Soja, Milho, Algodão, Café, etc.).
area_em_hectares: Dimensão do talhão/área de plantio.
latitude / longitude: Coordenadas de geolocalização do ponto de referência da lavoura.
data_registro: Data/hora de cadastro do registro.
