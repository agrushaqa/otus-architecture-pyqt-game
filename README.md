pyuic5 table.ui -o tablewidgetex.py -x
- генерация файла на основе PyQt5 UI code generator

# run kafka (ubuntu)
https://kafka.apache.org/quickstart
 Run the following commands in order to start all services in the correct order:

## Start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties

Open another terminal session and run:

## Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties

Once all services have successfully launched, you will have a basic Kafka environment running and ready to use. 

# Запуск

Запуск игры производится через запуск скрипта 
game_sea_fight.py

# Описание
 Этот проект совмещает сервер написанный для изучения SOLID принципов
 и игру морской бой.
 
Идея в том, что мы запускаем kafka
запускаем сервер.
сервер генерирует положения кораблей 
передаёт их клиенту
клиент на PyQt их отображает.

Сейчас эти эти части не взаимосвязаны.
Поскольку этот проект учебный его доработку я пока откладываю на неопределённое время

Описание работы сервера смотри здесь
https://github.com/agrushaqa/-otus-architecture-kafka-exchange-messages/pull/1/files