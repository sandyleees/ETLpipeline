## 1. 프로젝트 개요

steam 게임 할인 데이터 20개를 CheapShark API로 호출하고, 필요한 정보만 정제해서, CSV 파일로 저장하는 ETL 파이프라인을 만든 후 GIThub에 올린다.

## 2. 해당 프로젝트의 목표

- git을 통해 완성된 프로젝트를 올리는 과정을 경험한다. 이를 통해 git의 기능을 학습한다.
- ETL 과정의 전체적인 흐름을 학습한다. 
(이 과정에서 파일 간 함수를 import하며 의존성 발생했으나, 아직 airflow까지 생각하지 않는 제일 간단한 ETL 기초 파이프라인 프로젝트를 다루고자 하므로 우선 프로젝트 완성에 집중했다)
- 해당 프로젝트를 수행하는 과정에서 나오는 개념에 대해 학습한다.
    - 네트워크 / API : IP, DNS, URL 구조, API, 엔드포인트, HTTP 메서드, 상태코드, 데이터 형식
    - Python: 모듈/라이브러리/프레임워크, import 방식, 가상환경, `if __name__`, lambda
    - pandas: DataFrame 구조, 주요 메서드
    - Linux: 폴더 구조, 주요 명령어

## 3. 최종 폴더 구조

```bash
steam-etl/
├── .git/                          ← Git 이력 저장소 (자동 생성)
│
├── venv/                          ← 가상환경 (GitHub에 안 올라감)
│   ├── bin/ # 가상환경 전용 실행파일
│   │   ├── activate               ← 가상환경 켜는 스위치
│   │   ├── python3                ← 가상환경 전용 Python
│   │   └── pip                    ← 가상환경 전용 pip
│   └── lib/ # 가상환경 전용 라이브러리 
│       └── site-packages/
│           ├── requests/          ← pip install로 설치된 라이브러리
│           └── pandas/            ← pip install로 설치된 라이브러리 
│
├── extract/
│   └── extract.py                 ← CheapShark API 호출 (Extract)
│
├── transform/
│   └── transform.py               ← 데이터 정제 (Transform)
│
├── load/
│   └── load.py                    ← CSV 저장 (Load)
│
├── data/
│   └── steam_deals.csv            ← 최종 결과물
│
└── .gitignore                     ← Git 제외 목록 (venv/, __pycache__/, .git/)
```

## 4. 각 파일 코드 흐름

1.  [extract.py](http://extract.py) : CheapShark API에서 /deal 엔드포인트에 GET 요청을 보내 steam(storeID=1) 게임 할인 목록 20개를 가져온다 (extract_deals() 함수)
2. [transform.py](http://transform.py) : extract_deals() 의 결과를 pandas DataFrame 으로 변환하고, 필요한 8개의 컬럼만 걸러낸 뒤 type 변환과 날짜 변환을 수행한다 (transform_deals() 함수)
3. [load.py](http://load.py) : transfrom_deals() 의 결과 DataFrame 을 data/steam_deals.csv 파일로 저장한다. (load_to_csv() 함수)

> 참고 : 약 10시간 소요 = 프로젝트 수행 + 회고록 및 학습 개념 정리 (구체적인 내용은 Notion에 작성함)
