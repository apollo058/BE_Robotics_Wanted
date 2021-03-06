![image](https://user-images.githubusercontent.com/88444944/166816713-e28a22d2-b256-4429-a582-4c14867874fd.png)


# Wanted team_B #2베어로보틱스 기업과제  

주어진 데이터 셋을 요구사항 대로 서빙하기 위한 관계형 데이터베이스 테이블을 설계하고,\
주어진 기능을 제공하는 REST API 서버를 개발합니다.


## Team process:

### Team 분업  ###  
  
  #
|성명|업무|비고|
|------|---|---|
|최승리|점포명없이 조회가능한 API, 프랜차이즈의 메뉴기준 집계 API작성 및 테스트코드/ 기획|팀장⭐ |
|하정현|방문인원, 결제수단에 따른 통계 집계 API구현 및 테스트코드 |.|
|남기윤|결제기록(POSLOG)DB적재 API, 필수적인 기본 검색데이터 집계API 구현 및 테스트코드|.|\

### 중점 point

1. RESTFUL 한 API 구현 (Endpoint URL, HTTP Method , JSON Response)
2. 효율적인 쿼리 구현
3. 요구사항 뿐 아니라 다른 기능이 함게 있는 서버라고 가정하고 폴더, 파일, 코드 스트럭처를 설계

## Directory Info.

```
├─menu                      -menu add 디렉토리
│  ├─migrations
│  │  └─__pycache__
│  └─__pycache__
├─point_of_sale             -프로젝트 main configure
│  ├─settings
│  │  └─__pycache__
│  └─__pycache__
├─pos_log                   -poslog CRUD 및 검색 add 디렉토리
│  ├─migrations    
│  │  └─__pycache__
│  ├─tests                  -unit test 디렉토리
│  │  └─__pycache__
│  └─__pycache__
└─restaurants               -restaurant add 디렉토리
    ├─migrations
    │  └─__pycache__
    └─__pycache__
```
## 실행 안내

```
#앱 실행
$python manage.py runserver --settings=point_of_sale.settings.local
#테스트 실행
$python manage.py test --settings=point_of_sale.settings.local 
```

## 베어로보틱스 project 요구사항 분석
\
모 프랜차이즈(e.g. BR company) 경영진은 본인들의 사업에 관한 **insight** 를 얻고자 합니다.

* 각 점포의 POS에서 결제된 데이터를 RDB로 저장해주세요.
* 프랜차이즈 매니저는 여러 검색조건과 정렬조건을 통해 집계된 결과를 원합니다.
* 점포들의 데이터가 다음과 같은 CSV파일로 제공됩니다.

```
restraunt_id,restaurant_name,group,city,address
21,비비고,1,서울,서초구 서초동
22,비비고,1,서울,관악구 신림동
31,빕스버거,2,서울,강남구 개포동
32,빕스버거,2,서울,관악구 신림동
```

* POS데이터의 예시는 다음과 같습니다.

```
Payment: CARD, CASH, PHONE, BITCOIN
Note that id is a unique id generated in RDB automatically. Data payload
from POS does not have id.
```
* 기대하는 결과
  * 주어진 데이터를 RDB에 migration 할것.
    - Restaurant
    - POS data
  * (선택사항) 필요하다면 다른 데이터 model을 정의해도 좋습니다.(단, ORM을 통한 RDB테이블일것)
  * 필수구현사항
    1. 점포POS로부터 데이터를 가져와 저장하는 REST API
    2. 점포별 KPI(핵심성과지표)를 집계하는 REST API
  * 선택구현사항
    1. 결제수단에 따른 점포별 KPI를 집계하는 REST API
    2. 고객 인원수에 따른 점포별 KPI를 집계하는 REST API
  * 구현시 가산점
    1. 유닛테스트 코드
    2. Swagger UI
    3. 점포명에 상관없이 총계를 집계하는 REST API
    4. 기한에 여유가 있다면, 판매한 메뉴정보를 함께 저장하고, 판매한 메뉴를 기준으로 데이터를 집계하는 기능을 추가해주세요.

    
    
## API info.

### 점포 POS 결제기록 API
* 점포 ID, 가격, 인원, 결제수단, **판매된 메뉴의 리스트** 를 DB에 저장합니다.(url:"api/pos" method:POST) 전체조회:(url:"api/pos" method:GET)
* RUD 기능 = api/pos<int:pos_id>  read:GET, update:PATCH, delete: DELETE
```
#input eg.
{
    "restaurant" : 21,
    "price" : 5000,
    "number_of_party" : 1,
    "payment" : "CASH",
    "menu_list" : [
        {
            "menu":2,
            "count":1
        },
        {
            "menu":1,
            "count":3
        }
    ]
    }
```

### 점포별 KPI 집계 API
* 기간(필수), timesize(필수, 집계기준단위), 가격범위, 인원범위, 그룹id를 입력받아 해당하는 통계를 출력합니다.(method:GET)
```
#input eg.
/api/pos?start-time=2022-02-23&end-time=2022-02-26&timesize=day&min-price=100&max-price=50000&group=1&min-party=1&max-party=4
```
* 기본 방식에서 결제방식 파라미터를 추가로 받아 해당하는 통계를 출력합니다.(method:GET)
```
#input eg.
/api/pos?start-time=2022-02-23&end-time=2022-02-26&timesize=day&min-price=100&max-price=50000&group=1&min-party=1&max-party=4&payment=all
```
* 기본 방식에서 인원 파라미터를 추가로 받아 해당하는 통계를 출력합니다.(method:GET)
```
#input eg.
/api/pos?start-time=2022-02-23&end-time=2022-02-26&timesize=day&min-price=100&max-price=50000&group=1&min-party=1&max-party=4&number-of-party=2
```
* 기본 방식에서 **주소**를 추가로 받아 해당하는 통계를 출력합니다.(method:GET)
```
#input eg.
/api/pos?start-time=2022-02-23&end-time=2022-02-26&timesize=day&min-price=100&max-price=50000&group=1&min-party=1&max-party=4&adress="성북구"
```
### 메뉴별 집계 API

* 메뉴데이터 CRUD (url:"api/menu")
```
#input eg.
{
    "menu_name" : "갈비찜",
    "price" : 5000,
    "group" : 1,
}
```

* 기간, 메뉴리스트, 정렬기준을 인자로 받아 메뉴별 판매를 비교합니다. (url:"api/menu/sales")
```
#input eg.
/api/menu/sales?start-time=2022-02-23&end-time=2022-02-26&menu_list="갈비찜,싸이버거"
```

### 점포데이터 CRUD

* 점포정보를 CRUD합니다.
* 점포 정보를 추가합니다. (url:"api/restaurants/create", method:POST)
* 점포 정보를 가져옵니다. (url: "api/restaurants/<점포 ID>", method:GET)
* 점포 정보를 수정합니다. (url: "api/restaurants/<점포 ID>", method:PATCH)
* 점포 정보를 제거합니다. (url: "api/restaurants/<점포 ID>", method:DELETE)
```
#input.eg
{
  "group": 1,
  "restaurant_name": "점포 1"
  "city": "서울",
  "address": "남구 XXX로 125번"
}
```


## DB info.

![image](https://user-images.githubusercontent.com/88444944/166816865-ad38ade0-7449-4f25-8588-36b02b95bdd6.png)

