# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

from re import sub
text = 'Когда повтор — ошибка. Однокоренные слова бросаются в глаза, и читатель неосознанно пытается установить между ними связь, хотя никакой связи, скорее всего, нет. Прочитайте этот пример:Вооружённые силы эльфов держались из последних сил, гномов было больше, и они сильно обозлились на своих бывших союзников. Очень много разных «сил», да? Это к тому же ещё и неблагозвучно. А кроме того, обилие лексических повторов в тексте часто свидетельствует о его однообразности и о скудном словарном запасе автора. Джо был фермером. Он был уже немолод и беден, но у него был трактор, который был куплен, когда Джо был помоложе и побогаче. Есть и ещё одна причина, почему вам следует избегать лексических повторов. Современные издательства строго относятся к этой ошибке и требуют от литературных редакторов по максимуму вычищать её из текста. По своему опыту скажу, что на лексические повторы приходится от 20 до 50% всех правок, которые делает редактор. Иногда, чтобы устранить лексический повтор, нужно полностью поменять структуру предложения. Посмотрите на пример с Джо и его трактором: насколько сильно вам придётся переписать этот фрагмент, чтобы оставить там всего одно слово «был»? Я думаю, в результате у вас получится совсем другой текст. Так что если вы не хотите, чтобы ваши собственные творения становились неузнаваемы после редактуры, позаботьтесь в том числе и о лексических повторах. Когда повтор — не ошибка Если бы с повторами всё было так просто, мне бы не пришлось писать эту статью. На самом деле всё несколько сложнее. Бывает, что два однокоренных слова по соседству не считаются ошибкой, и таких случаев немало. Давайте их разберём. Во-первых, как я уже сказал, повтор может быть художественным приёмом, если его используют сознательно и умело. Со стилистикой — как с пряностями: корицу можно класть в суп, а перец — в варенье, если вы знаете, в каких комбинациях, в каком количестве и т.д. Если же вы сыплете наобум, просто потому, что «ну ведь можно же», — тогда вы испортите блюдо, только и всего. Ну или испортите текст. На повторе однокоренных слов строятся всевозможные варианты синтаксического параллелизма, в частности анафора и эпифора. Повтор также может использоваться просто для того, чтобы что-то подчеркнуть, выделить (как, например, само слово «повтор» в этих двух предложениях). Вот вам для наглядности ещё несколько примеров: А за окном шёл дождь. За грязным зарешечённым окном всё шёл и шёл дождь, и Хорхе уже был близок к тому, чтобы плюнуть, взять рюкзак и ехать прямо сейчас. В поисках ключей я перерыл всю квартиру. Нашёл: сто рублей (старые, советские), кошку, трёхметровые шнурки в упаковке, капли от икоты, велосипедный насос, кошку, подозрительный флакончик с парфюмом и кошку. Ключей нигде не было. Если хотите чего-то добиться — прямо сейчас беритесь и делайте. Если не хотите — можете просто слушать, можете идти. А ваши отговорки мне не интересны. Не кружись, большая птица, / Не кружись над головою, / Не видать тебе добычи — / Всю добычу съем я сам. Москва — город. И Ленинград — город. Мурманск — тоже город, кто бы там что ни говорил. А ваш Горнопрокопьевск... Вы меня извините, был я в том Горнопрокопьевске. Не город, а так, две улицы и сельпо.'

top_words = {}
words = sub(r'[^\w\s]', '', text).lower().split()
for i in words:
    top_words.setdefault(i,0)
    top_words[i] += 1

top_words=dict(sorted(top_words.items(), key=lambda x: x[1], reverse=True)[:10])

for place, word in enumerate(top_words.items()):
    print(f'{place+1}. {word[1]} раз(а) - "{word[0].capitalize()}"')