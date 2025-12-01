import streamlit as   作为 st
import tkinter as   作为 tk
import random

st.title("Web"   “网络”)
st.write   写("Click it to RUN"   “点击它运行”)
if   如果 st.button("Clicked"   “点击”):
    st.success("it's running")   “运行”

    def on_closing():
        pass   通过
    
    
    def close_all_other_windows():
        global root   全球根
        if root.winfo_exists():   如果root.winfo_exists ():
            root.destroy()
            for widget in   在 root.winfo_children():
                if isinstance(widget, tk.Toplevel):如果是实例（widget）， tk。最高级的):
                    widget.destroy()
    
    
    def show_thanks_popup():
        thanks_popup = tk.Toplevel()thank_popup = tk. top （）
        thanks_popup.title("感谢")
        thanks_popup.protocol("WM_DELETE_WINDOW", on_closing)
        screen_width = thanks_popup.winfo_screenwidth()Screen_width = thank_popup .winfo_screenwidth（）
        screen_height = thanks_popup.winfo_screenheight()Screen_height = thank_popup .winfo_screenheight（）
        x = (screen_width - 300) // 2X = (screen_width - 300) //
        y = (screen_height - 150) // 2Y = (screen_height - 150) //
        thanks_popup.geometry(f"300x150+{x}+{y}")
        thanks_label = tk.Label(thanks_popup, text="谢谢你 我爱你", font=("微软雅黑", 20))
        thanks_label.pack(pady=30)
        thanks_popup.after(1500, lambda: close_all_other_windows())thanks_popup。After （1500, lambda: close_all_other_windows()）
    
    
    def create_child_popup(parent):def create_child_popup(父):
        child = tk.Toplevel(parent)孩子= tk。最高级的(父母)
        child.title("来自Zejun_Fu")
        child.resizable(False   假, False   假)
        child.protocol("WM_DELETE_WINDOW", on_closing)
    
        screen_width = child.winfo_screenwidth()
        screen_height = child.winfo_screenheight()
        x = random.randint(0, screen_width - 400)
        y = random.randint(0, screen_height - 200)
        child.geometry(f"400x200+{x}+{y}")
    
        message_label = tk.Label(child, text="同学 我已经喜欢你很久了\n能请你成为我的恋人吗", font=("微软雅黑", 20))
        message_label.pack(pady=30)
    
        accept_button = tk.Button(child, text="Yes", font=("微软雅黑", 14),
                                  command=show_thanks_popup)
        accept_button.place(x=50, y=120)
    
        reject_button = tk.Button(child, text="No", font=("微软雅黑", 14),
                                  command=lambda: create_child_popup(child))
        reject_button.place(x=250, y=120)
    
    
    root = tk.Tk()
    root.title("来自Zejun_Fu")
    root.resizable(False   假, False   假)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"400x200+{(screen_width - 400) // 2}+{(screen_height - 200) // 2}")
    
    message_label = tk.Label(root, text="同学 我已经喜欢你很久了\n能请你成为我的恋人吗", font=("微软雅黑", 20))
    message_label.pack(pady=30)
    
    accept_button = tk.Button(root, text="Yes", font=("微软雅黑", 14),
                              command=show_thanks_popup)
    accept_button.place(x=50, y=120)
    
    reject_button = tk.Button(root, text="No", font=("微软雅黑", 14),
                              command=lambda: create_child_popup(root))
    reject_button.place(x=250, y=120)
    
    root.mainloop()

result = "Result = success"
st.write(result)
