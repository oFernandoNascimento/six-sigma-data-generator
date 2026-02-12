import pandas as pd
import random

# Configuração
dates = pd.date_range(start='2024-01-01', end='2024-02-29', freq='D')
machines = ['Máquina A (Estamparia)', 'Máquina B (Solda)', 'Máquina C (Pintura)']
shifts = ['Manhã', 'Tarde', 'Noite']

data_list = []

# Geração dos Dados
for date in dates:
    for machine in machines:
        for shift in shifts:
            total_produced = random.randint(800, 1200)

            # Lógica de Defeitos por Máquina
            if machine == 'Máquina B (Solda)':
                defect_rate = random.uniform(0.005, 0.015)
            elif machine == 'Máquina C (Pintura)':
                defect_rate = random.uniform(0.02, 0.05)
            else:
                defect_rate = random.uniform(0.01, 0.03)

            # Introdução de variabilidade (ruído)
            if random.random() > 0.95:
                defect_rate *= 2

            defects = int(total_produced * defect_rate)
            good_parts = total_produced - defects
            
            planned_time = 480
            downtime = random.randint(0, 45)
            operating_time = planned_time - downtime

            data_list.append({
                'Data': date,
                'Máquina': machine,
                'Turno': shift,
                'Total Produzido': total_produced,
                'Peças Defeituosas': defects,
                'Peças Boas': good_parts,
                'Tempo Planejado (min)': planned_time,
                'Tempo Parada (min)': downtime,
                'Tempo Operando (min)': operating_time
            })

df = pd.DataFrame(data_list)
df.to_excel('oee_six_sigma.xlsx', index=False)

print("Arquivo 'oee_six_sigma.xlsx' gerado com sucesso.")
