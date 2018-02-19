f = open('./format.txt','r')

# 딕셔너리
microformat = dict()
i=0
while True:
    # 명령어 읽어오기
    line = f.readline()
    if not line: break
    if line[0]=='\n':break
    div = line.find(':')
    line = line[:-1] # 엔터 문자 제거

    # 한 줄의 명령어를 코드와 명령어 이름으로 분리
    code = line[:div]
    name = line[div+1:]
    code = code.strip()
    name = name.strip()

    print(code+' = '+name)

    # 딕셔너리
    microformat[name] = code
    
    i = i+1
print(microformat)
print('\n명령어 형식 등록 완료')

f.close()

# 번역
f = open('./program.txt','r')

line = f.readline()
if line.find('address bit :') == -1 :
    print('address bit를 지정해주세요.')
    exit()

div = line.find(':')
addressbit = int(line[div+1:])
translated = list(range(2**addressbit))

#0 채우기
for i in range(2**addressbit):
    translated[i] = '0'

while True:
    # 명령어 읽어오기
    line = f.readline()
    if not line: break
    
    if line[0]!='\n':
        if line.find('ORG') == -1 :
            
            print(line[:-1]+' -> ',end='')
            # 명령어 분리하기
            linesplited = line.split()

            word = ''
            for i in range(3):
                linesplited[i] = microformat[linesplited[i]]
                word = word + linesplited[i]

            print(word+'\n')
            translated[address] = word
            address = address + 1
            
        else :
            print('\n')
            div = line.find(':')
            address = line[:div]
            address = [int(s) for s in address.split() if s.isdigit()]
            address = int(address[0])

# text 조립
text = ''
for i in range(2**addressbit):
    hexed = hex(int(translated[i],2))
    hexed = hexed[2:]
    text = text + hexed + ' '

f.close()

f = open('rom.txt','w')
f.write('v2.0 raw\n')
f.write(text)
f.close()

    
