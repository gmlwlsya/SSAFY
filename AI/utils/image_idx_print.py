# 방법1
# 이미지 범위 내 문자 프린트 
# 해당 출력으로 경로내이미즈프린트 -> md 작성
# last_page = 178
# md_title = "08.4-2.Agent모델.md"

# for i in range(1, last_page + 1):
#     print(f'![alt text](image_day08/page_{i:04d}.jpg)\n')

# print(f"{md_title} 파일 작성이 완료되었습니다!")
# 위 코드로 그대로 파일 저장 시 터미널에서 아래 코드 실행(파일명 변경 가능)
# python image_idx_print.py > AI/08.4-2.Agent모델.md


# 방법2
import os

# page 설정
last_page = 178

# 파일명
md_title ="08.4-2.Agent모델.md"

# AI 폴더 하위에 저장되도록 경로 설정
output_path = os.path.join("AI", md_title)

# 파일 생성 및 작성
with open(output_path, "w", encoding="utf-8") as f:
    for i in range(1, last_page + 1):
        f.write(f'![alt text](image_day08/page_{i:04d}.jpg)\n')

# 터미널에는 완료 메시지만 깔끔하게 출력
print(f"🎉 {output_path} 파일 작성이 완료되었습니다!")