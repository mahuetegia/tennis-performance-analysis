# Peso que tiene partidos anteriores en estado de forma
def peso_recencia(n):
    return (0.836**n)

def peso_rival_ganar(ranking):
    if ranking <= 10:
        return 1.0
    elif ranking <= 20:
        return 0.9
    elif ranking <= 30:
        return 0.8
    elif ranking <= 40:
        return 0.7
    elif ranking <= 50:
        return 0.6
    else:
        return 0.5

def peso_rival_perder(ranking):
    if ranking <= 10:
        return 0.5
    elif ranking <= 20:
        return 0.6
    elif ranking <= 30:
        return 0.7
    elif ranking <= 40:
        return 0.8
    elif ranking <= 50:
        return 0.9
    else:
        return 1.0

def peso_torneo(torneo):
    switcher = {
        "G": 1.5,
        "M": 1.1,
        "A": 0.8,
        "D": 1.0,
        "O": 0.5,
        "F": 1.4
    }
    return switcher.get(torneo, 0)

def peso_ronda_ganar(ronda):
    switcher = {
        "F": 1.5,
        "SF": 1.3,
        "QF": 1.1,
        "R16": 0.9,
        "R32": 0.7,
        "R64": 0.5,
        "R128": 0.3,
        "RR": 0.6
    }
    return switcher.get(ronda, 0)

def peso_ronda_perder(ronda):
    switcher = {
        "F": 0.3,
        "SF": 0.5,
        "QF": 0.7,
        "R16": 0.9,
        "R32": 1.1,
        "R64": 1.3,
        "R128": 1.5,
        "RR": 0.6
    }
    return switcher.get(ronda, 0)

def diez_ultimos_partidos(df,jugador,fecha,valor_ronda):
    df_jugador=df[
        ((df["winner_name"]==jugador) | (df["loser_name"]==jugador))
            &
        ((df["tourney_date"]<fecha) | ((df["tourney_date"]==fecha) & (df["valor_ronda"]<valor_ronda)))
    ].sort_values(by=["tourney_date", "valor_ronda"], ascending=[False,False]).head(10)
    return df_jugador

