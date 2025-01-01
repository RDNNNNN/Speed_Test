import speedtest
import tkinter as tk


def speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000
    upload_speed = st.upload() / 1000000
    ping = st.results.ping

    result_label.config(
        text=f"下載速度: {download_speed:.2f} Mbps\n上傳速度: {upload_speed:.2f} Mbps\nPing: {ping:.2f} ms"
    )


window = tk.Tk()
window.title("網速測試")
window.geometry("300x200")

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

test_button = tk.Button(window, text="測試", font=("Arial", 12), command=speed_test)
test_button.pack(pady=10)

window.mainloop()
