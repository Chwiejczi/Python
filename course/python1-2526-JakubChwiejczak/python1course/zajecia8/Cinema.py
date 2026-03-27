import logging


class CinemaErr(Exception):
    pass


class NoFreeSeatsError(CinemaErr):
    pass


class SeatOccupied(CinemaErr):
    pass


class UserAlreadyHasReservation(CinemaErr):
    pass


class WrongUser(CinemaErr):
    pass


class WrongSeat(CinemaErr):
    pass


logger = logging.getLogger(__name__)


class CinemaHall:
    def __init__(self, seats):
        self.seats = seats
        self.FreeSeatsNo = len(seats.keys())
        logger.debug("stworzono salę")

    def reserve(self, seatU, user):  # seatU - miejsce ktore chce zarezerwowac user
        if user in self.seats.values():
            logger.warning("user ma rezerwacje")
            raise UserAlreadyHasReservation("User Already have reservation")
        elif self.FreeSeatsNo == 0:
            logger.warning("nie ma wolnych miejsc")
            raise NoFreeSeatsError("All seats are occupied")
        elif self.seats[seatU] == None:
            self.seats[seatU] = user
            self.FreeSeatsNo = self.FreeSeatsNo - 1
        else:
            logger.warning("wszystko zajete")
            raise SeatOccupied("Seat already occupied")
        logger.info("wszystko przebieglo poprawnie")
        return "Seat has been booked correctly"

    def cancel(self, seatU, user):
        if self.seats[seatU] == None:
            logger.error("miejsce jest wolne")
            raise WrongSeat("Seat is free")
        if self.seats[seatU] != user:
            logger.exception("miejsce nie jest twoje")
            raise WrongUser("You're not the seat's owner")
        else:
            self.seats[seatU] = None
            logger.info("miejsce odwolane")
        return "Seat has been canceled correctly"


dict = {"A1": None, "A2": None, "A3": None}

Cinema = CinemaHall(dict)
try:
    print(Cinema.reserve("A1", "Jan"))
except CinemaErr as e:
    print(f"{e} ")


try:
    print(Cinema.reserve("A1", "Jan"))
except CinemaErr as e:
    print(f"{e} ")


try:
    print(Cinema.cancel("A1", "Jan"))
except CinemaErr as e:
    print(f"{e} ")
