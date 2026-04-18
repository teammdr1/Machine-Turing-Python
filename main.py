tape = list("!!!X_______") # Exemple
head = 0
state = "A"

rules = {
    # (état, symbole lu): (symbole écrit, direction, nouvel état)
}

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

print("Ruban final :", "".join(tape))
