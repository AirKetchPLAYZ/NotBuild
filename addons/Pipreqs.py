import os


def pconfig(cfgreader):
    pypackages = " "
    iterp = "python3"
    for row in cfgreader:
        if not len(row) > 1:
            continue
        if row[0].lower() == 'interpreter':
            iterp = row[1]
        if row[0].lower() == 'pypackages':
            for i in row[1:]:
                pypackages = pypackages + i + ' '
    if pypackages.strip() != "":
        command = iterp + " -m pip install" + pypackages
    return [command]

id = "Pipreqs"
