from bs4 import BeautifulSoup

# Đọc file HTML (thay 'index.html' nếu tên file của bạn khác)
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Tìm section có id="guide"
guide_section = soup.find('section', id='guide')

if guide_section:
    # Lấy tiêu đề H2
    title = guide_section.find('h2').get_text(strip=True)
    # Lấy tất cả các thẻ li (các mục lưu ý)
    items = guide_section.find_all('li')
    
    # Phần chân trang tĩnh muốn thêm vào cuối file
    footer_text = """
*** TOOL AUTOEDGEFB ĐƯỢC CUNG CẤP HOÀN TOÀN MIỄN PHÍ ***
*** TÁC GIẢ KHÔNG CHỊU BẤT KỲ TRÁCH NHIỆM NÀO ĐỐI VỚI MỌI HẬU QUẢ PHÁT SINH TỪ VIỆC SỬ DỤNG TOOL ***

Nếu người dùng có bất kỳ thắc mắc hoặc đóng góp, vui lòng liên hệ theo:
➤ Telegram: t.me/autoedgefb
✉ Email: nguyenphuocan131@gmail.com
🌐 Tải Tool tại: autoedgefb.cronpost.com

*** AUTOEDGEFB - Phantom Edition ***
*** © Developed by: anhnn@2026 ***
"""
    
    # Ghi ra file text
    with open('raw-guide.txt', 'w', encoding='utf-8') as out:
        out.write(f"=== {title.upper()} ===\n\n")
        
        # Đánh dấu a, b, c... cho từng dòng giống code Inno Setup cũ của bạn
        for i, item in enumerate(items):
            text_span = item.find('span')
            if text_span:
                # get_text() tự động loại bỏ các thẻ <strong>, <i>, lấy text thuần
                text = text_span.get_text(separator=" ", strip=True)
                char_index = chr(97 + i) # 97 là mã ASCII của chữ 'a'
                out.write(f"{char_index}. {text}\n\n")
                
        # Ghi thêm đoạn footer vào cuối cùng
        out.write(footer_text.strip() + "\n")
                
    print("Đã tạo file raw-guide.txt thành công kèm Footer!")
else:
    print("Không tìm thấy section id='guide' trong HTML.")
