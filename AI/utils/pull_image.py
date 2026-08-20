import os
import requests

# --------------------------------------------------------------------------
# [필수 설정] F12 -> Network 탭 -> Request Headers 내의 Cookie 전체 값 복사 후 붙여넣기
# 쿠키값은 매번 바뀌기 때문에 매번 바꿔주기!!!!!!!!
COOKIES = "WMONID=Pshfgl-zNPg; lgnId=tjgmlwls8843@naver.com; JSESSIONID_HAKSAF=zqwcc6ALppiIgFB0pbE7fM4rx92Yv-7ZpekDzrFSclvxHXER00f5!1280883601!-290790654!1787183734795"
# --------------------------------------------------------------------------

# 저장할 폴더 경로 설정 (역슬래시 경로를 위해 r"" 형태로 작성)
SAVE_DIR = r"C:\Users\SSAFY\Desktop\github\AI\image_day07"

# 기본 URL 및 고유 파라미터
BASE_URL = "https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2026082010034304700/assets/page-images/page-979aa903-f3693f77-"
PARAMS = "?timestamp=publish-26820957-fdcb"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://edu.ssafy.com/",
    # encode('utf-8').decode('latin-1') 을 추가하여 헤더 인코딩 오류 방지
    "Cookie": COOKIES.encode('utf-8').decode('latin-1')
}

# 폴더가 없을 경우 자동 생성
os.makedirs(SAVE_DIR, exist_ok=True)

print(f"=== SSAFY E-Book 이미지 다운로드 시작 ===")
print(f"저장 경로: {SAVE_DIR}\n")

success_count = 0

# 범위는 해당 교재 범위에 맞춰 설정
for page_num in range(1, 219):
    # 1 -> 0001, 218 -> 0218 포맷팅
    page_str = f"{page_num:04d}"
    img_url = f"{BASE_URL}{page_str}.jpg{PARAMS}"
    file_path = os.path.join(SAVE_DIR, f"page_{page_str}.jpg")

    try:
        res = requests.get(img_url, headers=headers)
        if res.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(res.content)
            success_count += 1
            print(f"[{page_num}/218] 저장 완료 -> page_{page_str}.jpg")
        else:
            print(f"[{page_num}/218] 실패 (HTTP 상태 코드: {res.status_code}) - 쿠키 값이나 권한을 확인하세요.")
    except Exception as e:
        print(f"[{page_num}/218] 에러 발생: {e}")

print(f"\n=== 다운로드 완료: 총 {success_count}/218개 성공 ===")