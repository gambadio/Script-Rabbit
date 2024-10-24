# processor.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import os
import json
from anthropic import Anthropic
from docx import Document
from default_prompts import DEFAULT_PROMPTS
import re
from cryptography.fernet import Fernet
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class DocumentProcessor:
    def __init__(self, master):
        self.master = master
        self.anthropic = None
        self.prompts = DEFAULT_PROMPTS.copy()
        self.current_prompt = "Academic_Content_Formatter"
        self.file_paths = []
        self.last_output_folder = None
        
        # Create StringVar before setup_ui
        self.api_key_var = tk.StringVar()
        self.api_status_var = tk.StringVar(value="API Key: Not Set")
        
        self.encryption_key = self.get_or_create_key()
        self.setup_ui()
        
        # Load saved data after UI is setup
        self.load_saved_prompts()
        self.load_saved_api_key()

    def get_or_create_key(self):
        key_file = "encryption.key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, "wb") as f:
                f.write(key)
            return key

    def encrypt_api_key(self, api_key):
        f = Fernet(self.encryption_key)
        return f.encrypt(api_key.encode()).decode()

    def decrypt_api_key(self, encrypted_api_key):
        f = Fernet(self.encryption_key)
        return f.decrypt(encrypted_api_key.encode()).decode()

    def save_api_key(self, api_key):
        encrypted_key = self.encrypt_api_key(api_key)
        config = {}
        
        if os.path.exists("config.json"):
            with open("config.json", "r") as f:
                config = json.load(f)
        
        config["api_key"] = encrypted_key
        
        with open("config.json", "w") as f:
            json.dump(config, f)

    def load_saved_api_key(self):
        try:
            if os.path.exists("config.json"):
                with open("config.json", "r") as f:
                    config = json.load(f)
                    if "api_key" in config:
                        decrypted_key = self.decrypt_api_key(config["api_key"])
                        self.api_key_var.set(decrypted_key)
                        self.set_api_key(silent=True)
                        self.api_status_var.set("API Key: Set")
        except Exception as e:
            print(f"Error loading API key: {e}")
            self.api_status_var.set("API Key: Error Loading")

    def setup_ui(self):
        # API Frame
        api_frame = ttk.Frame(self.master)
        api_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(api_frame, text="Anthropic API Key:").pack(side=tk.LEFT)
        self.api_key_entry = ttk.Entry(api_frame, textvariable=self.api_key_var, width=40, show="*")
        self.api_key_entry.pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(api_frame, text="Set API Key", command=self.set_api_key).pack(side=tk.LEFT, padx=(10, 0))
        ttk.Label(api_frame, textvariable=self.api_status_var).pack(side=tk.LEFT, padx=(10, 0))

        # File Frame
        file_frame = ttk.Frame(self.master)
        file_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Upload Buttons Frame
        button_frame = ttk.Frame(file_frame)
        button_frame.pack(fill=tk.X, pady=(0, 5))

        ttk.Button(button_frame, text="Upload DOCX Files", 
                  command=self.upload_files).pack(side=tk.LEFT, padx=5)

        # Listbox with Scrollbar
        listbox_frame = ttk.Frame(file_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True)

        self.file_listbox = tk.Listbox(listbox_frame, width=70, height=10, selectmode=tk.EXTENDED)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        # Control Buttons Frame
        control_frame = ttk.Frame(self.master)
        control_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Button(control_frame, text="Remove Selected", command=self.remove_selected).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Clear All", command=self.clear_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Process Files", command=self.process_files).pack(side=tk.LEFT, padx=5)

        # Output Frame
        output_frame = ttk.Frame(self.master)
        output_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(output_frame, text="Output Folder:").pack(side=tk.LEFT)
        self.output_folder = tk.StringVar()
        ttk.Entry(output_frame, textvariable=self.output_folder, width=40).pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(output_frame, text="Browse", command=self.browse_output_folder).pack(side=tk.LEFT, padx=(10, 0))

        # Prompt Frame
        prompt_frame = ttk.Frame(self.master)
        prompt_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(prompt_frame, text="Current Prompt:").pack(side=tk.LEFT)
        self.current_prompt_var = tk.StringVar(value=self.current_prompt)
        ttk.Label(prompt_frame, textvariable=self.current_prompt_var).pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(prompt_frame, text="Manage Prompts", command=self.manage_prompts).pack(side=tk.RIGHT)

    def set_api_key(self, silent=False):
        api_key = self.api_key_var.get()
        if api_key:
            try:
                self.anthropic = Anthropic(api_key=api_key)
                if not silent:
                    messagebox.showinfo("API Key", "API Key set successfully!")
                self.save_api_key(api_key)
                self.api_status_var.set("API Key: Set")
            except Exception as e:
                if not silent:
                    messagebox.showerror("API Key Error", f"Error setting API Key: {str(e)}")
                self.api_status_var.set("API Key: Error")
        else:
            if not silent:
                messagebox.showerror("API Key Error", "Please enter an API Key.")
            self.api_status_var.set("API Key: Not Set")

    def upload_files(self):
        files = filedialog.askopenfilenames(filetypes=[('Word Documents', '*.docx')])
        for file in files:
            if file not in self.file_paths:
                self.file_paths.append(file)
                self.file_listbox.insert(tk.END, os.path.basename(file))

    def load_split_files(self, folder_path):
        self.clear_all()
        self.file_paths = []
        
        files = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.docx'):
                full_path = os.path.join(folder_path, filename)
                files.append((self.get_sort_key(filename), full_path, filename))
        
        files.sort(key=lambda x: x[0])
        
        for _, full_path, filename in files:
            self.file_listbox.insert(tk.END, filename.replace('.docx', ''))
            self.file_paths.append(full_path)
        
        self.output_folder.set(os.path.join(folder_path, 'processed'))

    def get_sort_key(self, filename):
        base_name = os.path.splitext(filename)[0]
        parts = re.split('([0-9]+)', base_name)
        parts = [int(part) if part.isdigit() else part.lower() for part in parts]
        return parts

    def browse_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder.set(folder)

    def remove_selected(self):
        selection = self.file_listbox.curselection()
        for index in reversed(selection):
            self.file_listbox.delete(index)
            del self.file_paths[index]

    def clear_all(self):
        self.file_listbox.delete(0, tk.END)
        self.file_paths.clear()

    def get_next_folder_name(self, base_path):
        """Get the next available 'processed_n' folder name"""
        if not os.path.exists(os.path.join(base_path, "processed")):
            return "processed"
        
        i = 2
        while os.path.exists(os.path.join(base_path, f"processed_{i}")):
            i += 1
        return f"processed_{i}"

    def process_files(self):
        if not self.anthropic:
            messagebox.showerror("Error", "Please set your Anthropic API Key first.")
            return

        if not self.file_paths:
            messagebox.showerror("Error", "No files to process.")
            return

        base_folder = self.output_folder.get()
        if not base_folder:
            messagebox.showerror("Error", "Please select an output folder.")
            return

        # Determine output folder name
        output_folder_name = self.get_next_folder_name(base_folder)
        output_folder = os.path.join(base_folder, output_folder_name)
        
        try:
            os.makedirs(output_folder, exist_ok=True)
        except Exception as e:
            messagebox.showerror("Error", f"Could not create output folder: {str(e)}")
            return

        processed_files = []
        for file_path in self.file_paths:
            try:
                doc = Document(file_path)
                content = "\n".join([para.text for para in doc.paragraphs])
                
                response = self.anthropic.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=8000,
                    temperature=0.7,
                    system=self.prompts[self.current_prompt],
                    messages=[
                        {"role": "user", "content": f"Please process this content: {content}"}
                    ]
                )

                output_content = response.content[0].text if response.content else ""
                
                original_filename = os.path.basename(file_path)
                base_name = os.path.splitext(original_filename)[0]
                output_file = os.path.join(output_folder, f"{base_name}.html")
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(output_content)
                
                processed_files.append(output_file)

            except Exception as e:
                messagebox.showerror("Error", f"Error processing file {file_path}: {str(e)}")

        if processed_files:
            self.last_output_folder = output_folder
            messagebox.showinfo("Success", f"All files processed successfully in folder:\n{output_folder}")
        else:
            messagebox.showwarning("Warning", "No files were processed successfully.")

    def load_saved_prompts(self):
        if os.path.exists("saved_prompts.json"):
            try:
                with open("saved_prompts.json", "r") as f:
                    saved_prompts = json.load(f)
                    for name, prompt in saved_prompts.items():
                        if name not in DEFAULT_PROMPTS:
                            self.prompts[name] = prompt
            except Exception as e:
                print(f"Error loading saved prompts: {e}")

    def save_prompts(self):
        save_dict = {k: v for k, v in self.prompts.items() if k not in DEFAULT_PROMPTS}
        try:
            with open("saved_prompts.json", "w") as f:
                json.dump(save_dict, f)
        except Exception as e:
            print(f"Error saving prompts: {e}")

    def manage_prompts(self):
        prompt_manager = PromptManager(self.master, self.prompts, self.current_prompt)
        self.master.wait_window(prompt_manager)
        if prompt_manager.result:
            self.current_prompt = prompt_manager.result
            self.current_prompt_var.set(self.current_prompt)
        self.save_prompts()


