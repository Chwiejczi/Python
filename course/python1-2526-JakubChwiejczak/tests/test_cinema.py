import pytest
from zajecia8.Cinema import (
    CinemaHall,
    SeatOccupied,
    UserAlreadyHasReservation,
    WrongUser,
)


def test_reserve_seat():
    dict = {"A1": None, "A2": None, "A3": None}
    hall = CinemaHall(dict)
    user = "Jan Kowalski"
    seat = "A1"

    # spr czy będzie ok komunikat
    assert hall.reserve(seat, user) == "Seat has been booked correctly"

    # spr czy dobrze przypisalismy mijsce
    assert hall.seats[seat] == user


def test_reserve_occupied_seat():
    dict = {"A1": None, "A2": None, "A3": None}
    hall = CinemaHall(dict)
    user = "Jan Kowalski"
    seat = "A1"

    hall.reserve(seat, user)

    # spr czy będzie ok komunikat
    with pytest.raises(SeatOccupied) as exc_info:
        hall.reserve(seat, "uzytkownik")
    assert "Seat already occupied" in str(exc_info.value)


def test_reserve_2seats_by_user():
    dict = {"A1": None, "A2": None, "A3": None}
    hall = CinemaHall(dict)
    user = "Jan Kowalski"
    seat = "A1"

    hall.reserve(seat, user)

    with pytest.raises(UserAlreadyHasReservation) as exc_info:
        hall.reserve("A2", user)
    assert "User Already have reservation" in str(exc_info.value)


def test_cancel():
    dict = {"A1": None, "A2": None, "A3": None}
    hall = CinemaHall(dict)
    user = "Jan Kowalski"
    seat = "A1"

    hall.reserve(seat, user)

    # spr komunikatu

    assert hall.cancel(seat, user) == "Seat has been canceled correctly"

    # spr czy sie zwolnilo
    assert hall.seats[seat] == None


def test_cancel_by_wrong_user():
    dict = {"A1": None, "A2": None, "A3": None}
    hall = CinemaHall(dict)
    user = "Jan Kowalski"
    seat = "A1"

    hall.reserve(seat, user)

    with pytest.raises(WrongUser) as exc_info:
        hall.cancel(seat, "Lech W")
    assert "You're not the seat's owner" in str(exc_info.value)


# ==================2 & 3===================


@pytest.fixture
def hall_res():
    dict = {"A1": None, "A2": None, "A3": None}
    hall = CinemaHall(dict)
    hall.reserve("A3", "abc")
    hall.reserve("A2", "Skidibi")
    return hall


@pytest.mark.parametrize(
    "seatU, user,should_raise",
    [
        ("A1", "Jan Kowalski", False),
        ("A1", "Andrzej Lepper", False),
        ("A3", "Jan Kowalski", True),
        ("A1", "Skidibi", True),
    ],
    ids=["correct", "correct", "wrong", "wrong"],
)
def test_reservation(seatU, user, should_raise, hall_res):
    hall = hall_res
    # dict={'A1': None, 'A2':None,'A3':None}
    # hall=CinemaHall(dict)
    # hall.reserve("A3","abc")
    # hall.reserve("A2","Skidibi")
    if should_raise:
        with pytest.raises((UserAlreadyHasReservation, SeatOccupied)):
            hall.reserve(seatU, user)
    else:
        hall.reserve(seatU, user)
        assert hall.seats[seatU] == user


# =================4====================


def test_full_reservation():
    dict = {"A1": None, "A2": None, "A3": None}
    hall = CinemaHall(dict)
    hall.reserve("A1", "Kowalski")

    with pytest.raises(SeatOccupied):
        hall.reserve("A1", "Nowak")
    hall.cancel("A1", "Kowalski")
    hall.reserve("A1", "Nowak")

    assert hall.seats["A1"] == "Nowak"
