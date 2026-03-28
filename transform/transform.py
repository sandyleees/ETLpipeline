import pandas as pd                    # 데이터 정제 라이브러리
from datetime import datetime          # 날짜 변환용

import sys                             # 파일 경로 설정용 - python 실행 환경 제어
import os                              # 파일/폴더 경로 처리 

# 다른 폴더의 파일을 import하기 위한 경로 설정
# extract 폴더가 transform 폴더와 다른 위치에 있어서 필요함
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# __file__ = 지금 이 파일의 경로 (어느 컴퓨터든 자동으로 찾음)
# 절대경로로 써도 되지만 그러면 내 컴퓨터(sandy)에서만 작동하게 되므로 비추천함
# sys.path.append('/home/sandy/steam-etl') 이게 절대경로로 import 찾을 폴더 정하는 코드

from extract.extract import extract_deals  # extract.py의 함수 가져오기
# 상위폴더 steam-etl -> 안에 있는 extract폴더 -> 안에 있는 extract.py (extract.extract)
# extract.py에 있는 extract_deal 함수 가져오기 -- 의존성 O 


def transform_deals(raw_data):
    """
    raw_data: extract_deals()가 반환한 리스트 (딕셔너리 20개)
    → pandas DataFrame으로 변환 후 정제해서 반환
    """

    # 리스트를 pandas DataFrame으로 변환 
    # (리스트안에 딕셔너리 들어간 [{게임1},{게임2}, ... ]보다 표형태가 보기 좋으니까)
    # DataFrame = 표 형태의 데이터 구조 (엑셀 시트랑 비슷)
    df = pd.DataFrame(raw_data)
    # DataFrame 구조 : 딕셔너리 key = 컬럼 / value = 각 행의 값 됨.

    print(f"정제 전 컬럼 목록: {list(df.columns)}")
    print(f"정제 전 행 수: {len(df)}")

    # ① 필요한 컬럼만 추리기 -> 컬럼부터 추리고 추려진 놈들을 정제하는게 효율적
    df = df[[
        'title',            # 게임 이름
        'salePrice',        # 할인가
        'normalPrice',      # 원가
        'savings',          # 할인율
        'metacriticScore',  # 메타크리틱 점수
        'steamRatingText',  # 스팀 평가
        'dealRating',       # 딜 평점
        'releaseDate'       # 출시일
    ]]

    # ② 데이터 타입 변환
    # 문자열로 된 숫자들을 실제 숫자로 변환
    # WSL에 python3 extract/extract.py 으로 실행시켜봤을때 모든 숫자형이 JSON 형식에 따라
    # 문자형으로 저장되어있었음을 확인가능하므로 형변환 필요
    df['salePrice']      = df['salePrice'].astype(float)      # '2.99' → 2.99
    df['normalPrice']    = df['normalPrice'].astype(float)    # '29.99' → 29.99
    df['savings']        = df['savings'].astype(float)        # '90.030010' → 90.03
    df['metacriticScore']= df['metacriticScore'].astype(int)  # '90' → 90
    df['dealRating']     = df['dealRating'].astype(float)     # '9.2' → 9.2

    # ③ 소수점 정리
    # 90.030010 → 90.0 (소수점 첫째자리까지만)
    df['savings'] = df['savings'].round(1)

    # ④ 타임스탬프 → 날짜 변환
    # 1285027200 → '2010-09-21'
    # 타임스탬프 = 1970년 1월 1일부터 지금까지의 초(seconds)
    df['releaseDate'] = df['releaseDate'].apply(
        lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d')
    )

    print(f"\n정제 후 컬럼 목록: {list(df.columns)}")
    print(f"정제 후 행 수: {len(df)}")

    return df # 데이터프레임 자체를 반환 

# 이 파일을 직접 실행할 때만 아래 코드 실행
# (다른 파일에서 import할 때는 실행 안 됨)
# load.py에서 transform_deals() import해서 사용할 것이므로 
# 테스트 코드 실행 되지 않게 제한 걸어둠.
if __name__ == "__main__":
# → "이 파일 단독으로 테스트할 때만 실행해"
# → "다른 파일에서 import할 때는 함수만 빌려줄게"

    # 1. 데이터 가져오기
    raw_data = extract_deals()

    # 2. 정제하기
    df = transform_deals(raw_data)

    # 3. 결과 확인
    print("\n정제된 데이터 미리보기:")
    print(df.head())   # 상위 5개 행만 출력

    print("\n데이터 타입 확인:")
    print(df.dtypes)   # 각 컬럼의 타입 확인


