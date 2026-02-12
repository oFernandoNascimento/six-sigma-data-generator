# 🏭 Gerador de Dados de Qualidade Industrial (Lean Six Sigma)

Este script Python simula um ambiente fabril real para gerar datasets destinados a análises de Controle de Qualidade e OEE em Power BI.

## 🎯 Objetivo
Gerar dados realistas com variabilidade diária (ruído estatístico) para evitar médias estáticas e permitir análises de tendências, cálculo de Nível Sigma e KPIs de manufatura.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12+**
* **Pandas:** Para estruturação e exportação do DataFrame.
* **Random:** Para simulação estocástica de defeitos e paradas.

## 📊 O que o script simula?
1.  **Variabilidade de Processo:** Diferentes taxas de defeito baseadas na máquina (ex: Solda é mais estável que Pintura).
2.  **OEE (Overall Equipment Effectiveness):** Gera tempos de operação, paradas não planejadas e total produzido.
3.  **Cronologia:** Cria uma série temporal contínua para análise de tendências no Power BI.

## 🚀 Como usar
1. Instale as dependências:
   ```bash
   pip install pandas openpyxl
