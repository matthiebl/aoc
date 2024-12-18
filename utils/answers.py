answers = {
    2024: {
        1:  {"p1": 3246517, "p2": 29379307},
        2:  {"p1": 383, "p2": 436},
        3:  {"p1": 166905464, "p2": 72948684},
        4:  {"p1": 2530, "p2": 1921},
        5:  {"p1": 5732, "p2": 4716},
        6:  {"p1": 5318, "p2": 1831},
        7:  {"p1": 66343330034722, "p2": 637696070419031},
        8:  {"p1": 426, "p2": 1359},
        9:  {"p1": 6288707484810, "p2": 6311837662089},
        10: {"p1": 552, "p2": 1225},
        11: {"p1": 229043, "p2": 272673043446478},
        12: {"p1": 1421958, "p2": 885394},
        13: {"p1": 25751, "p2": 108528956728655},
        14: {"p1": 222208000, "p2": 7623},
        15: {"p1": 1527563, "p2": 1521635},
        16: {"p1": 66404, "p2": 433},
        17: {"p1": "3,7,1,7,2,1,0,6,3", "p2": 37221334433268},
        18: {"p1": 314, "p2": "15,20"},
    },
}


def get_answers(year: str, day: str):
    return answers.get(int(year), {}).get(int(day), None)


def answer_tester(year: str, day: str):
    """Gets the answers from the answers"""
    answers = get_answers(year, day)

    def inner(p1, p2):
        if answers is None:
            print(f"No stored answers for {year} day {day}")
            return False
        assert p1 == answers["p1"], f"Part 1: {p1} is not expected {answers["p1"]}"
        assert p2 == answers["p2"], f"Part 2: {p2} is not expected {answers["p2"]}"
        return True
    return inner
