import pandas as pd 
import os 
import sys 

# 상위 폴더를 import 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from transform.transform import transform_deals  
from extract.extract import extract_deals 

 
def load_to_csv(df):
    """
    정제된 DataFrame을 CSV 파일로 저장하는 함수
    """

    # 저장할 폴더 경로
    # os.path.dirname(__file__) = load 폴더
    # 상위 폴더(steam-etl)에 data 폴더 만들어서 저장
    output_dir = os.path.join(   
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), #'/home/sandy/steam-etl'
        'data'
    ) # 경로 join하면 /home/sandy/steam-etl + data = /home/sandy/steam-etl/data 경로 됨

    # data 폴더가 없으면 자동으로 만들기 
    os.makedirs(output_dir, exist_ok=True)
    # exist_ok=True는 폴더 이미 있어도 에러 나지 않도록 하기 위해.  
    # 폴더 없음 → 생성 ✅
    # 폴더 있음 → 그냥 넘어감 ✅ # exist_ok=False (기본값)이면 폴더 있음 → 에러 ❌ FileExistsError

    # 저장할 파일 전체 경로 -- steam_deals.csv 라는 이름으로 CSV 저장 예정 
    output_path = os.path.join(output_dir, 'steam_deals.csv')  

    # DataFrame을 CSV로 저장
    # index=False → 행 번호(0,1,2...)는 저장 안 함
    df.to_csv(output_path, index=False, encoding='utf-8-sig')     
    # encoding='utf-8-sig' → 엑셀에서 열 때 한글 깨짐 방지

    print(f"저장 완료: {output_path}")
    print(f"저장된 행 수: {len(df)}개")

if __name__ == "__main__":

    # 1. 데이터 가져오기
    raw_data = extract_deals()

    # 2. 정제하기
    df = transform_deals(raw_data)

    # 3. CSV로 저장
    load_to_csv(df)