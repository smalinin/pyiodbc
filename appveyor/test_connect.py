import sys
import pyiodbc
c = pyiodbc.connect(sys.argv[1])
c.close()
