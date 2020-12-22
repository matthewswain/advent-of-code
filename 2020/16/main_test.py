from main import Rule, Ticket, get_field_lookup


def test_rule():
    rule = Rule("departure location: 26-724 or 743-964")
    assert rule.validate(28)
    assert not rule.validate(725)


def test_get_field_lookup():
    rules = [
        Rule("class: 0 - 1 or 4 - 19"),
        Rule("row: 0 - 5 or 8 - 19"),
        Rule("seat: 0 - 13 or 16 - 19"),
    ]

    tickets = [
        Ticket("3,9,18"),
        Ticket("15,1,5"),
        Ticket("5,14,9"),
    ]

    lookup = get_field_lookup(rules, tickets)
    assert lookup == {0: "row", 1: "class", 2: "seat"}


def test_decode():
    ticket = Ticket("11,12,13")
    lookup = {0: "row", 1: "class", 2: "seat"}
    assert ticket.decode(lookup) == {"class": 12, "row": 11, "seat": 13}
