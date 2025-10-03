import pytest


@pytest.mark.parametrize('numbers', [1, 2, -1])
def test_numbers(numbers: int):
    assert numbers > 0


@pytest.mark.parametrize(
    "phone_number",
    ["+70000000011", "+70000000022", "+70000000033"],
    ids=[
        "User with money on bank account",
        "User without money on bank account",
        "User with operations on bank account"
    ]
)
def test_identifiers(phone_number: str):
    pass


users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    pass
