spacer=''
astericks=''
maxLineCounter=int(input('Enter number of lines: '))
counter=0
increamerter=1
while counter!=-1:
    spacer=spacer.join(' ' for a in range(maxLineCounter-counter))
    astericks=astericks.join('*' for a in range(counter*2+1))
    print(spacer+astericks)
    spacer=''
    astericks=''
    counter+=increamerter
    if(counter==maxLineCounter):
        increamerter=-1




