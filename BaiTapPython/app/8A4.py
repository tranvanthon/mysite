import time
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
import random
import os

# --- DANH SÁCH HỌC SINH ---
students = {
    "Phan Hoàng Anh": "images/Anh.png",
    "Trương Thị Như Bình": "images/Binh.png",
    "Lâm Thanh Duy": "images/Duy.png",
    "Nguyễn Tiến Đạt": "images/Đạt.png",
    "Nguyễn Hải Đăng": "images/Đăng.png",
    "Nguyễn Thị Mỹ Hạnh": "images/Hạnh.png",
    "Lê Mai Chí Hiền": "images/Hiền.png",
    "Cao Văn Lê Hoài": "images/Hoài.png",
    "Nguyễn Khải Hoàng": "images/Hoàng.png",
    "Lê Thị Thanh Hương": "images/Hương.png",
    "Tạ Minh Kha": "images/Kha.png",
    "Phạm Đăng Khoa": "images/KhoaPham.png",
    "Lư Phan Đăng Khoa": "images/KhoaLu.png",
    "Trương Tấn Khoa": "images/KhoaTruong.png",
    "Võ Thị Ngọc Lam": "images/Lam.png",
    "Nguyễn Trần Phi Long": "images/Long.png",
    "Lê Nguyễn Huỳnh Mai": "images/Mai.png",
    "Nguyễn Huỳnh Diễm My": "images/My.png",
    "Huỳnh Lê Ngọc Ngân": "images/Ngân.png",
    "Liêu Khôi Nguyên": "images/NguyênLieu.png",
    "Phan Trần Vạn Nguyên": "images/NguyênPham.png",
    "Nguyễn Thanh Nhật": "images/Nhật.png",
    "Phan Ngọc Bình Nhi": "images/Nhi.png",
    "Huỳnh Thị Ngọc Như": "images/Như.png",
    "Dương Thanh Phú": "images/Phú.png",
    "Hồ Thị Đào Quyên": "images/Quyên.png",
    "Nguyễn Thành Tài": "images/Tài.png",
    "Trần Văn Tấn": "images/Tấn.png",
    "Nguyễn Hoàng Thịnh": "images/Thịnh.png",
    "Nguyễn Trương Minh Thùy": "images/Thuy2.png",
    "Võ Ngọc Tuyền": "images/Tuyền.png",
    "Nguyễn Thị Thanh Thúy": "images/Thuy1.png",
    "Nguyễn Derik Thành Trí": "images/TriDerik.png",
    "Ngô Thanh Trí": "images/TriNgo.png",
    "Nguyễn Lam Trường": "images/Trường.png",
    "Lư Nguyễn Ngọc Vy": "images/Vy.png",
    "Lê Văn Bảo Vinh": "images/Vinh.png",
    "Nguyễn Lê Thanh Vân": "images/Vân.png",
    "Nguyễn Thị Đào Uyên": "images/Uyên.png",
    "Nguyễn Thị Minh Tuyết": "images/Tuyết.png",
    "Dương Thị Như Ý": "images/ý.png",
}

remaining_students = list(students.keys())


# --- HÀM HIỂN THỊ ẢNH ---
def show_image(img_path):
    if not img_path or not os.path.exists(img_path):
        photo_label.config(image="", text="(Không có ảnh)", fg="gray")
        return
    img = Image.open(img_path)
    img = img.resize((300, 450), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    photo_label.config(image=photo)
    photo_label.image = photo


# --- HIỆU ỨNG XOAY NGẪU NHIÊN ---
def spin_randomly(duration=2000, interval=100):
    end_time = time.time() + duration / 1000
    result_label.config(fg="black")

    def spin():
        if time.time() < end_time:
            name = random.choice(list(students.keys()))
            result_label.config(text=name)
            root.after(interval, spin)
        else:
            pick_random()

    spin()


# --- HIỆU ỨNG MỜ DẦN KHI HIỆN TÊN ---
def fade_in_text(label, text, steps=15, delay=80):
    label.config(text=text)
    for i in range(steps):
        color_value = int(255 * (i / steps))
        hex_color = f"#{color_value:02x}{color_value:02x}{255:02x}"
        root.after(i * delay, lambda c=hex_color: label.config(fg=c))


# --- HIỆU ỨNG NHẤP NHÁY ẢNH ---
def flash_photo(times=6, delay=200):
    def flash(count=0):
        if count < times:
            if photo_label.winfo_ismapped():
                photo_label.pack_forget()
            else:
                photo_label.pack(pady=30)
            root.after(delay, flash, count + 1)

    flash()


# --- CHỌN NGẪU NHIÊN ---
def pick_random(event=None):
    if not remaining_students:
        fade_in_text(result_label, "🎉 Hết người để chọn!", steps=10)
        return
    name = random.choice(remaining_students)
    remaining_students.remove(name)

    fade_in_text(result_label, f"🎯 {name}", steps=5, delay=70)
    show_image(students.get(name))
    flash_photo()


# --- BẮT ĐẦU XOAY ---
def start_spin(event=None):
    if not remaining_students:
        fade_in_text(result_label, "🎉 Hết người để chọn!", steps=10)
        return
    spin_randomly(duration=2500, interval=80)


# --- THOÁT ---
def quit_app():
    root.destroy()


# --- GIAO DIỆN ---
root = tk.Tk()
root.title("🎓 BỐC THĂM NGẪU NHIÊN - HIỂN THỊ ẢNH 🎓")
root.geometry("1024x768")
root.resizable(False, False)

# --- ẢNH NỀN ---
try:
    bg_image = Image.open("images/background.jpg")
    bg_image = bg_image.resize((1024, 768), Image.LANCZOS)
    bg_image = bg_image.filter(ImageFilter.GaussianBlur(radius=5))  # 💨 Làm mờ nền
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Lỗi tải ảnh nền: {e}")

# --- TIÊU ĐỀ ---
title_label = tk.Label(
    root,
    text="🎯 CHƯƠNG TRÌNH BỐC THĂM HỌC SINH 8A4 🎯",
    font=("Helvetica", 32, "bold"),
    bg="#ffffff",
    fg="#0044cc",
)
title_label.pack(pady=25)

# --- ẢNH HỌC SINH ---
photo_label = tk.Label(root, bg="#ffffff")
photo_label.pack(pady=30)

# --- NHÃN KẾT QUẢ ---
result_label = tk.Label(
    root,
    text="Nhấn Enter hoặc nút dưới để chọn 🎲",
    font=("Helvetica", 26, "bold"),
    bg="#ffffff",
    fg="black",
)
result_label.pack(pady=25)

# --- NÚT CHỌN NGƯỜI ---
pick_button = tk.Button(
    root,
    text="🎯 Bắt đầu bốc thăm",
    font=("Helvetica", 20, "bold"),
    bg="#4CAF50",
    fg="white",
    width=18,
    height=2,
    command=start_spin,
)
pick_button.pack(pady=15)

# --- NÚT THOÁT ---
exit_button = tk.Button(
    root,
    text="🚪 Thoát",
    font=("Helvetica", 18, "bold"),
    bg="#f44336",
    fg="white",
    width=15,
    height=1,
    command=quit_app,
)
exit_button.pack(pady=5)

# --- PHÍM ENTER ---
root.bind("<Return>", start_spin)

root.mainloop()
