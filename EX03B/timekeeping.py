"""Converting time from one system to another."""


def convert(kella_aeg, mitu_sec_minutis, uus_sec_minutis):
    """
    Annan programmile sisse kellaja, ja ytlen mitu sekundit on minutis. Arvutan ka mitu sekundit kokku on.

    :param kella_aeg: Ette antud kella aeg
    :param mitu_sec_minutis: Mitu sekundit on selle aja-arvamise yhes minutis
    :param uus_sec_minutis: Mitu sekundit on uue aja-arvamise yhes minutis
    :return:
    """
    if kella_aeg == "00:00":
        return kella_aeg
    elif int(kella_aeg[-2:]) >= int(mitu_sec_minutis):
        return None
    all_seconds = mitu_sec_minutis * int(kella_aeg[:2]) + int(kella_aeg[-2:])
    MM = all_seconds // uus_sec_minutis
    SS = all_seconds % uus_sec_minutis
    return ymarda(MM, SS)


def ymarda(minutid, sekundid):
    """
    Teisendan aja 6igele kujule.

    :param minutid: kui on 10st v2iksem, peab 0 numbri ees olema siis -et v2ljastatud s6ne n2eks kellaja moodi v2lja
    :param sekundid: teen kindlaks, et sekundid ymardatakse ja v2ljastatakse kahendkujul
    :return:
    """
    sekundid = int(round(sekundid))
    if minutid < 10 and sekundid < 10:
        return str(0) + str(minutid) + ":" + str(0) + str(int(str(sekundid)[:2]))
    if minutid < 10:
        return str(0) + str(minutid) + ":" + str(int(str(sekundid)[:2]))
    if sekundid < 10:
        return str(minutid) + ":" + str(0) + str(int(str(sekundid)[:2]))
    else:
        return str(minutid) + ":" + str(int(str(sekundid)[:2]))


if __name__ == '__main__':
    print(convert("99:00", 1, 100))
    print(convert("10:00", 30, 100))
    print(convert("12:12", 20, 30))
