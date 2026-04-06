def calculate_score(round):
    round_score = []
    for participant in round["scores"]:
        round_score.append((participant, sum(round["scores"][participant].values())))
    return sorted(round_score, key=lambda x: x[1], reverse=True)

def update_participants(round_scores, participants):
    for i, (name, score) in enumerate(round_scores):
        if i == 0:
            participants[name]["wins"] += 1
        participants[name]["points"] += score
        if participants[name]["best"] < score:
            participants[name]["best"] = score
    return 

def show_round(round_scores, round_number, round_name):
    print(f"Ronda {round_number}  - {round_name} ")
    for i, (name, score) in enumerate(round_scores, start=1):
        if i == 1:
            print(f"Ganador {name} ({score} pts)")
        else:
            print(f" {i}° {name} ({score} pts)")
    return

def process_round(round, round_number, participants):
    round_scores = calculate_score(round)
    update_participants(round_scores, participants)
    show_round(round_scores, round_number, round["theme"])
    return

def show_table(participants, total_rounds):
    orderede_participants = sorted(participants.items(), key=lambda x: x[1]["points"], reverse=True)
    print("Tabla de posiciones final:")
    for participant in orderede_participants:
        print("-" * 25)
        print(f"Nombre: {participant[0]}")
        print(f"Puntos totales: {participant[1]["points"]}")
        print(f"Rondas ganadas: {participant[1]["wins"]}")
        print(f"Mejor ronda: {participant[1]["best"]}")
        print(f"Promedio: {participant[1]["points"] / total_rounds:.2f}")
    return

def main():
    rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
            'Santiago': {'judge_1': 6, 'judge_2': 7,
'judge_3': 6},
            'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
            'Mateo': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
            'Camila': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
            'Lucía': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
            'Mateo': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
            'Camila': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
            'Santiago': {'judge_1': 7, 'judge_2': 7,
'judge_3': 6},
            'Lucía': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9,
'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
            'Santiago': {'judge_1': 8, 'judge_2': 9,
'judge_3': 7},
            'Lucía': {'judge_1': 7, 'judge_2': 7,
'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8,
'judge_3': 9},
            'Mateo': {'judge_1': 8, 'judge_2': 9,
'judge_3': 8},
            'Camila': {'judge_1': 7, 'judge_2': 7,
'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
            'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 7},
        }
    }
]
    participants = {
        name: {"points": 0, "wins": 0, "best": 0}
        for name in rounds[0]["scores"]
        }
    for i, round in enumerate(rounds, start=1):
        process_round(round, i, participants)
    show_table(participants, len(rounds))