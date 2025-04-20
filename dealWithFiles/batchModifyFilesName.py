import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def batch_rename(directory, prefix_filter, suffix_filter, operation, match_regex, source_text, target_text):
    try:
        for filename in os.listdir(directory):
            if not os.path.isfile(os.path.join(directory, filename)):
                continue

            name, ext = os.path.splitext(filename)
            if prefix_filter and not name.startswith(prefix_filter):
                continue
            if suffix_filter and not name.endswith(suffix_filter):
                continue

            new_name = name

            if operation == '增加':
                if match_regex:
                    match = re.search(match_regex, new_name)
                    if match:
                        new_name = new_name[:match.end()] + target_text + new_name[match.end():]
            elif operation == '替换':
                new_name = new_name.replace(source_text, target_text)

            new_filename = new_name + ext
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        messagebox.showinfo("成功", "批量重命名完成！")
    except Exception as e:
        messagebox.showerror("错误", str(e))

def select_directory():
    folder = filedialog.askdirectory()
    if folder:
        dir_var.set(folder)

def on_rename():
    batch_rename(
        dir_var.get(),
        prefix_var.get(),
        suffix_var.get(),
        operation_var.get(),
        regex_var.get(),
        source_var.get(),
        target_var.get()
    )

root = tk.Tk()
root.title("批量文件重命名工具")
root.geometry("500x400")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 目录选择
dir_var = tk.StringVar()
tk.Label(frame, text="选择目录:").grid(row=0, column=0, sticky='w')
tk.Entry(frame, textvariable=dir_var, width=40).grid(row=0, column=1)
tk.Button(frame, text="浏览", command=select_directory).grid(row=0, column=2)

# 前缀
tk.Label(frame, text="前缀过滤:").grid(row=1, column=0, sticky='w')
prefix_var = tk.StringVar()
tk.Entry(frame, textvariable=prefix_var).grid(row=1, column=1, columnspan=2, sticky='we')

# 后缀
tk.Label(frame, text="后缀过滤:").grid(row=2, column=0, sticky='w')
suffix_var = tk.StringVar()
tk.Entry(frame, textvariable=suffix_var).grid(row=2, column=1, columnspan=2, sticky='we')

# 操作类型
operation_var = tk.StringVar(value="增加")
tk.Label(frame, text="操作类型:").grid(row=3, column=0, sticky='w')
ttk.Combobox(frame, textvariable=operation_var, values=["增加", "替换"]).grid(row=3, column=1, columnspan=2, sticky='we')

# 正则匹配语法
regex_var = tk.StringVar()
tk.Label(frame, text="正则匹配(用于增加):").grid(row=4, column=0, sticky='w')
tk.Entry(frame, textvariable=regex_var).grid(row=4, column=1, columnspan=2, sticky='we')

# 替换源
source_var = tk.StringVar()
tk.Label(frame, text="源字符串(用于替换):").grid(row=5, column=0, sticky='w')
tk.Entry(frame, textvariable=source_var).grid(row=5, column=1, columnspan=2, sticky='we')

# 替换目标 / 增加内容
target_var = tk.StringVar()
tk.Label(frame, text="目标字符串/新增内容:").grid(row=6, column=0, sticky='w')
tk.Entry(frame, textvariable=target_var).grid(row=6, column=1, columnspan=2, sticky='we')

# 执行按钮
tk.Button(frame, text="开始重命名", command=on_rename).grid(row=7, column=0, columnspan=3, pady=10)

root.mainloop()
if __name__ == '__main__':
    pass