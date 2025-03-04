#####################################
### TP 5 : Les fonctions (encore) ###
#####################################

### I) Calendrier ###
#Question 1
def isLeap(a : int) -> bool :
    '''Savoir si a est une année bissextile
    params : year -> l'année à déterminer
    return : bool'''
    return (a % 4 == 0 and a % 100 != 0) or a % 400 == 0

#Question 2
def nbDaysYears(a : int) -> int:
    '''Retourne le nombre de jours de l'année a
    params : a (annee)
    return : int (nb jours)
    '''
    return isLeap(a) + 365

#Question 3
def nbDaysMonth(a : int,m : int) -> int:
    '''Retourne le nombre de jours du mois m de l'année a
    params : a (annee) ; m (mois)
    return : int (nombre jours du mois
    '''
    bissextile = isLeap(a)
    if m in [1,3,5,7,8,10,12] :
        return 31
    elif m in [4,6,9,11] :
        return 30
    else :
        if bissextile : return 29
        else : return 28

#Question 4
def _getTimestamp(d : int, m : int, y : int) -> int:
    '''Renvoyer un pseudo-timestamp de la date ( nb de jours depuis l'an 1)
    params : d (jour),m(mois),y(annee)
    return : timestamp
    '''
    step = int()
    if y>=1 :
        step = 1
    else :
        step = -1
    timestamp = int()

    #on compte le nombre d'années entieres ecoulées depuis l'an 1
    for i in range(1,y,step) :
        if isLeap(i) :
            timestamp += 366
        else :
            timestamp += 365

    # on compte le nombre de mois ecoulées dans l'années en cours
    for i in range(1,m) :
        timestamp += nbDaysMonth(y,i)

    #on ajoute le nombre de jours du mois en cours
    timestamp += d

    return abs(timestamp)

def nbDaysInterval(start_day : int, start_month : int, start_year : int, \
end_day : int, end_month : int, end_year : int) -> int:
    '''Retourne le nombre de jours dans un intervalle donne
    params : start_day,start_month,start_year,end_day,end_month,end_year
    return : int le nombre de jour
    '''
    start_timestamp = _getTimestamp(start_day,start_month,start_year)
    end_timestamp = _getTimestamp(end_day, end_month, end_year)

    return end_timestamp - start_timestamp

#Question 5
week_daysList = ['lundi','mardi','mercredi','jeudi',
'vendredi','samedi','dimanche']

# on sait que le 4 nov 2024 (timestamp :739194)  est un lundi :
dataList = [739194,(4,11,2024)]

def getWeekDay(d : int, m : int, y : int) -> str:
    '''Retourner le jour de la semaine correspondant a une date donnee
    params : d (jour),m(mois),y(annee)
    return : str (jour de la semaine)
    '''
    timestampInt = _getTimestamp(d,m,y)
    intervalInt = nbDaysInterval(*dataList[1],d,m,y)
    return week_daysList[intervalInt%7]

#Question 6
def calendar(year : int) -> None:
    """Afficher le calendrier de l'annee year
    params : year
    return : None
    """
    monthList = ['janvier','février','mars','avril','mai','juin','juillet',
    'aout','septembre','octobre','novembre','decembre']

    print(f"###[{year}]###")

    for month in monthList:
        print(f"\n#[{month.upper()}]#\n")
        nbDaysInt = nbDaysMonth(year,monthList.index(month)+1)
        for dayInt in range(1,nbDaysInt+1) :
            print(f"{getWeekDay(dayInt,monthList.index(month)+1,year)} - \
{dayInt}")

def oneLineCalendar(year):
    exec('monthList = ["janvier","février","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]\nprint("###[{}]###".format(year))\nfor month in monthList:\n\tprint("#[{}]#".format(month.upper()))\n\tnbDaysInt = nbDaysMonth(year,monthList.index(month)+1)\n\tfor dayInt in range(1,nbDaysInt+1) :\n\t\tprint("{} -{}".format(getWeekDay(dayInt,monthList.index(month)+1,year),dayInt))')






















