"""Orwell 1984."""


class Citizen:
    """Class which represents a single citizen."""

    def __init__(self, name, party, status="citizen"):
        """
        Class constructor.

        :param name: name of the citizen
        :param party: party which he belongs to
        :param status: status
        """
        allowed_statuses = ["citizen", "prole", "nonperson", "under surveillance"]
        if status in allowed_statuses:
            self.status = status
            self.name = name
            self.party = party
            if status == "prole":
                self.party = None
            if status == "nonperson":
                self.name = None
                self.party = None
        if status not in allowed_statuses:
            self.status = "citizen"
            self.name = name
            self.party = party
        if self.party is not None:
            self.party.add_party_member(self)

    def set_party(self, party):
        """
        Set citizen's party. The method does not return anything.

        :param party: new party (Inner or Outer, both are Party class instances)
        """
        if (isinstance(party, Party)) or party is None:
            if self.party is not None and self in self.party.get_party_members():
                self.party.remove_party_member(self)
            if party is not None:
                print(self)
                party.add_party_member(self)
            self.party = party

    def get_party(self):
        """
        Get the citizen's party.

        :return: party object
        """
        return self.party

    def set_status(self, status):
        """
        Set citizen's status. The method does not return anything.

        :param status: new status
        """
        allowed_statuses = ["citizen", "prole", "nonperson", "under surveillance"]
        if status in allowed_statuses:
            self.status = status
        if status == "prole":
            self.party = None
        if status == "nonperson" and self.party is not None:
            self.party.vaporize(self)

    def get_status(self):
        """
        Get the citizen's status.

        :return: status
        """
        return self.status

    def set_name(self, name):
        """
        Set the citizen's name. The method does not return anything.

        :param name: new name
        """
        self.name = name

    def get_name(self):
        """
        Get the citizen's name.

        :return: name
        """
        return self.name

    def __str__(self):
        """
        Compute string representation of this object.

        :return: f"BIG BROTHER IS WATCHING YOU, {self.name}"
        """
        return "BIG BROTHER IS WATCHING YOU, {}".format(self.name)


class Party:
    """Party class."""

    def __init__(self):
        """Class constructor."""
        self.party_members = []

    def get_party_members(self):
        """
        Get the list of party members.

        :return: list
        """
        return self.party_members

    def add_party_member(self, citizen):
        """
        Add the citizen to the party members' list.

        Citizen must be instance of Citizen class, must have name, must not already be a member and must not have a
        'nonperson' status.
        Does not return anything.
        :param citizen Citizen class instance
        """
        if (isinstance(citizen, Citizen)) and citizen.name != "" and citizen.name is not None and citizen.status != "nonperson" and citizen not in self.party_members:
            citizen.party = self
            self.party_members.append(citizen)

    def remove_party_member(self, citizen):
        """Remove the citizen from the party members' list."""
        if citizen in self.party_members:
            self.party_members.remove(citizen)

    def vaporize(self, citizen):
        """
        Remove the citizen from the party members, set his name and party to None and status to nonperson.

                    The method does not return anything.
        :param citizen: Citizen class instance

        """
        if citizen in self.party_members:
            self.party_members.remove(citizen)
            citizen.party = None
            citizen.name = None
            citizen.status = "nonperson"

    def get_privileges(self):
        """
        Get privileges granted by party.

        :return: None
        """
        return None

    @staticmethod
    def get_slogan():
        r"""
        Get the party slogan.

        :return: "WAR IS PEACE\nFREEDOM IS SLAVERY\nIGNORANCE IS STRENGTH"
        """
        return "WAR IS PEACE\nFREEDOM IS SLAVERY\nIGNORANCE IS STRENGTH"


class InnerParty(Party):
    """Inner party class, which extends the Party class."""

    def get_privileges(self):
        """
        Get privileges granted by party (Override).

        :return: "Everything"
        """
        return "Everything"

    def __str__(self):
        """
        Compute string representation of this object.

        :return: "Inner party"
        """
        return "Inner party"


class OuterParty(Party):
    """Outer party class, which extends the Party class."""

    def __str__(self):
        """
        Compute string representation of this object.

        :return: "Outer party"
        """
        return "Outer party"


class BigBrother:
    """Big brother class."""

    def __init__(self, inner_party, outer_party):
        """
        Class constructor.

        :param inner_party: inner party object
        :param outer_party: outer party object
        """
        self.inner_party = inner_party
        self.outer_party = outer_party
        self.vaporized = 0

    def get_all_citizens(self):
        """
        Get all citizens who are members in the parties.

        :return: list
        """
        return self.outer_party.get_party_members() + self.inner_party.get_party_members()

    def massive_vaporize(self, status):
        """
        Vaporize people with a given status.

        :param status: string
        :return: number of vaporized people per session
        """
        session_vaper = 0
        for citizen in self.get_all_citizens():
            if citizen.status == status:
                citizen.party.vaporize(citizen)
                session_vaper += 1
        self.vaporized += session_vaper
        return session_vaper

    def get_number_of_vaporized(self):
        """
        Get number of vaporized people of all time.

        :return: integer
        """
        return self.vaporized


if __name__ == '__main__':
    ip = InnerParty()
    op = OuterParty()

    c = Citizen("Winston Smith", op, "under surveillance")
    c1 = Citizen("Julia", op, "under surveillance")

    assert (c.get_name()) == 'Winston Smith'
    assert str(c.get_party()) == 'Outer party'
    assert (c.get_status()) == 'under surveillance'
    assert str(c) == 'BIG BROTHER IS WATCHING YOU, Winston Smith'
    assert str(c1) == 'BIG BROTHER IS WATCHING YOU, Julia'
    c.set_party(ip)
    assert str(c.get_party()) == 'Inner party'
    assert len(ip.get_party_members()) == 1
    assert len(op.get_party_members()) == 1
    assert not (c in op.get_party_members())
    c.set_party(op)
    assert str(c.get_party()) == 'Outer party'
    assert len(op.get_party_members()) == 2

    c2 = Citizen("O'Brien", ip)
    assert (c2.get_name()) == "O'Brien"
    assert str(c2.get_party()) == 'Inner party'
    assert (c2.get_status()) == 'citizen'

    c3 = Citizen("Syme", op, "nonperson")
    assert (c3.get_name()) is None
    assert (c3.get_party()) is None
    assert (c3.get_status()) == 'nonperson'

    c4 = Citizen("Smb", op, "prole")

    assert (c4.get_name()) == 'Smb'
    assert (c4.get_party()) is None
    assert (c4.get_status()) == 'prole'

    assert len(ip.get_party_members()) == 1
    assert len(op.get_party_members()) == 2
    assert str(ip) == 'Inner party'
    assert str(op) == 'Outer party'
    assert (ip.get_privileges()) == 'Everything'
    assert (op.get_privileges()) is None

    assert (ip.get_slogan()) == 'WAR IS PEACE\nFREEDOM IS SLAVERY\nIGNORANCE IS STRENGTH'

    bb = BigBrother(ip, op)
    assert len(bb.get_all_citizens()) == 3
    assert (bb.massive_vaporize("under surveillance")) == 2
    assert len(bb.get_all_citizens()) == 1
    assert (c.get_name()) is None
    assert (c.get_party()) is None
    assert (c.get_status()) == 'nonperson'
    assert len(ip.get_party_members()) == 1
    assert len(op.get_party_members()) == 0
    assert (bb.massive_vaporize("citizen")) == 1
    assert (bb.get_number_of_vaporized()) == 3
