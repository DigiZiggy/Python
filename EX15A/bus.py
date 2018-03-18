"""Program to find closest departure time."""


class ReadFile:
    """Read the file."""

    def __init__(self, file: str):
        """
        Read the file.

        :param file:
        """
        self.file = file
        try:
            with open(self.file, encoding='utf-8', mode='r') as file:
                bus_times = file.read()
                file.close()
        except Exception:
            print("File not found!")
            raise Exception("File not found!")
        self.bus_times = bus_times

    def return_file(self):
        """
        Return file.

        :return:
        """
        return self.bus_times


class Input:
    """Deal with customer input."""

    def __init__(self, input):
        """
        Deal with customer input.

        :param file:
        """
        self.input = input

    @staticmethod
    def check_time(input):
        """
        Check time.

        :return:
        """
        allowed = "0123456789:"
        time = input.split(":")
        for each in input:
            if each not in allowed:
                raise Exception
        hours = [ch for ch in time[0]]
        if input[-3] != ":" or int(time[1]) >= 60:
            raise Exception
        if hours[0] == "0" or input == "":
            raise Exception
        if time[0] == "00" or time[0] == "0":
            raise Exception
        if int(time[0]) > 24:
            raise Exception
        if len(time[0]) > 2 or len(time[1]) > 2:
            raise Exception
        return input


class Main:
    """Represent a main."""

    def __init__(self, file: str):
        """
        Read file.

        :param file:
        """
        file = ReadFile(file)
        self.file = file

    def get_departure_time(self):
        """
        Your bus will depart at {departure time (HH:mm)}.

        :param time_now:
        :return:
        """
        user_input = input("What is the time now?")
        Input.check_time(user_input)
        time = user_input.split(":")
        split_up = self.file.return_file().split('\n')
        split_up_dict = {}
        for each in split_up:
            ssplit = each.split()
            key = ssplit[0]
            ssplit.pop(0)
            split_up_dict[key] = ssplit
        end_time = self.get_time(split_up_dict, time)
        print("Your bus will depart at {}".format(end_time))

    def get_time(self, split_up_dict, time):
        """
        something.

        :param input:
        :return:
        """
        keys = list(split_up_dict.keys())
        if self.does_input_hour_excist(split_up_dict, time):
            if_this = self.does_input_hour_excist(split_up_dict, time)
            return "{}".format(if_this)
        else:
            if time[0] in keys:
                hours = time[0]
            minutes = min([int(i) for i in split_up_dict[hours]], key=lambda x: abs(x - int(time[1])))
            if minutes <= int(time[1]):
                if minutes != int(split_up_dict[hours][-1]):
                    minutes = [int(i) for i in split_up_dict[hours]][[int(i) for i in split_up_dict[hours]].index(minutes) + 1]
                    return "{}:{}".format(hours, minutes)
                elif minutes == int(split_up_dict[hours][-1]):
                    if keys.index(hours) + 1 >= len(keys):
                        hours = keys[0]
                    else:
                        hours = keys[keys.index(hours) + 1]
                    minutes = split_up_dict[hours][0]
                    return "{}:{}".format(hours, minutes)
            if time[1] == int(split_up_dict[hours][-1]) and hours == keys[-1]:
                minutes = int(split_up_dict[keys[0]][0])
                hours = keys[0]
            if minutes == int(split_up_dict[hours][-1]) and minutes <= int(time[1]):
                hours = keys[keys.index(hours) + 1]
                minutes = split_up_dict[hours][0]
            if len(str(minutes)) < 2:
                minutes = "0{}".format(minutes)
            return "{}:{}".format(hours, minutes)

    def does_input_hour_excist(self, split_up_dict, time):
        """
        Check whether input hour is current.

        :return:
        """
        keys = list(split_up_dict.keys())
        if time[0] not in keys:
            hourslist = []                 # finds hour values that are bigger than input hour value
            for each in keys:
                if int(each) > int(time[0]):
                    hourslist.append(each)
            if hourslist == []:
                hours = keys[0]
                minutes = split_up_dict[keys[0]][0]
                return "{}:{}".format(hours, minutes)
            if hourslist == []:
                hours = keys[0]
            else:
                hours = hourslist[0]
            minutes = split_up_dict[hours][0]
            return "{}:{}".format(hours, minutes)


if __name__ == '__main__':

    Main("bussiajad2.txt").get_departure_time()
