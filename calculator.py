# Nhập thư viện tkinter để tạo giao diện đồ họa
from tkinter import *
from tkinter import messagebox

# Tạo cửa sổ chính
window = Tk()
window.title("Máy Tính Đơn Giản")
window.geometry("400x500")
window.configure(bg="#f0f0f0")

# Tạo biến để lưu trữ các số và kết quả
num1_var = StringVar()
num2_var = StringVar()
result_var = StringVar()

# Hàm kiểm tra đầu vào có phải là số không
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Hàm thực hiện phép tính
def calculate(operation):
    # Lấy giá trị từ ô nhập liệu
    num1 = num1_var.get()
    num2 = num2_var.get()
    
    # Kiểm tra đầu vào
    if not num1 or not num2:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ hai số!")
        return
    
    if not is_number(num1) or not is_number(num2):
        messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số!")
        return
    
    # Chuyển đổi sang số
    num1 = float(num1)
    num2 = float(num2)
    
    # Thực hiện phép tính
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Lỗi", "Không thể chia cho 0!")
                return
            result = num1 / num2
        
        # Hiển thị kết quả
        result_var.set(f"Kết quả: {result}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

# Tạo các thành phần giao diện
Label(window, text="Máy Tính Đơn Giản", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

# Khung nhập số thứ nhất
frame1 = Frame(window, bg="#f0f0f0")
frame1.pack(pady=10)
Label(frame1, text="Số thứ nhất:", bg="#f0f0f0").pack(side=LEFT)
Entry(frame1, textvariable=num1_var).pack(side=LEFT, padx=10)

# Khung nhập số thứ hai
frame2 = Frame(window, bg="#f0f0f0")
frame2.pack(pady=10)
Label(frame2, text="Số thứ hai:  ", bg="#f0f0f0").pack(side=LEFT)
Entry(frame2, textvariable=num2_var).pack(side=LEFT, padx=10)

# Khung chứa các nút phép tính
button_frame = Frame(window, bg="#f0f0f0")
button_frame.pack(pady=20)

# Tạo các nút phép tính
Button(button_frame, text="+", command=lambda: calculate("+"), width=10).pack(side=LEFT, padx=5)
Button(button_frame, text="-", command=lambda: calculate("-"), width=10).pack(side=LEFT, padx=5)
Button(button_frame, text="×", command=lambda: calculate("*"), width=10).pack(side=LEFT, padx=5)
Button(button_frame, text="÷", command=lambda: calculate("/"), width=10).pack(side=LEFT, padx=5)

# Nhãn hiển thị kết quả
Label(window, textvariable=result_var, font=("Arial", 14), bg="#f0f0f0").pack(pady=20)

# Chạy chương trình
window.mainloop()
