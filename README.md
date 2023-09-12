<details>
<summary>Titanic From Disaster</summary>

#### DDA
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| survival | Survival | 0 = No, 1 = Yes | 명목형, 데이터 분석 후 결정함 |
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 순서형, 데이터 분석 후 결정함. 등급에 따른 나열가능 |
| sex | Sex | | 명목형, 분석 후 결정함. |
| Age | Age in years | | 이산형, 분석 후 결정, 누락사항있어 정확한 통계를 확인 하는데 부적합하다고 판단함.  |
| sibsp | # of siblings / spouses aboard the Titanic | | 명목형, 분석 후 결정함. |
| parch | # of parents / children aboard the Titanic | | 명목형, 분석 후 결정함. |
| ticket | Ticket number | | 순서형, sibsp, parch, pclass, fare와 함께 분석 후 확인 |
| fare | Passenger fare | | 이산형, 분석 후 결정함. |
| cabin | Cabin number | | 명목형, 분석 후 결정함.|
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S =Southampton | 명목형, 분석 후 결정함. |
| PassengerId | PassengerId |  | 명목형, 분석 후 결정, 고유값을 가지고 있어 활용도가 떨어진다고 생각함. | 

</details>

<details>
<summary>Type Of Contract Channel</summary>
    
#### DDA
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |    
| type_of_contract | type_of_contract |  | 순서형, 분석 후 확인  |
| type_of_contract2 | type_of_contract(세부사항) |  | 순서형, type_of_contract와 같이 분석하여 유형별 나열.  |
| channel | channel(접근경로) |  | 순서형, 분석 후 제품 접근성 확인 |
| datetime | datetime |  | 연속형, 분석 후 날짜별 판매량 확인 |
| Term | Term(계약주기) |  | 순서형, age와 같이 분석하여 나이대별 구매력 확인 가능. |
| payment_type | payment_type(지불형태) |  | 순서형, 분석 후 확인 |
| product | product |  | 순서형, product별 판매량 확인. |
| amount | amount |  | 순서형, amount에 따른 판매량 확인. |
| state | state |  | 순서형, 제품의 장기 사용 가능 확인 |
| overdue_count | overdue_count |  | 순서형, overdue와 같이 분석 후 확인 |
| overdue | overdue |  | 이산형, 분석 후 연체율 확인가능 |    
| credit rating | credit rating |  | 이산형, 분석 후 확인 |
| bank | bank |  | 순서형, 은행별 전략설정 가능 |
| cancellation | cancellation |  | 순서형, 제품의 장기 사용 가능 확인 |
| age | age |  | 순서형, 나이때 별 구매력을 확인 가능하나 분석 중 이상수치확인. |
| Mileage | Mileage |  | 이산형, 분석 후 확인 |

</details>
