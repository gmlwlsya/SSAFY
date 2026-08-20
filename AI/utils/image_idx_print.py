# 방법1
# 이미지 범위 내 문자 프린트 
# 해당 출력으로 경로내이미즈프린트 -> md 작성
for i in range(1, 219):
    if i < 10:
        text = f'![alt text](image_day07/page_000{i}.jpg)'
        print(text)

    elif i < 100:
        text = f'![alt text](image_day07/page_00{i}.jpg)'
        print(text)
    else:
        text = f'![alt text](image_day07/page_0{i}.jpg)'
        print(text)
# 위 코드로 그대로 파일 저장 시 터미널에서 아래 코드 실행(파일명 변경 가능)
# python image_idx_print.py > output_images.md


# 방법2
# 결과를 저장할 파일명 설정 (py, md, txt 등 변경 가능)
# 파일명 변경 가능
output_filename = "output_images.md"

with open(output_filename, "w", encoding="utf-8") as f:
    # 범위 변경 가능
    for i in range(1, 219):
        # zfill(4)를 사용하면 1 -> '0001', 12 -> '0012', 100 -> '0100' 으로 자동 맞춤됩니다.
        formatted_num = str(i).zfill(4)
        text = f"![alt text](image_day07/page_{formatted_num}.jpg)\n"
        f.write(text)

print(f"저장이 완료되었습니다: {output_filename}")