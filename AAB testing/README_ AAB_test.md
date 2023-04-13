      date: 03 2023
      status: finished 
      Elena Skripnichenko
      TG @Skrilen
      в рамках курса SkillFactory Data science pro
__________
# A/A/B test
В исследовании данные одного маркетплейса. Данные о кликах, просмотрах и покупках сегментированы для тестирования по схеме ААВ.

Желание маркет-плейса - выяснить, оказывает влияние алгоритм, примененный к B-сегменту пользователей. Для оценки маркетплейс использует метрики: 
 - CTR, 
 - PR, 
 - GMV. 

Задача, решаемая в проекте - выяснить, корректно ли проведено сегментирование для ААВ теста и работает ли алгоритм, примененный к В-сегменту. 

Содержание:

1  Task setting
1.1  Evaluatuion criteria
2  Imports & load
3  EDA
3.1  Samples balance
3.2  Samples intersection
3.3  Actions logic
3.3.1  Duplicates check
3.4  Distribution of actions in samples
4  Metrics
4.1  Aggregated counters
4.2  CTR
4.3  PR
4.4  GMV
4.5  metrics per user
5  Tests
5.1  Shapiro-Wilk test
5.1.1  CTR
5.1.2  PR
5.1.3  GMV
5.2  A to C (AA) metrics comparision
5.2.1  CTR
5.2.2  PR
5.2.3  GMV
5.3  C and A to B (AB) metrics comparision
5.3.1  CTR
5.3.2  PR
5.3.3  GMV
6  Conclusions