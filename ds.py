import zlib
import os
import re
columns = []
File = 'New Database'
       
def path(root) :
       os.chdir(root)

parent = os.getcwd()

def db() :
       try :
              with open(File + ".ds", "rb") as myfile:
                     f_content = myfile.read()
       except IOError :
              f_content = ''
              for item in columns :
                     f_content+= item
                     f_content+= '!@#@!'              
              f_content = zlib.compress(f_content)
              with open(File + ".ds", "wb") as myfile:
                     myfile.write(f_content)
              os.mkdir(File + '__ds')                            
              List = list('qwertyuiopasdfghjklzxcvbnm1234567890_')
              #List = list('amndro')
              for item1 in List :
                     os.mkdir(parent + chr(92) + File + '__ds' + chr(92) + item1)                     
              for item1 in List :
                     for item2 in List :
                            os.mkdir(parent  + chr(92) + File + '__ds' + chr(92) + item1 + chr(92) + item2)
                            f_content = '!@@@!'
                            f_content = zlib.compress(f_content)
                            os.chdir(parent + chr(92) + File + '__ds' + chr(92) + item1 + chr(92))
                            with open(File + ".ds", "wb") as myfile:
                                   myfile.write(f_content)
              print 'Stage1 Completed'
              for item1 in List :
                     for item2 in List :
                            for item3 in List :
                                   os.mkdir(parent + chr(92) + File + '__ds' + chr(92) + item1 + chr(92) + item2 + chr(92) + item3)
                                   f_content = '!@@@!'
                                   f_content = zlib.compress(f_content)
                                   os.chdir( parent  + chr(92) + File + '__ds' + chr(92) + item1 + chr(92) + item2 + chr(92) )
                                   with open(  File + ".ds", "wb") as myfile:
                                          myfile.write(f_content)
              print 'Stage2 Completed'
              for item1 in List :
                     for item2 in List :
                            for item3 in List :
                                   os.chdir(parent + chr(92) + File + '__ds' + chr(92) + item1 + chr(92) + item2 + chr(92) + item3)
                                   f_content = '!@@@!'
                                   f_content = zlib.compress(f_content)                                   
                                   with open(  File + ".ds", "wb") as myfile:
                                          myfile.write(f_content)
              print 'Stage3 Completed'
              os.chdir(parent)
              
   
def read() :       
       with open(File + ".ds", "rb") as myfile:
              f_content = myfile.read()
       f_content = zlib.decompress(f_content)       
       return f_content

def readFile(rFile) :
       with open(rFile + ".ds", "rb") as myfile:
              f_content = myfile.read()
       f_content = zlib.decompress(f_content)       
       return f_content


def save(content) :
            f_content = content
            os.chdir(parent)
            f_content = zlib.compress(f_content)
            with open(File + ".ds", "wb") as myfile:
                   myfile.write(f_content)

def saveFile(content,rFile) :
            f_content = content            
            f_content = zlib.compress(f_content)
            with open(rFile + ".ds", "wb") as myfile:
                   myfile.write(f_content)
            
              
def read_columns() :
       return read().splitlines()[0].split('!@#@!')[:-1]

def insert(Values) :
       content = read()
       content += '\n'
       value = ''
       for item in Values :
              value += item
              value += '!@#@!'              
       content += value       
       save(content)
       List = []
       for item in Values :
              item = item.lower()
              item = item.replace(' ','_')                            
              Patterns = []
              for i in range(len(item)) :
                     Patterns.append( parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + File )                                          
              for i in range(len(item) - 1) :
                     Patterns.append( parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + item[i+1] + chr(92) +  File )                     
              for i in range(len(item) - 2) :
                     Patterns.append( parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + item[i+1] + chr(92) + item[i+2] + chr(92) + File )
              for combination in list(set(Patterns)) :
                     f_content = readFile( combination )                     
                     f_content += value
                     f_content += '!@@@!'                     
                     saveFile(f_content, combination )                     
                     
              
