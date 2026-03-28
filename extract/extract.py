import requests  # API 호출 라이브러리

def extract_deals():
    """
    CheapShark API에서 할인 게임 목록을 가져오는 함수
    """

    # 요청할 API 엔드포인트 URL -> 1.0은 API 버전 정보
    url = "https://www.cheapshark.com/api/1.0/deals"

    # 요청 조건 (API 문서에 나와있는 파라미터들)
    # URL에 직접 붙이는 것과 같음 -> 쿼리 파라미터로 
    # ?upperPrice=30&pageSize=20&sortBy=Deal%20Rating
    params = { 
        "upperPrice": 30,    # 30달러 이하 게임만
        "pageSize": 20,      # 20개만 가져오기
        "sortBy": "DealRating",  # 할인율 높은 순 정렬
        "storeID": "1" # Steam만 필터링
    } 
    # 파라미터및 API에 대한 자세한 내용은 CheapShark API URL으로 확인가능
    # https://apidocs.cheapshark.com 

    print("CheapShark API 호출 중...")

    # GET 요청 보내기
    # params를 따로 넘기면 requests가 URL에 자동으로 붙여줌
    response = requests.get(url, params=params)

    # 응답 상태코드 확인
    # 200 = 성공, 404 = 못찾음, 500 = 서버에러
    print(f"응답 상태코드: {response.status_code}")

    # JSON 형식으로 변환
    # response.json() = 텍스트로 된 JSON을 Python 리스트/딕셔너리로 변환
    data = response.json()

    print(f"가져온 게임 수: {len(data)}개")

    return data


# 이 파일을 직접 실행할 때만 아래 코드 실행
# (다른 파일에서 import할 때는 실행 안 됨)
# transform.py 에서 extract_deals() 함수 사용할 것이므로 제한 걸어둠.
if __name__ == "__main__":
# → "이 파일 단독으로 테스트할 때만 실행해"
# → "다른 파일에서 import할 때는 함수만 빌려줄게"

    deals = extract_deals()

    # 첫 번째 게임 데이터 구조 확인
    # 어떤 필드들이 있는지 눈으로 보기 위해
    print("\n첫 번째 게임 데이터 구조:")
    print(deals[0])