# minesweeper

Реализация консольного варианта игры Сапёр.

Игра запускается в консоле, взаимодействие с пользователем происходит с помощью консольных вводов/выводов.

Размеры поля и количество бомб задаётся с клавиатуры.

Взаимодействие с пользователем происходит посредством командной строки, состояние поля после каждого шага отображается в консоли, пользователь делает ход с помощью команд троек ﻿[X,Y,Action]﻿, где ﻿X﻿ и ﻿Y﻿ — координаты клетки на поле, а Action – действие, которое необходимо совершить: Flag — установить флажок на соответвующую клетку, пометив её как предположительно содержащую бомбу; Open – раскрыть содержимое клетки.