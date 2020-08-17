import os
def pconfig(cfgreader):
	compiler = 'gcc'
	cflags = ' '
	lflags = ' '
	files = ' '
	for row in cfgreader:
		if not len(row) > 1:
			continue
		if row[0].lower() == 'compiler':
			compiler = row[1]
		if row[0].lower() == 'cflags':
			for i in row[1:]:
				cflags = cflags + i + ' '
		if row[0].lower() == 'addlib':
			lflags = lflags + '-l' + row[1] + ' '
		if row[0].lower() == 'files':
			for i in row[1:]:
				files = files + '"' + os.path.abspath(i) + '" '
	command = compiler + cflags + files + lflags
	return [command]
id = "CBuild"
