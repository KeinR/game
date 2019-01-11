def save(p, sc, sab):
    file = open("game/save.txt", "w")
    file.write("p={} sc={} sab={}".format(p, sc, sab))
    file.close()


def load():
    p = "s"
    sc = False
    sab = False
    file = open("game/save.txt", "r")
    fileL = file.read().split()
    for value in fileL:
        if value[0] == "p":
            pvalue = value[2:]
            p = pvalue
        else:
            varT = ""
            var = ""
            for char in value:
                if char != "=":
                    varT += char
                if char == "=":
                    var = varT[:]
            val = value[len(var)+1:]
            if var == "sc":
                sc = bool(val[:])
            if var == "sab":
                sab = bool(val[:])
    file.close()
    return p, sc, sab
