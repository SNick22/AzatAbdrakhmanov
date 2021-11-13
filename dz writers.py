class Writers:
     def __init__(self, birth, death, name, surname, pseudonim, country, works):
          """

          :param birth: дата рождения
          :param death: дата смерти
          :param name: имя
          :param surname: фамилия
          :param pseudonim: псевдоним
          :param country: страна
          :param works: работы
          """
          self.bith = birth
          if death == "жив":
               self.death = None
          else:
               self.death = death
          self.name = name
          self.surname = surname
          self.pseudonim = pseudonim
          self.country = country
          self.works = works
     def addwork(self, newwork):
          """

          :param newwork: новая работа
          """
          self.newwork = newwork
          self.works.append(self.newwork)
class Publisher:
     def __init__(self, name, country):
          """

          :param name: имя издателя
          :param country: страна издания
          """
          self.name = name
          self.country = country

class Work:
     def __init__(self, authors, publishers, year):
          """

          :param authors: авторы
          :param publishers: издатели
          :param year: год
          """
          self.authors = authors
          self.publishers = publishers
          self.year = year
     def addauthor(self, newauthor):
          """

          :param newauthor: новый автор
          :return: добавление нового автора
          """
          self.newauthor = newauthor
          self.authors.append(self.newauthor)
class Book(Work):
     def __init__(self, binding, cover, authors, publishers, year):
          """

          :param binding: переплет
          :param cover: обложка
          :param authors: авторы
          :param publishers: издатели
          :param year: год
          """
          super().__init__(authors, publishers, year)
          self.binding = binding
          self.cover = cover
class Magazine(Work):
    def __init__(self, cover, authors, publishers, year):
        """

        :param cover: обложка
        :param authors: авторы
        :param publishers: издатели
        :param year: год
        """
        super().__init__(authors, publishers, year)
        self.cover = cover

class Publication(Work):
    def __init__(self, place, authors, publishers, year):
        """

        :param place: место публикации
        :param authors: авторы
        :param publishers: издатели
        :param year: год
        """
        super().__init__(authors, publishers, year)
        self.place = place
lev = Writers(1828,1910,"Лев","Толстой",None,"Российская империя",["Война и мир"])
lev.addwork("Анна Каренина")
print(lev.works)
pub = Publisher("Русский вестник", "Российская империя")
print(pub.name)
warandpeace = Book("Твердый переплет", "Твердая обложка", ["Лев Николаевич Толстой"], ["Русский вестник"], 1865)
warandpeace.addauthor("тоже Лев Николаевич Толстой")
print(warandpeace.authors)
#