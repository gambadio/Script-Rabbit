import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import os
import json
from anthropic import Anthropic
from default_prompts import DEFAULT_PROMPTS

class DocumentProcessor:
    def __init__(self, master):
        self.master = master
        self.anthropic = None
        self.prompts = DEFAULT_PROMPTS.copy()
        self.current_prompt = "Default"
        self.load_saved_prompts()
        self.setup_ui()

    def setup_ui(self):
        api_frame = ttk.Frame(self.master)
        api_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(api_frame, text="Anthropic API Key:").pack(side=tk.LEFT)
        self.api_key_var = tk.StringVar()
        self.api_key_entry = ttk.Entry(api_frame, textvariable=self.api_key_var, width=40, show="*")
        self.api_key_entry.pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(api_frame, text="Set API Key", command=self.set_api_key).pack(side=tk.LEFT, padx=(10, 0))

        file_frame = ttk.Frame(self.master)
        file_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.file_listbox = tk.Listbox(file_frame, width=70, height=10)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(file_frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        button_frame = ttk.Frame(self.master)
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Button(button_frame, text="Add Files", command=self.add_files).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Remove Selected", command=self.remove_selected).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Process Files", command=self.process_files).pack(side=tk.LEFT, padx=5)

        output_frame = ttk.Frame(self.master)
        output_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(output_frame, text="Output Folder:").pack(side=tk.LEFT)
        self.output_folder = tk.StringVar()
        ttk.Entry(output_frame, textvariable=self.output_folder, width=40).pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(output_frame, text="Browse", command=self.browse_output_folder).pack(side=tk.LEFT, padx=(10, 0))

        prompt_frame = ttk.Frame(self.master)
        prompt_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(prompt_frame, text="Current Prompt:").pack(side=tk.LEFT)
        self.current_prompt_var = tk.StringVar(value=self.current_prompt)
        ttk.Label(prompt_frame, textvariable=self.current_prompt_var).pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(prompt_frame, text="Manage Prompts", command=self.manage_prompts).pack(side=tk.RIGHT)

    def set_api_key(self):
        api_key = self.api_key_var.get()
        if api_key:
            try:
                self.anthropic = Anthropic(api_key=api_key)
                messagebox.showinfo("API Key", "API Key set successfully!")
            except Exception as e:
                messagebox.showerror("API Key Error", f"Error setting API Key: {str(e)}")
        else:
            messagebox.showerror("API Key Error", "Please enter an API Key.")

    def add_files(self):
        files = filedialog.askopenfilenames(filetypes=[("Word Documents", "*.docx"), ("Text Files", "*.txt")])
        for file in files:
            self.file_listbox.insert(tk.END, file)

    def remove_selected(self):
        selection = self.file_listbox.curselection()
        for index in reversed(selection):
            self.file_listbox.delete(index)

    def clear_all(self):
        self.file_listbox.delete(0, tk.END)

    def browse_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder.set(folder)

    def process_files(self):
        if not self.anthropic:
            messagebox.showerror("Error", "Please set your Anthropic API Key first.")
            return

        files = list(self.file_listbox.get(0, tk.END))
        if not files:
            messagebox.showerror("Error", "Please add files to process.")
            return

        output_folder = self.output_folder.get()
        if not output_folder:
            messagebox.showerror("Error", "Please select an output folder.")
            return

        for file in files:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                response = self.anthropic.messages.create(
                    model="claude-3-5-sonnet-20240620",
                    max_tokens=8000,
                    temperature=0.7,
                    system=self.prompts[self.current_prompt],
                    messages=[
                        {"role": "user", "content": f"Please process this content: {content}"}
                    ],
                    extra_headers={"anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"}
                )

                output_content = response.content[0].text if response.content else ""
                
                output_file = os.path.join(output_folder, f"processed_{os.path.basename(file)}.html")
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(output_content)

            except Exception as e:
                messagebox.showerror("Error", f"Error processing file {file}: {str(e)}")

        messagebox.showinfo("Success", "All files processed successfully!")

    def manage_prompts(self):
        prompt_manager = PromptManager(self.master, self.prompts, self.current_prompt)
        self.master.wait_window(prompt_manager)
        if prompt_manager.result:
            self.current_prompt = prompt_manager.result
            self.current_prompt_var.set(self.current_prompt)
        self.save_prompts()

    def load_saved_prompts(self):
        if os.path.exists("saved_prompts.json"):
            with open("saved_prompts.json", "r") as f:
                saved_prompts = json.load(f)
                for name, prompt in saved_prompts.items():
                    if name not in DEFAULT_PROMPTS:
                        self.prompts[name] = prompt

    def save_prompts(self):
        save_dict = {k: v for k, v in self.prompts.items() if k not in DEFAULT_PROMPTS}
        with open("saved_prompts.json", "w") as f:
            json.dump(save_dict, f)