class PromptManager(tk.Toplevel):
    def __init__(self, parent, prompts, current_prompt):
        super().__init__(parent)
        self.parent = parent
        self.prompts = prompts
        self.current_prompt = current_prompt
        self.result = None

        self.transient(parent)
        self.grab_set()
        self.attributes('-topmost', True)

        self.title("Prompt Manager")
        self.geometry("700x500")

        self.create_widgets()

    def create_widgets(self):
        self.prompt_frame = ttk.Frame(self)
        self.prompt_frame.pack(pady=10, padx=10, fill=tk.X)

        ttk.Label(self.prompt_frame, text="Select Prompt:").pack(side=tk.LEFT)
        self.prompt_var = tk.StringVar(value=self.current_prompt)
        self.prompt_combo = ttk.Combobox(self.prompt_frame, textvariable=self.prompt_var, 
                                       values=list(self.prompts.keys()), state="readonly", width=40)
        self.prompt_combo.pack(side=tk.LEFT, padx=(10, 0))
        self.prompt_combo.bind("<<ComboboxSelected>>", self.on_prompt_selected)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10, padx=10, fill=tk.X)

        ttk.Button(self.button_frame, text="New Prompt", command=self.new_prompt).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Save Changes", command=self.save_changes).pack(side=tk.LEFT, padx=5)
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

