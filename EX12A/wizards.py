"""Help wizards to get into school."""


class Wand:
    """Represent a wand."""

    def __init__(self, wood_type, core):
        """
        Take in two parameters.

        :param wood_type:
        :param core:
        """
        self.wood_type = wood_type
        self.core = core

    def set_wood_type(self, wood_type):
        """
        Give self a new variable.

        :param wood_type:
        :return:
        """
        self.wood_type = wood_type

    def set_core(self, core):
        """
        Give self a new variable.

        :param core:
        :return:
        """
        self.core = core

    @staticmethod
    def check_wand(wand):
        """
        Static method, check whether the wand is correct.

        :param wand:
        :return:
        """
        if isinstance(wand, Wand) and wand.core is not None and wand.wood_type is not None:
            pass
        else:
            raise MismatchError("The wand like that does not exist!")

    def __str__(self):
        """
        Return string.

        "{wood_type}, {core}"
        :return:
        """
        return "{}, {}".format(self.wood_type, self.core)


class Wizard:
    """Represent a wizard."""

    def __init__(self, name, wand=None):
        """
        Use check_wand method.

        :param name:
        :param wand:
        """
        self.name = name
        if wand is not None:
            if Wand.check_wand(wand):
                raise MismatchError("The wand like that does not exist!")
            self.wand = wand
        self.wand = wand

    def set_wand(self, wand):
        """
        Check whether wand is correct.

        :param wand:
        :return:
        """
        if Wand.check_wand(wand):
            raise MismatchError("The wand like that does not exist!")
        else:
            self.wand = wand

    def get_wand(self):
        """
        Return wand used by wizard.

        :return:
        """
        return self.wand

    def __str__(self):
        """
        Return wizards name.

        :return:
        """
        return str(self.name)


class School:
    """Represent a school."""

    schools = [
        "Hogwarts School of Witchcraft and Wizardry", "Durmstrang Institute",
        "Ilvermorny School of Witchcraft and Wizardry", "Castelobruxo",
        "Beauxbatons Academy of Magic"
    ]

    def __init__(self, name: str):
        """
        Save school name to self.

        :param name:
        """
        self.students = []
        if name in School.schools:
            self.name = name
        else:
            raise MismatchError("There is no such school!")

    def add_wizard(self, wizard):
        """
        Add new wizard into school.

        "{wizard name} is already studying in this school!"
        "{wizard name} started studying in {school name}.".
        :param wizard:
        :return:
        """
        if isinstance(wizard, Wizard):
            if wizard.get_wand() is None or wizard.name is None:
                raise MismatchError("It's a filthy muggle!")
            if wizard in self.students:
                return "{} is already studying in this school!".format(wizard)
            else:
                self.students.append(wizard)
                return "{} started studying in {}.".format(wizard, self)
        else:
            raise MismatchError("It's a filthy muggle!")

    def remove_wizard(self, wizard):
        """
        If wizard left school, remove.

        :param wizard:
        :return:
        """
        if wizard in self.students:
            self.students.remove(wizard)

    def get_wizards(self):
        """
        Return list of all wizards in that school.

        :return:
        """
        return self.students

    def get_wizard_by_wand(self, wand):
        """
        Find wizard who owns that wand.

        :param wand:
        :return:
        """
        if Wand.check_wand(wand):
            raise MismatchError("The wand like that does not exist!")
        for each in self.students:
            if wand == Wizard.get_wand(each):
                return each
        return None

    def __str__(self):
        """
        Return name of school.

        :return:
        """
        return self.name


class MismatchError(Exception):
    """
    Class MismatchError inherits its properties from Exception class.

    Should have user-defined message.
    """

    def __init__(self, message):
        """
        Class constructor.

        :param message: user message
        """
        self.message = message


if __name__ == '__main__':

    wand1 = Wand("Holly", "Phoenix feather")
    wand2 = Wand("Vine", "Dragon heartstring")
    bad_wand = Wand(None, "empty")
    assert str(wand1) == 'Holly, Phoenix feather'
    assert str(wand2) == 'Vine, Dragon heartstring'
    wizard1 = Wizard("Harry Potter")
    wizard2 = Wizard("Hermione Granger")
    assert str(wizard1) == 'Harry Potter'
    assert str(wizard2) == 'Hermione Granger'
    bad_wizard = Wizard(None, None)
    school = School("Hogwarts School of Witchcraft and Wizardry")
    assert str(school) == 'Hogwarts School of Witchcraft and Wizardry'
    assert wizard1.get_wand() is None
    wizard1.set_wand(wand1)
    assert str(wizard1.get_wand()) == 'Holly, Phoenix feather'
    # wizard1.set_wand(bad_wand)  # --> MismatchError: The wand like that does not exist!
    assert school.add_wizard(wizard1) == 'Harry Potter started studying in Hogwarts School of Witchcraft and Wizardry.'
    assert school.get_wizards().__len__() == 1
    # school.add_wizard(wizard2)  # --> MismatchError: It's a filthy muggle!
    # school.add_wizard(bad_wizard)  # --> MismatchError: It's a filthy muggle!
    wizard2.set_wand(wand2)
    assert school.add_wizard(wizard2) == 'Hermione Granger started studying in Hogwarts School of Witchcraft and Wizardry.'
    assert school.get_wizards().__len__() == 2
    assert school.add_wizard(wizard1) == 'Harry Potter is already studying in this school!'
    assert str(school.get_wizard_by_wand(wand1)) == 'Harry Potter'
    assert str(school.get_wizard_by_wand(wand2)) == 'Hermione Granger'
    school.remove_wizard(wizard1)
    assert school.get_wizard_by_wand(wand1) is None
    School.schools.append("Example school")
    assert "Example school" in School.schools
