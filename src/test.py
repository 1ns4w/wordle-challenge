from json import dumps, loads

infile = open('out/palabras_por_fecha.json', 'a+')
infile.write(dumps('[]'))
print(infile.read())