from catalog.models import Book, BookInstance, Language, Author, Genre

# BookInstance.objects.all().delete()
# Book.objects.all().delete()
# Language.objects.all().delete()
# Author.objects.all().delete()
# Genre.objects.all().delete()


# --------------------------------

sk = Author(first_name='Stephen',last_name='King',date_of_birth='1947-09-21')
ac = Author(first_name='Agatha', last_name='Christie',date_of_birth='1890-09-15', date_of_death='1976-01-12')
jb = Author(first_name='Jorge Luis', last_name='Borges',date_of_birth='1989-08-24', date_of_death='1986-06-14')
mb = Author(first_name='Mario', last_name='Benedetti',date_of_birth='1920-09-14',date_of_death='2009-05-17')

sk.save()
ac.save()
jb.save()
mb.save()

# --------------------------------

es = Language(name='Spanish')
fr = Language(name='French')
en = Language(name='English')
gr = Language(name='German')

es.save()
fr.save()
en.save()
gr.save()

# --------------------------------

genres = ['Horror', 'Sci-Fi', 'Drama', 'Thriller', 'Romance', 'Literary Fiction', 'Mistery']

horror = Genre(name='Horror')
scifi = Genre(name='Sci-Fi')
drama = Genre(name='Drama')
thriller= Genre(name='Thriller')
romance = Genre(name='Romance')
litfic = Genre(name='Literary Fiction')
mistery = Genre(name='Mistery')

horror.save()
scifi.save()
drama.save()
thriller.save()
romance.save()
litfic.save()
mistery.save()

# --------------------------------

carrie = Book(title='Carrie', summary='Set primarily in the then-future year of 1979, it revolves around the eponymous Carrie White, a friendless, bullied high-school girl from an abusive religious household who uses her newly discovered telekinetic powers to exact revenge on those who torment her.', pubdate='1974-04-05', isbn='9789871138999', author=sk, language=en)

mrmercedes = Book(title='Mr. Mercedes', summary='The stolen Mercedes emerges from the pre-dawn fog and plows through a crowd of men and women on line for a job fair in a distressed American city. Then the lone driver backs up, charges again, and speeds off, leaving eight dead and more wounded. The case goes unsolved and ex-cop Bill Hodges is out of hope when he gets a letter from a man who loved the feel of death under the Mercedes’s wheels…', pubdate='2015-12-29',isbn='9781501125607',author=sk,language=en)

kennedy = Book(title='11/22/63', summary='On November 22, 1963, three shots rang out in Dallas, President Kennedy died, and the world changed. What if you could change it back? Stephen King’s heart-stoppingly dramatic new novel is about a man who travels back in time to prevent the JFK assassination—a thousand page tour de force.', pubdate='2011-11-08', isbn='9781451627282', author=sk, language=en)

roger = Book(title='The Murder of Roger Ackroyd',summary='Roger Ackroyd knew too much. He knew that the woman he loved had poisoned her brutal first husband. He suspected also that someone had been blackmailing her. Then, tragically, came the news that she had taken her own life with an apparent drug overdose.', pubdate='1926-02-01', isbn='9780062073563', author=ac, language=en)

orient = Book(title='Murder on the Orient Express', summary='Just after midnight, the famous Orient Express is stopped in its tracks by a snowdrift. By morning, the millionaire Samuel Edward Ratchett lies dead in his compartment, stabbed a dozen times, his door locked from the inside. Without a shred of doubt, one of his fellow passengers is the murderer.', pubdate='1934-01-01', isbn='9780062073501', author=ac, language=en)

witness = Book(title='Witness for the Prosecution', summary="Leonard Vole stands in the dock, accused of murder. His wife can prove his innocence but when she takes the stand she denies his alibi. Can he escape the hangman's noose?", pubdate='1953-10-28', isbn='9780573702303', author=ac, language=en)

aleph = Book(title='El Aleph', summary='El cuento El Aleph de Jorge Luis Borges es uno de los más emblemáticos de este autor argentino. A tal punto llega el interés suscitado por este, que es considerado un cuento de culto en la comunidad de intelectuales. Existe más de una razón para eso.', pubdate='1949-02-02', isbn='9789500755764', author=jb, language=es)