def search(item) :
       item = item.lower()
       if len(item) > 3 :              
              f_content = readFile(parent + chr(92) + File + '__ds' + chr(92) +  item[0] + chr(92) + item[1] + chr(92) + item[2] + chr(92) + File)              
              Found = [ m.start() for m in re.finditer(item,f_content.lower())]
              Final = []
              for item in Found :                     
                     go , i = True , 0
                     while go :                            
                            if f_content[ item + i -5 : item + i ] == '!@@@!' :
                                   go = False
                                   x = item + i                                   
                            i -= 1
                     go , i = True , 0
                     while go :
                            if f_content[ item + i : item + i + 5] == '!@@@!' :
                                   go = False
                                   y = item + i
                            i += 1                 
                     Final.append( f_content[ x : y ].split('!@#@!')[:-1])                                          
              return list(set(map(tuple,Final)))
       elif len(item) == 3 :
              f_content = readFile(parent + chr(92) + File + '__ds' + chr(92) +  item[0] + chr(92) + item[1] + chr(92) + item[2] + chr(92) + File )
              content = f_content.split('!@@@!')
              content = content[1:-1]
              #content[0] = content[0][5:]
              #content[len(content) - 1] = content [len(content)-1][:-5]
              Final = []
              for item in content :
                     Final.append(item.split('!@#@!')[:-1])
              return list(set(map(tuple,Final)))
       elif len(item) == 2 :
              f_content = readFile(parent + chr(92) + File + '__ds' + chr(92) +  item[0] + chr(92) + item[1] + chr(92)  + File )                     
              content = f_content.split('!@@@!')
              content = content[1:-1]
              #content[0] = content[0][5:]
              #content[len(content) - 1] = content [len(content)-1][:-5]
              Final = []              
              for item in content :                     
                     Final.append(item.split('!@#@!')[:-1])
              return list(set(map(tuple,Final)))
       else :
              f_content = readFile(parent + chr(92) + File + '__ds' + chr(92) +  item[0] + chr(92) + File )
              content = f_content.split('!@@@!')
              content = content[1:-1]
              #content[0] = content[0][5:]
              #content[len(content) - 1] = content [len(content)-1][:-5]
              Final = []              
              for item in content :                     
                     Final.append(item.split('!@#@!')[:-1])
              return list(set(map(tuple,Final)))

def searchColumn(item,column_name) :
       item = item.lower()
       query = item
       index = 0
       for i in read_columns() :
              if i == column_name :
                     break
              index+=1
       Final = []       
       for result in search(item) :
              if query in result[index].lower() :                            
                            Final.append(list(result) )                   
       #return  list(set(map(tuple,Final)))
       return Final
       
def delete(item) :
       query , item = item.lower().replace(' ','_') , item.lower().replace(' ','_')
       print 'This will delete following records \n '
       i = 1
       for item in search(query) :              
              print i , ' : ' , item
              i+=1
       print '\n Enter "Yes" or "y" to continue  \n'
       Combination = []
       for outer in search(query) :
              temp = []
              for item in outer :
                     item = item.replace(' ','_')
                     item = item.lower()
                     for i in range(len(item)) :
                            temp.append(parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + File )
                     for i in range(len(item) - 1 ) :
                            temp.append(parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + item[i+1] + chr(92) + File )
                     for i in range(len(item) - 2 ) :
                            temp.append(parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + item[i+1] + chr(92) + item[ i +2 ] + chr(92) + File )
              Combination.append(list(set(temp)))
       if raw_input().lower()[0] == 'y' :
              for item in Combination :
                     for inner in item :
                            f_content = readFile(inner)
                            Found = [ m.start() for m in re.finditer(query,f_content.lower()) ]
                            print  inner[23:-4] , '     :   ' , Found
                            for num in Found :
                                   go , i = True , 0
                                   while go :
                                          if f_content[ num + i -5 : num + i ] == '!@@@!' :
                                                 go = False
                                                 x = num + i
                                          i -= 1
                                   go , i = True , 0
                                   while go :
                                          if i > len(f_content) :
                                                 break
                                          if f_content[ num + i : num + i + 5] == '!@@@!' :
                                                 go = False
                                                 y = num + i
                                          i += 1
                                   if i <= len(f_content) :
                                          f_content = f_content.replace(f_content[ x - 5 : y ],'',1)
                                   saveFile(f_content,inner)
              print 'Records deleted'
              