class PromptManager(tk.Toplevel):
    def __init__(self, parent, prompts, current_prompt):
        super().__init__(parent)
        self.parent = parent
        self.prompts = prompts
        self.current_prompt = current_prompt
        self.result = None

        self.title("Prompt Manager")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.prompt_frame = ttk.Frame(self)
        self.prompt_frame.pack(pady=10, padx=10, fill=tk.X)

        ttk.Label(self.prompt_frame, text="Select Prompt:").pack(side=tk.LEFT)
        self.prompt_var = tk.StringVar(value=self.current_prompt)
        self.prompt_combo = ttk.Combobox(self.prompt_frame, textvariable=self.prompt_var, values=list(self.prompts.keys()), state="readonly", width=40)
        self.prompt_combo.pack(side=tk.LEFT, padx=(10, 0))
        self.prompt_combo.bind("<<ComboboxSelected>>", self.on_prompt_selected)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10, padx=10, fill=tk.X)

        ttk.Button(self.button_frame, text="New Prompt", command=self.new_prompt).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Save Changes", command=self.save_changes).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Delete Prompt", command=self.delete_prompt).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Close", command=self.close).pack(side=tk.RIGHT, padx=5)

        self.edit_frame = ttk.Frame(self)
        self.edit_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.prompt_text = tk.Text(self.edit_frame, wrap=tk.WORD)
        self.prompt_text.pack(fill=tk.BOTH, expand=True)

        self.load_current_prompt()

    def on_prompt_selected(self, event):
        selected_prompt = self.prompt_var.get()
        self.prompt_text.delete("1.0", tk.END)
        self.prompt_text.insert(tk.END, self.prompts[selected_prompt])

    def new_prompt(self):
        new_name = simpledialog.askstring("New Prompt", "Enter a name for the new prompt:", parent=self)
        if new_name:
            if new_name in self.prompts:
                messagebox.showerror("Error", "A prompt with this name already exists.")
            else:
                self.prompts[new_name] = ""
                self.prompt_combo['values'] = list(self.prompts.keys())
                self.prompt_var.set(new_name)
                self.prompt_text.delete("1.0", tk.END)

    def save_changes(self):
        current_name = self.prompt_var.get()
        new_content = self.prompt_text.get("1.0", tk.END).strip()
        
        if current_name in DEFAULT_PROMPTS:
            new_name = simpledialog.askstring("Save as New Prompt", 
                f"The '{current_name}' prompt is a default prompt and cannot be modified directly. Enter a new name to save these changes as a new prompt:",
                parent=self)
            if new_name:
                if new_name in self.prompts:
                    messagebox.showerror("Error", "A prompt with this name already exists.")
                else:
                    self.prompts[new_name] = new_content
                    self.prompt_combo['values'] = list(self.prompts.keys())
                    self.prompt_var.set(new_name)
                    messagebox.showinfo("Saved", f"Changes saved as new prompt '{new_name}'.")
            else:
                messagebox.showinfo("Not Saved", "Changes were not saved.")
        else:
            self.prompts[current_name] = new_content
            messagebox.showinfo("Saved", f"Changes to '{current_name}' have been saved.")

    def delete_prompt(self):
        current_name = self.prompt_var.get()
        if current_name in DEFAULT_PROMPTS:
            messagebox.showinfo("Cannot Delete", f"The '{current_name}' prompt is a default prompt and cannot be deleted.")
            return
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the prompt '{current_name}'?"):
            del self.prompts[current_name]
            self.prompt_combo['values'] = list(self.prompts.keys())
            if self.prompts:
                self.prompt_var.set(next(iter(self.prompts)))
                self.on_prompt_selected(None)
            else:
                self.prompt_var.set("")
                self.prompt_text.delete("1.0", tk.END)

    def load_current_prompt(self):
        self.prompt_text.delete("1.0", tk.END)
        self.prompt_text.insert(tk.END, self.prompts[self.current_prompt])

    def close(self):
        self.result = self.prompt_var.get()
        self.destroy()
