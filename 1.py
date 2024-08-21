import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.entry = tk.Entry(self.frame, width=50)
        self.entry.pack(side=tk.LEFT, padx=10)
        
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        
        self.tasks_listbox = tk.Listbox(self.root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)
        
        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT)
        
    def add_task(self):
        task_description = self.entry.get()
        if task_description:
            self.tasks.append(task_description)
            self.update_tasks_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty")
        
    def update_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            new_description = self.entry.get()
            if new_description:
                self.tasks[selected_task_index[0]] = new_description
                self.update_tasks_listbox()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task description cannot be empty")
        else:
            messagebox.showwarning("Warning", "No task selected")
        
    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected")
        
    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
