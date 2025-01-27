# Previsão de Rendimento de Colheita e Otimização da Irrigação

## Descrição do Projeto

Este projeto utiliza técnicas de **Deep Learning** para prever o rendimento das colheitas e otimizar a irrigação, com base em variáveis ambientais e dados históricos. A abordagem visa fornecer insights precisos para auxiliar na tomada de decisões no agronegócio, promovendo práticas agrícolas mais eficientes e sustentáveis.

## Objetivos

- **Previsão de Rendimento de Colheita:** Antecipar a produtividade agrícola com base em fatores ambientais e históricos.
- **Otimização da Irrigação:** Fornecer recomendações para uso eficiente da água, garantindo o crescimento ideal das culturas e conservação dos recursos hídricos.

## Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Bibliotecas:** TensorFlow, Keras, Pandas, NumPy, Scikit-learn
- **Desenvolvimento Web:** Flask para a criação de APIs RESTful
- **Ferramentas de Serialização:** Joblib para serialização de modelos e escaladores

## Estrutura do Repositório

- `app.py`: Script principal que implementa a API Flask para servir o modelo de previsão.
- `cliente.py`: Script de exemplo para consumir a API e obter previsões.
- `dataset.csv`: Conjunto de dados utilizado para treinar o modelo.
- `dicionario_dados.xlsx`: Dicionário detalhado das variáveis presentes no dataset.
- `modelo.ipynb`: Notebook Jupyter contendo o processo de desenvolvimento e treinamento do modelo de Deep Learning.
- `modelo_dsa.keras`: Arquivo serializado do modelo treinado.
- `scaler.joblib`: Objeto de escalonamento dos dados para garantir consistência nas previsões.

## Como Utilizar

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/LucasBoden-da/Agronegocio.git
   cd Agronegocio
   ```

2. **Instalar as Dependências:**

   Certifique-se de ter o Python instalado. Em seguida, instale as bibliotecas necessárias:

   ```bash
   pip install -r requirements.txt
   ```

3. **Executar a API:**

   Inicie o servidor Flask para disponibilizar a API de previsão:

   ```bash
   python app.py
   ```

   A API estará disponível em `http://127.0.0.1:5000/`.

4. **Obter Previsões:**

   Utilize o script `cliente.py` ou ferramentas como o Postman para enviar requisições à API e obter as previsões de rendimento de colheita e recomendações de irrigação.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contato

Para mais informações ou interesse em colaborações:

- **Autor:** Lucas Boden
- **Email:** lucas.boden@example.com
- **LinkedIn:** [https://www.linkedin.com/in/lucas-stuart/](https://www.linkedin.com/in/lucas-stuart/)
