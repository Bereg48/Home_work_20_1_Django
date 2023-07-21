# Условия домашки
Чтобы справиться с заданиями, проверьте, что вы изучили весь материал урока:

Посмотрели видео и прочитали конспект.
Проанализировали эталонный код в разделе «Задачи».
Разобрали решения задач по скринкастам в разделе «Подготовка к практике».
 
Контекст: зачем решать подобные задачи
Получение данных из БД по запросу пользователя/клиента обязует разработчика описывать отображение этих данных. Если делается обычное веб-приложение, то отображение необходимо выводить в HTML-страницы. Для этого проводится работа над шаблонами.

Теперь придадим динамику нашему приложению, а также сделаем страницы более привлекательными.

Критерий выполнения заданий
Результат задания залейте в GitHub и сдайте в виде ссылки на репозиторий.
# Задание 1
Создайте новый контроллер и шаблон, которые будут отвечать за отображение карточки товара. На странице важно выводить всю информацию о товаре.

Для создания шаблонов используйте UI kit Bootstrap. При возникновении проблем возьмите за основу данный шаблон.

# Задание 2
В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек отображаемое описание обрежьте после первых выведенных 100 символов.

# Задание 3
Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый) шаблон и также подшаблон с главным меню.

При необходимости можно выделить больше общих шаблонов.

# Задание 4
Для выводимого изображения на странице реализуйте шаблонный фильтр, который преобразует переданный путь в полный путь для доступа к медиафайлу:

<!-- Исходный вариант --> 
<img src="/media/{{ object.image }}" />
<!-- Итоговый вариант -->
<img src="{{ object.image|mediapath }}" />

Реализуйте описанный функционал с помощью шаблонного тега:

<!-- Исходный вариант -->
<img src="/media/{{ object.image }}" />
<!-- Итоговый вариант -->
<img src="{% mediapath object.image %}" />

# * Дополнительное задание
Добавьте функционал создания продукта через внешний интерфейс, не используя стандартную админку.
Реализуйте постраничный вывод списка продуктов.