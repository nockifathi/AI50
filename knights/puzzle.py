from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # If and only if A is knight, then A must not be knave
    Biconditional(AKnight, Not(AKnave)),
    # If and only if A is knight, then "I am both a knight and a knave." is true.
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # If and only if A is knight, then A must not be knave
    Biconditional(AKnight, Not(AKnave)),
    # If and only if B is knight, then B must not be knave
    Biconditional(BKnight, Not(BKnave)),
    # If and only if A is knight, then "A and B is knight" is true
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # If and only if A is knight, then A must not be knave
    Biconditional(AKnight, Not(AKnave)),
    # If and only if B is knight, then B must not be knave
    Biconditional(BKnight, Not(BKnave)),
    # If and only if A is knight, then (A and B is knight or A and B is knave)
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If and only if B is knight, then (A is knight and B is knave, or A is knave and B is knight)
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # If and only if A is knight, then A must not be knave
    Biconditional(AKnight, Not(AKnave)),
    # If and only if B is knight, then B must not be knave
    Biconditional(BKnight, Not(BKnave)),
    # If and only if C is knight, then C must not be knave
    Biconditional(CKnight, Not(CKnave)),
    # If and only if A is knight, then A is either knight or knave
    Biconditional(AKnight, Or(AKnight, AKnave)),
    # If and only if B is knight, then "A said 'I am a knave'." is true
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    # If and only if B is knight, then "C is a knave" is true
    Biconditional(BKnight, CKnave),
    # If and only if C is knight, then A is a knight
    Biconditional(CKnight, AKnight)

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
