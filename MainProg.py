import sys
import dataForSQL
import dbConnectToSQL

def main(args):
    dt = dataForSQL.DataForSQL()
    # dt.addreses()
    # dt.findId()
    dt.openCSV()
    dt.manySelect()


    
if __name__ == "__main__":
    main(sys.argv)