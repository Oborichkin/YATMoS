Еще немного подумав про импорт JUnit пришел к выводу что Case и CaseResult не тождественны
конкретному тесту (например в pytest) и конкретному отчету (junit+логи+всяческие вложения).

Один и тот же Case может быть проверен разными тестами и разными способами. Так что стоит выделить
отдельную сущность Implementation и Report.

Implementation - конркетное воплощение тестового кейса, это может быть как и код, так и ручной тест (manual).

Report - результат конкретного выполнения Implementation. Для pytest это например лог теста и прочие вложения.

> Стоит подумать отдельно как в эту схему будут встраиваться manual-тесты. Будут ли они полностью копировать
> Case?

> Также стоит подумать насчет необходимости Step'ов как детей именно Case'ов. Может быть сделать их детьми
> Implementation? Может вообще пока их не учитывать?