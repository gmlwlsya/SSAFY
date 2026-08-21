
# 수정할 변수명,개발자 도구(F12)에서 가져올 위치,수정 방법
# BASE_URL & PARAMS,General → Request URL,파일명 끝 숫자(0001.jpg)를 기준으로 앞/뒤로 쪼개서 넣기
# Referer,Headers → Request Headers → Referer,전체 URL 주소 그대로 복사해서 넣기
# COOKIES,Headers → Request Headers → Cookie,Cookie: 우측의 긴 전체 문자열 복사해서 넣기
 

import os
import requests

# --------------------------------------------------------------------------
# [필수 설정] F12 -> Network 탭 -> Request Headers 내의 Cookie 전체 값 복사 후 붙여넣기
# 쿠키값은 매번 바뀌기 때문에 매번 바꿔주기!!!!!!!!
COOKIES = "WMONID=Pshfgl-zNPg; lgnId=tjgmlwls8843@naver.com; JSESSIONID_HAKSAF=uwEhssS-ExBCqjArLeYXtMua9SoA8cgJ0eoMaWQ1KCXhStzwx20v!-1591731161!-393179310!1787271759038"
# --------------------------------------------------------------------------

# 저장할 폴더 경로 설정 (원하는 경로로 수정 가능)
SAVE_DIR = r"C:\Users\SSAFY\Desktop\github\AI\image_day08"

# 1. 새 Request URL 기반으로 수정된 BASE_URL 및 PARAMS
BASE_URL = "https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2026082020081603500/assets/page-images/page-8e45ecd8-be3cabfd-"
PARAMS = "?timestamp=publish-268201345-0c03"

# 2. 새 Referer 주소 반영 및 Cookie 인코딩 적용
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2026082020081603500/index.html",
    # encode('utf-8').decode('latin-1') 적용으로 헤더 인코딩 오류 방지
    "Cookie": COOKIES.encode('utf-8').decode('latin-1')
}

# 저장 폴더 생성
os.makedirs(SAVE_DIR, exist_ok=True)

print(f"=== SSAFY E-Book 이미지 다운로드 시작 ===")
print(f"저장 경로: {SAVE_DIR}\n")

last_page = 178  # 필요 시 전체 페이지 수에 맞게 변경 (예: 218)
success_count = 0

for page_num in range(1, last_page + 1):
    # 페이지 번호 4자리 포맷팅 (0001, 0002 ...)
    page_str = f"{page_num:04d}"
    img_url = f"{BASE_URL}{page_str}.jpg{PARAMS}"
    file_path = os.path.join(SAVE_DIR, f"page_{page_str}.jpg")

    try:
        res = requests.get(img_url, headers=headers)
        if res.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(res.content)
            success_count += 1
            print(f"[{page_num}/{last_page}] 저장 완료 -> page_{page_str}.jpg")
        else:
            print(f"[{page_num}/{last_page}] 실패 (HTTP 상태 코드: {res.status_code}) - 쿠키 값이나 권한을 확인하세요.")
    except Exception as e:
        print(f"[{page_num}/{last_page}] 에러 발생: {e}")

print(f"\n=== 다운로드 완료: 총 {success_count}/{last_page}개 성공 ===")