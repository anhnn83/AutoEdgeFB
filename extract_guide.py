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
*** THE AUTOEDGEFB TOOL IS PROVIDED COMPLETELY FREE OF CHARGE ***
*** THE AUTHOR BEARS NO RESPONSIBILITY FOR ANY CONSEQUENCES ARISING FROM THE USE OF THE TOOL ***

Users with any questions or contributions, please contact:
Nguyen Ngoc Anh
➤ Telegram: t.me/anhnn83
✉ Email: anhnn@dgd.vn
🌐 Download Tool at: autoedgefb.cronpost.com

AUTOEDGEFB - Phantom Edition
© 2026 Developed by anhnn
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
