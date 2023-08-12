def rhythm (song):
    song = song.split()
    lst = []
    for word in song:
        count = 0
        for i in word:
            if i in 'абв':
                count += 1
        lst.append (count)
    return len(lst) == lst.count(lst[0])
song = input ('Винни, введи стишок: ')
print ('Парам пам-пам' if rhythm (song) == True else 'Пам парам')
