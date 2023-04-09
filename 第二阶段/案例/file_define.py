from data_define import Record
import json

class File_Reader:
    def __init__(self, path):
        self.path = path
    
    def read_data(self):
        pass

class TextFileReader(File_Reader):
    def __init__(self, path):
        self.path = path
    
    def read_data(self):
        f = open(self.path, 'r', encoding="UTF-8-sig")
        l =[]
        for line in f.readlines():
            line = line.strip()
            data = Record(line.split(',')[0], line.split(',')[1], int(line.split(',')[2]), line.split(',')[3])
            l.append(data)
        f.close()
        return l
    
class JsonFileReader(File_Reader):
    def __init__(self, path):
        self.path = path
    
    def read_data(self):
        f = open(self.path, 'r', encoding="UTF-8-sig")
        l =[]
        for line in f.readlines():
            data_dict = json.loads(line)
            data = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            l.append(data)
        f.close()
        return l

if __name__ == '__main__':
    text_file_reader = TextFileReader('H:/pylearning/第二阶段/2011年1月销售数据.txt')
    data = text_file_reader.read_data()
    for i in data:
        print(i)

    json_file_reader = JsonFileReader('H:/pylearning/第二阶段/2011年2月销售数据JSON.txt')
    data = json_file_reader.read_data()
    for i in data:
        print(i)
