from maze import mapprinter, pathcontroller

path, squares, sl = pathcontroller(sidelength = 11)
print path
mapprinter(path, sl)
