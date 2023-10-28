# S3
## HW of course MLOps by SBT

Представьте, что в инфраструктуру вашей компании завезли новый облачный сервис хранения и версионирования данных, внутри вашего уютного ДЦ он находится на другой физической машине (не на той, куда вы обычно ssh-итесь или не на той, где у вас запускаются таски) и теперь чтобы организовать обучение с сохранением чекпоинтов вам нужно складывать их не локально диск, а в бакет. Задание: поднимите Docker Compose с MinIO, сконфигурируйте бакет, продемонстрируйте, что умеете сохранять чекпоинт модели (state_dict + hyperparameters + optimizers state) в бакет, а так же, что умеете восстанавливать обучение из чекпоинта в бакете.


