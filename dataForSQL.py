import dbConnectToSQL as db
import re
import csv

class DataForSQL(db.DbConnectSQL):
    def __init__(self) -> None:
        super().__init__()
        self.data = []
        self.ids = {}
        
    def addreses(self):
        with open('dataanswers.txt', encoding="utf-8-sig", mode ='r') as f:
            for lines in f:
                self.data.append(lines.rstrip()[:-10])
                
    def openCSV(self):
        with open('datacsv.csv', encoding="utf-8-sig", mode ='r') as f:
            csvFile = csv.reader(f, delimiter  = ';', quotechar=None)
            for line in csvFile:
                self.data.append(line)
                # print(type(line))

    def findId(self):
        for line in self.data:
            val = "%" + str(line) + "%"
            sql = "SELECT id FROM question WHERE questionnaire_id=183 AND name_rus LIKE '" + val + "'"
            self.mycursor.execute(sql)
            d=self.mycursor.fetchone()
            print(d)
            
    def manySelect(self):
        alldata = []
        for line in self.data:
            lineData=[]
            anketID = int(line[0])
            lineData.append(anketID)
            for question in line[1:]:
                sql = f"SELECT id FROM user_question_set WHERE user_task_id={anketID} AND parent_question_id={int(question)}"
                print(sql)
                self.mycursor.execute(sql)
                d=self.mycursor.fetchone()
                if d != None:
                    lineData.append(d[0])
                else: lineData.append(None)
                
            alldata.append(lineData)
            
        with open("questionSetID.txt", "w") as file1:
            for line in alldata:
                file1.writelines(';'.join(str(x) for x in line) + "\n")
            
        # for line in alldata:
        #     print(line)
            
        

        
    


        
        