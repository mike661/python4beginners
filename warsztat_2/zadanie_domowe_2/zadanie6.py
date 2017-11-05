# Zadanie 6
# Jesteś administratorem Bardzo Wysokiego Budynku Biurowego BWBB.
# Masz listę ile osób znajduje się na kolejnych piętrach BWBB: `lista_osob` (czyli wartość lista_osób[5] to liczba osób na piętrze nr 5) - zawiera ona tylko liczby całkowite
# W budynku znajduje się określona liczba ewakuacyjnych klatek schodowych: `liczba_klatek_schodowych` - jest to liczba całkowita
# Każda z klatek pozwala na jednoczesne poruszanie się kilku osób obok siebie: `liczba_osob_w_rzedzie` (liczba całkowita).
# Odstęp czasowy miedzy każdym ewakuowanym rzędem osób to 1 sekunda.
# `tempo_schodzenia` to liczba sekund potrzebna na przejście jednego piętra. Uznajemy, że wszyscy schodzą w tym samym tempie
# Ewakuacja budynku zaczyna się od najwyższego piętra, piętro po piętrze w dół.
# Po jakim czasie powinna zaczynać się ewakuacja dla poszczególnych pięter żeby nie tworzyły się zatory?
# Zatory nie tworzą się wtedy, gdy osoby z wyższych minęły już piętro, które jest w danym momencie ewakuowane. 
# Funkcja ewakuacja powinna zwracać listę z intami po ilu sekundach od rozpoczęcia ewakuacji budynku  na każdym piętrze zostanie włączony alarm 
# czyli result[6] przechowuje po ilu sekundach został włączony alarm na szóstym piętrze

# Osoby ewakuowane same rozkładają się po równo na liczbę zejść ewakuacyjnych
# Piętro zaczyna się ewakuować od razu po uruchomieniu na nim alarmu
# Argumenty do funkcji będą przekazane po nazwie, jako keyword

def ewakuacja(lista_osob, liczba_klatek_schodowych, liczba_osob_w_rzedzie, tempo_schodzenia):
    rev_lista_osob = lista_osob[::-1]
    result = [0]
    for x in rev_lista_osob[0:-1]:
    	czekanie = x // (liczba_klatek_schodowych * liczba_osob_w_rzedzie) #ile sekund schodzą pełne rzędy osob
    	if x % (liczba_klatek_schodowych * liczba_osob_w_rzedzie) != 0:  #jesli istnieje reszta z dzielenia to dodajemy jedna sekunde (rownoznaczne z tym ze jest jeszcze niepelny rzad, ktory musi zejsc)
    		result.append(result[-1] + czekanie+31)
    	else:
    		result.append(result[-1] + czekanie+30)
    return result[::-1]


lista_osob = [5, 10, 15]
liczba_klatek_schodowych = 2
liczba_osob_w_rzedzie = 1
tempo_schodzenia = 30

assert [73, 38, 0] == ewakuacja(
    lista_osob=lista_osob,
    liczba_klatek_schodowych=liczba_klatek_schodowych,
    liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
    tempo_schodzenia=tempo_schodzenia
)