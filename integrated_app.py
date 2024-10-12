import tkinter as tk
from tkinter import ttk
import os
from splitter import DocumentSplitter
from processor import DocumentProcessor
from merger import DocumentMerger

class IntegratedApp:
    def __init__(self, master):
        self.master = master
        master.title("Integrated Document Processor")
        master.geometry("800x600")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.splitter_frame = ttk.Frame(self.notebook)
        self.processor_frame = ttk.Frame(self.notebook)
        self.merger_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.splitter_frame, text="Splitter")
        self.notebook.add(self.processor_frame, text="Processor")
        self.notebook.add(self.merger_frame, text="Merger")

        self.splitter = DocumentSplitter(self.splitter_frame, self.on_split_complete)
        self.processor = DocumentProcessor(self.processor_frame)
        self.merger = DocumentMerger(self.merger_frame)

    def on_split_complete(self, output_folder):
        self.processor.load_split_files(output_folder)
        self.notebook.select(1)  # Switch to the Processor tab
