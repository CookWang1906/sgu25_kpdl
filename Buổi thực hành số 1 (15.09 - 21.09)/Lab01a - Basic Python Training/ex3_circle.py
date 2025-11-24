'''Bài 7. Tính chu vi và diện tích hình tròn:
- Nhập vào bán kính r là số thực.
- Sau đó, tính chu vi và diện tích hình tròn biết: cv = 2πr, dt = πr2.'''

import math
# Nhập và kiểm tra
try:
    r = float(input("Nhập bán kính của hình tròn (r): "))

    if r < 0:
        print("Bán kính không thể là số âm. Vui lòng nhập lại.")
    else:
        # Tính toán
        chu_vi = 2 * math.pi * r
        dien_tich = math.pi * (r ** 2)

        # In ra kết quả
        print(f"Chu vi của hình tròn là: {chu_vi:.2f}")
        print(f"Diện tích của hình tròn là: {dien_tich:.2f}")

except ValueError:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số.")