ficciones = Book(title='Ficciones', summary='Ficciones es posiblemente la obra más reconocida de Jorge Luis Borges y un hito en la historia de la literatura. Aquí se encuentran lo policiaco («La muerte y la brújula») y lo fantástico («La lotería en Babilonia»), lo irreal («Las ruinas circulares») y lo imaginario («Tlön, Uqbar, Orbis Tertius»), el que Borges consideró acaso su mejor cuento («El Sur») y uno de los comienzos más cautivadores de un relato jamás escrito («Nadie lo vio desembarcar en la unánime noche»).Cada uno de los dieciséis cuentos reunidos en este libro es, en sí, pieza fundacional y celebración del universo borgeano.' ,pubdate='1944-02-02',isbn='9789500755757', author=jb, language=es)

hacedor = Book(title='El Hacedor', summary='En El hacedor confluyen las simbologías de Oriente y Occidente, el cosmos y las cosmogonías, los siglos, las dinastías, lo universal y lo profundamente local: Heráclito, Homero, Dante con Rosas, Facundo y Juan Muraña. Tal diversidad de temas se corresponde con una multiplicidad de géneros. Así, los relatos, poemas y ensayos de estas páginas terminan configurando uno de los libros más personales del autor; una miscelánea que da cuenta de las preocupaciones que recorren toda la obra borgeana.', pubdate='1960-02-02', isbn='9789500756457', author=jb, language=es)

borra = Book(title='La borra del café', summary='Novela inolvidable, donde el humor y el amor a los seres humanos se convierte en reflejo de nosotros mismos. La borra del café consta de cuarenta y ocho fragmentos y un enigma desarrollado en la imagen misteriosa de una mujer, la presencia de una higuera y la reiteración a lo largo de los años de una hora, las tres y diez. Benedetti rescata, en un espacio de ensueño, las anécdotas que acompañaron a Claudio, el protagonista, durante su niñez en Montevideo.', pubdate='1992-03-03', isbn='9789878317014', author=mb, language=es)

respiro = Book(title='El mundo que respiro', summary='Mario Benedetti asegura que, con suerte y con amores, se aprende; que debe cuidarse ese gajo de corazón que no traiciona; que no queda tiempo para el odio; que no hay que desperdiciar la risa; que hay que afinar el oído cuando se cruza el mar para escuchar ese piano salvado del naufragio.', pubdate='2001-03-03', isbn='9789878317243', author=mb, language=es)

tregua = Book(title='La tregua', summary='La tregua es la obra de Mario Benedetti que ha alcanzado mayor éxito de público. La cotidianidad gris y rutinaria, marcada por la frustración y la ausencia de perspectivas de la clase media urbana, impregna las páginas de esta novela, que, adoptando la forma de un diario personal, relata un breve período de la vida de un empleado viudo, próximo a la jubilación, cuya existencia se divide entre la oficina, la casa, el café y una precaria vida familiar dominada por una difícil relación con unos hijos ya adultos.', pubdate='1960-03-05', isbn='9789877670233', author=mb, language=es)

carrie.save()
mrmercedes.save()
kennedy.save()

carrie.genre.add(horror)
mrmercedes.genre.add(thriller)
kennedy.genre.add(litfic)


roger.save()
orient.save()
witness.save()

roger.genre.add(mistery)
orient.genre.add(mistery)
witness.genre.add(drama)


aleph.save()
ficciones.save()
hacedor.save()

aleph.genre.add(litfic)
ficciones.genre.add(litfic)
hacedor.genre.add(litfic)


borra.save()
respiro.save()
tregua.save()

borra.genre.add(drama)
respiro.genre.add(romance)
tregua.genre.add(drama)



# --------------------------------
a = BookInstance(imprint='Planeta', due_back='2022-07-13',status='o',book=carrie)
a.save()
b = BookInstance(imprint='Planeta', due_back='2022-07-13',status='m',book=carrie)
b.save()
c = BookInstance(imprint='Planeta', status='a',book=carrie)
c.save()
d = BookInstance(imprint='Planeta', status='a',book=carrie)
d.save()

