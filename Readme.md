# Условия домашки
Чтобы справиться с заданиями, проверьте, что вы изучили весь материал урока:

Посмотрели видео и прочитали конспект.
Проанализировали эталонный код в разделе «Задачи».
Разобрали решения задач по скринкастам в разделе «Подготовка к практике».
 
Контекст: зачем решать подобные задачи
‍Написание контроллеров на основе функций — быстрый и легкий способ начать работу. Но есть способ еще быстрее и надежнее — писать контроллеры на основе классов.

Настало время провести рефакторинг веб-приложения и добавить функциональность для улучшения SEO сайта путем создания раздела с блогом.

Критерий выполнения задания
Результат задания залили в GitHub и сдали в виде ссылки на репозиторий.
### Задание 1
Продолжаем работать с проектом из предыдущего домашнего задания. Переведите имеющиеся контроллеры с FBV на CBV.

### Задание 2
Создайте новую модель блоговой записи со следующими полями:

заголовок,
slug (реализовать через CharField),
содержимое,
превью (изображение),
дата создания,
признак публикации,
количество просмотров.
Для работы с блогом реализуйте CRUD для новой модели.

Slug — человекопонятный URL, представляет собой набор символов, которые можно прочитать как связные слова или предложения в адресной строке, служит уникальным идентификатором записи в рамках одной модели и состоит из безопасных для обработки запроса символов:

0-9,
a-z(обычно в нижнем регистре),
символ -.
### Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

при открытии отдельной статьи увеличивать счетчик просмотров;
выводить в список статей только те, которые имеют положительный признак публикации;
при создании динамически формировать slug name для заголовка;
после успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.
## * Дополнительное задание
Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.

Примечание: для отправки писем рекомендуем использовать почтовый сервис Яндекс.

Дополнительное задание, помеченное звездочкой, выполнять желательно, но не обязательно.