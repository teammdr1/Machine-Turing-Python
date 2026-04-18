# Machine de Turing — Exemple d'exécution

Ce programme simule une machine de Turing basée sur un ensemble de règles définies dans un dictionnaire.

## Structure du ruban

```python
tape = list("!!!X_______")  # exemple de départ
head = 0                     # position de la tête
state = "A"                 # état initial
````

* `tape` : bande de travail (liste de символes)
* `head` : position de lecture/écriture
* `state` : état actuel de la machine

## Format des règles

```python
(état, symbole_lu): (symbole_écrit, direction, nouvel_état)
```

* `>` : déplacement vers la droite
* `<` : déplacement vers la gauche
* `"HALT"` : arrêt de la machine

## Règles de transition

```python
rules = {
    # à compléter
}
```

## Fonctionnement

À chaque étape :

1. Lecture du symbole sous la tête
2. Recherche de la règle correspondante
3. Écriture du nouveau symbole
4. Déplacement de la tête
5. Changement d’état
6. Affichage de l’état du ruban

## Boucle principale

```python
while state != "HALT":
    if head >= len(tape):
        tape.append("_")

    symbol = tape[head]
    key = (state, symbol)

    if key not in rules:
        print("Erreur:", state, symbol)
        break

    write, move, new_state = rules[key]
    tape[head] = write

    head += 1 if move == ">" else -1

    if head < 0:
        tape.insert(0, "_")
        head = 0

    state = new_state

    print("Ruban:", "".join(tape), "Tête:", head, "Etat:", state)
```

## Résultat final

```python
print("Ruban final :", "".join(tape))
```

## Objectif

Ce script sert de base pour expérimenter des machines de Turing simples en modifiant uniquement le dictionnaire `rules`.