e = BookInstance(imprint='Planeta', due_back='2022-08-13',status='o',book=mrmercedes)
e.save()
f = BookInstance(imprint='Planeta', due_back='2022-09-13',status='m',book=mrmercedes)
f.save()
g = BookInstance(imprint='Planeta', status='a',book=mrmercedes)
g.save()
h = BookInstance(imprint='Planeta', status='a',book=mrmercedes)
h.save()

i = BookInstance(imprint='Sexto Piso', due_back='2022-08-15',status='o',book=kennedy)
i.save()
j = BookInstance(imprint='Sexto Piso', due_back='2022-09-17',status='m',book=kennedy)
j.save()
k = BookInstance(imprint='Sexto Piso', status='a',book=kennedy)
k.save()
l = BookInstance(imprint='Sexto Piso', status='a',book=kennedy)
l.save()

m = BookInstance(imprint='Sexto Piso', due_back='2023-08-15',status='o',book=roger)
m.save()
n = BookInstance(imprint='Sexto Piso', due_back='2022-09-17',status='m',book=roger)
n.save()
o = BookInstance(imprint='Sexto Piso', status='a',book=roger)
o.save()
p = BookInstance(imprint='Sexto Piso', status='a',book=roger)
p.save()

q = BookInstance(imprint='Planeta', due_back='2022-08-13',status='o',book=orient)
q.save()
r = BookInstance(imprint='Planeta', due_back='2022-09-13',status='m',book=orient)
r.save()
s = BookInstance(imprint='Planeta', status='a',book=orient)
s.save()
t = BookInstance(imprint='Planeta', status='a',book=orient)
t.save()

u = BookInstance(imprint='Planeta', status='a',book=witness)
u.save()
v = BookInstance(imprint='Planeta', status='a',book=witness)
v.save()
w = BookInstance(imprint='Planeta', status='a',book=witness)
w.save()

x = BookInstance(imprint='Planeta', due_back='2022-07-13',status='o',book=aleph)
x.save()
y = BookInstance(imprint='Planeta', due_back='2022-07-13',status='m',book=aleph)
y.save()
z = BookInstance(imprint='Planeta', status='a',book=aleph)
z.save()
a1 = BookInstance(imprint='Planeta', status='a',book=aleph)
a1.save()

b1 = BookInstance(imprint='Sexto Piso', due_back='2023-08-15',status='o',book=ficciones)
b1.save()
c1 = BookInstance(imprint='Sexto Piso', due_back='2022-09-17',status='m',book=ficciones)
c1.save()
d1 = BookInstance(imprint='Sexto Piso', status='a',book=ficciones)
d1.save()
e1 = BookInstance(imprint='Sexto Piso', status='a',book=ficciones)
e1.save()

f1 = BookInstance(imprint='Planeta', status='a',book=hacedor)
f1.save()
g1 = BookInstance(imprint='Planeta', status='a',book=hacedor)
g1.save()
h1 = BookInstance(imprint='Planeta', status='a',book=hacedor)
h1.save()

i1 = BookInstance(imprint='Planeta', due_back='2022-08-13',status='r',book=borra)
i1.save()
j1 = BookInstance(imprint='Planeta', due_back='2022-09-13',status='m',book=borra)
j1.save()
k1 = BookInstance(imprint='Planeta', status='a',book=borra)
k1.save()
l1 = BookInstance(imprint='Planeta', status='a',book=borra)
l1.save()

m1 = BookInstance(imprint='Planeta', due_back='2022-08-13',status='r',book=borra)
m1.save()
n1 = BookInstance(imprint='Planeta', due_back='2022-09-13',status='m',book=borra)
n1.save()
o1 = BookInstance(imprint='Planeta', status='a',book=borra)
o1.save()
p1 = BookInstance(imprint='Planeta', status='a',book=borra)
p1.save()

q1 = BookInstance(imprint='Planeta', due_back='2022-08-13',status='m',book=borra)
q1.save()
r1 = BookInstance(imprint='Planeta', due_back='2022-09-13',status='o',book=borra)
r1.save()
s1 = BookInstance(imprint='Planeta', status='a',book=borra)
s1.save()
t1 = BookInstance(imprint='Planeta', status='a',book=borra)
t1.save()













