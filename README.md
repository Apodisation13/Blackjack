### На данный момент реализовано следующее:

1) Вы берете за стол деньги (ввести можно положительное целое число, отрицательное и не-число нельзя)
2) Игра продолжается пока вы не потратили всё до 0.
3) Каждый раунд начинается со ставки
4) Ставка не может больше чем есть у вас, так же должна быть целым положительным числом

# Игра:
Карты 2-10 - соответствуют номиналу.
Тузы - или 1 или 11 очков.
Картинки - все по 10. 
Надо набрать очков больше чем дилер, но не более 21. Более 21 - сразу проигрыш.

# Описание процесса:
1) Раздали две случайные карты дилеру и игроку. У дилера видна только одна карта.
2. Стартовая проверка:
  * Если блэкджек у обоих (21 очко), ничья, деньги вернулись игроку.
  * Если блэкджек у дилера, сразу проигрыш ставки.
  * Если блэкджек у игрока, выигрыш двойной ставки (то есть например, поставил 100, выиграл эти 100 назад и ещё 200)
 3. Если блэджека ни у кого нет, можно ввести double, hit или stand
