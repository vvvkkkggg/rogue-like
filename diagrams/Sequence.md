Sequence diagram иллюстрирует взаимодействие между пользователем (Player) и различными компонентами системы при выполнении основных действий в игре. Вот описание взаимодействий:

## Start game (Начало игры)

### 1
* Пользователь отправляет команду "Start game" в контроллер.
* Контроллер перенаправляет команду "Start game" в модель.
* Модель обновляет поле игры и отправляет команду "Update field" в представление.
* Представление отображает обновленное поле для пользователя.
* Exit (Выход)

### 2
* Пользователь отправляет команду "Exit" в контроллер.
* Контроллер перенаправляет команду "Exit" в модель.
* Модель очищает поле игры и отправляет команду "Clean field" в представление.
* Представление очищает отображаемое поле.
* Make move (Сделать ход)

### 3
* Пользователь отправляет команду "Make move" в контроллер.
* Контроллер перенаправляет команду "Change field" в модель.
* Модель обновляет поле в соответствии с ходом пользователя и отправляет команду "Update field" в представление.
* Представление отображает обновленное поле для пользователя.
## Компоненты диаграммы:
* Player (Пользователь): Тот, кто взаимодействует с игрой.
* Player (Класс игрока): Представляет пользователя в системе.
* Controller (Контроллер): Управляет процессами игры и взаимодействием между моделью и представлением.
* Model (Модель): Логическая часть игры, ответственная за состояние и правила игры.
* View (Представление): Отображает состояние игры пользователю.