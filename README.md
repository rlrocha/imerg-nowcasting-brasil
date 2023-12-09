# Nowcasting com dados IMERG da região sul do Brasil

Repositório com instruções e códigos para criação de uma base de dados IMERG para nowcasting da região sul do Brasil.

## INMET

Os dias com maior intensidade precipitação (mm/dia) podem ser extraídos como mostra o notebook [rainy-days](notebooks/rainy-days.ipynb). Os dados são obtidos na [Base de Dados Meteorológicos](https://bdmep.inmet.gov.br/) do INMET.

## IMERG

Inicialmente é necessário realizar o cadastro na [EARTHDATA](https://urs.earthdata.nasa.gov/) para obter os links dos arquivos e, posteriormente, fazer o download dos dados. Além disso, é necessário gerar os arquivos de [pré-requisito](https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Generate%20Earthdata%20Prerequisite%20Files).

O recorte utilizado para extrair imagens da região sul do Brasil dos dados [IMERG](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHE_06/summary) tem como base o retângulo formado pelas seguintes coordenadas:

```
-62.45,-34.35,-43.35,-21.65
```

Onde os valores são, respectivamente: longitude miníma, latitude mínima, longitude máxima e latitude máxima.

O download dos dados IMERG, através da lista de arquivos, é mostrado no notebook [download-imerg](notebooks/download-imerg.ipynb).

## Modelo

O download do modelo para o nowcasting da região sul do Brasil é realizado pela execução do script [download_model](download_model.py), como mostra o exemplo abaixo:

```shell
python download_model.py
```

## Metadados e resultados

A análise dos metadados pode ser feita e visualizada através do notebook [metadata-analysis](notebooks/metadata-analysis.ipynb).

Os resultados obtidos pelo modelo U-Net podem ser obtidos pelo notebook [unet-results](notebooks/unet-results.ipynb). Para obter uma melhor visualização dos resultados, através de GIFs, é aconselhável utilizar o [nbviewer](https://nbviewer.org/github/rlrocha/imerg-nowcasting-brasil/blob/main/notebooks/unet-results.ipynb).

---
Links úteis:
- Instituto Nacional de Meteorologia (INMET): [portal](https://portal.inmet.gov.br/).
- Jupyter Notebook Viewer: [nbviewer](https://nbviewer.org/).
- Download do modelo: [dropbox](https://www.dropbox.com/scl/fi/ngwvakmytc0rzy6k43taz/model.h5?rlkey=q4hg17kj90q57xm1uixwav45c&dl=0).