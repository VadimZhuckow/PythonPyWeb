import os
import time

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from rest_framework import serializers
    from apps.db_train_alternative.models import Author


    # Сериализатор
    class AuthorSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(max_length=200)
        email = serializers.EmailField()

        def create(self, validated_data):
            return Author.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Обновить и вернуть существующий объект Author на основе предоставленных проверенных данных.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


    # _____________________________________________________________________________________
    # Сериализация (Модель трансформируется в словарь который потом станет Json объектом)

    # Получение объекта Author из базы данных
    author = Author.objects.get(pk=1)  # Пример: получение объекта с первичным ключом равным 1

    # Создание сериализатора и сериализация объекта Author
    serializer = AuthorSerializer(author)

    # Получение сериализованных данных в формате JSON (словарь)
    serialized_data = serializer.data

    # Вывод сериализованных данных
    print(serialized_data)
    # _____________________________________________________________________________________

    # Десериализация (Json объект (словарь) трансформируется в Модель и сохраняется в БД)

    json_data = {'name': 'Jo21h1n', 'email': 'jo2h21n@example'}  # с ошибкой в поле email

    serializer = AuthorSerializer(data=json_data)
    # Проверка валидности данных
    if serializer.is_valid():
        # Создание или обновление объекта Author
        serializer.save()
    else:
        # Вывод информации об ошибках валидации
        print("Ошибка")
        print(serializer.errors)

    json_data = {'name': 'Joh21n', 'email': 'j212ohn@example.com'}

    serializer = AuthorSerializer(data=json_data)
    # Проверка валидности данных
    if serializer.is_valid():
        print("Данные для записи")
        print(serializer.validated_data)
        # Создание или обновление объекта Author
        serializer.save()
    else:
        # Вывод информации об ошибках валидации
        print(serializer.errors)