def deleteColumn(item,column) :
       query , item = item.lower().replace(' ','_') , item.lower().replace(' ','_')
       print 'This will delete following records \n '
       i = 1
       for item in searchColumn(query,column) :              
              print i , ' : ' , item
              i+=1
       print '\n Enter "Yes" or "y" to continue  \n'
       Combination = []       
       for outer in searchColumn(query,column) :
              temp = []
              for item in outer :
                     item = item.replace(' ','_')                     
                     for i in range(len(item)) :
                            temp.append(parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + File )
                     for i in range(len(item) - 1 ) :
                            temp.append(parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + item[i+1] + chr(92) + File )
                     for i in range(len(item) - 2 ) :
                            temp.append(parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + item[i+1] + chr(92) + item[ i +2 ] + chr(92) + File )
              Combination.append(list(set(temp)))                     
       if raw_input().lower()[0] == 'y' :
              for item in Combination  :
                     for inner in item :
                            f_content = readFile(inner)
                            Found = [ m.start() for m in re.finditer(query,f_content.lower()) ]
                            for num in Found :
                                   go , i = True , 0
                                   while go :
                                          if f_content[ num + i -5 : num + i ] == '!@@@!' :
                                                 go = False
                                                 x = num + i
                                          i -= 1
                                   go , i = True , 0
                                   while go :
                                          if i > len(f_content) :
                                                 break
                                          if f_content[ num + i : num + i + 5] == '!@@@!' :
                                                 y = num + i
                                                 go = False
                                          i += 1
                                   if i <= len(f_content) :
                                          f_content = f_content.replace(f_content[ x - 5 : y ],'',1)
                                          saveFile(f_content,inner)                            
       print 'Records deleted'
       
def update(A,B) :
       identifier = A[0]
       identifier_column = A[1]
       value = B [0]
       column = B[1]
       index = 0
       for i in read_columns() :
              if i == column :
                     break
              index+=1       
       query , i = identifier.lower() , 1
       print 'The followin g records will be updated : '       
       for item in searchColumn(query,column) :
              print i , '  ' , item
              i+=1
       print '\n Enter "Yes" or "y" to continue  \n'       
       if raw_input().lower()[0] == 'y' :
              for item in searchColumn(query,column) :
                     item = list(item)
                     item[index] = str(value)
                     print item
                     deleteColumnF(identifier,identifier_column)
                     print 'deleted'
                     #insert(item)              
              print 'Records updated'

def deleteColumnF(item,column) :
       query , item = item.lower().replace(' ','_') , item.lower().replace(' ','_')       
       i = 1
       Combination = []       
       for outer in searchColumn(query,column) :
              temp = []
              for item in outer :
                     item = item.replace(' ','_')                     
                     for i in range(len(item)) :
                            temp.append(parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + File )
                     for i in range(len(item) - 1 ) :
                            temp.append(parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + item[i+1] + chr(92) + File )
                     for i in range(len(item) - 2 ) :
                            temp.append(parent + chr(92) + File + '__ds' + chr(92) +  item[i] + chr(92) + item[i+1] + chr(92) + item[ i +2 ] + chr(92) + File )
              Combination.append(list(set(temp)))                     
       if 1 > 0 :
              for item in Combination  :
                     for inner in item :
                            f_content = readFile(inner)
                            Found = [ m.start() for m in re.finditer(query,f_content.lower()) ]
                            for num in Found :
                                   go , i = True , 0
                                   while go :
                                          if f_content[ num + i -5 : num + i ] == '!@@@!' :
                                                 go = False
                                                 x = num + i
                                          i -= 1
                                   go , i = True , 0
                                   while go :
                                          if i > len(f_content) :
                                                 break
                                          if f_content[ num + i : num + i + 5] == '!@@@!' :
                                                 y = num + i
                                                 go = False
                                          i += 1
                                   if i <= len(f_content) :
                                          f_content = f_content.replace(f_content[ x - 5 : y ],'',1)
                                   saveFile(f_content,inner)                                   
