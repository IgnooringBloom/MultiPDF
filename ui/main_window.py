from PyQt6.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, 
                            QPushButton, QListWidget, QLabel, QFileDialog, QStatusBar) # Importing all the necessary classes from the library.
from PyQt6.QtCore import Qt
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Page Arranger")
        self.setMinimumSize(800, 600)
        self.setup_ui()
        
    def setup_ui(self):
        # Create central widget and main layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        
        # Create toolbar with buttons
        toolbar_layout = QHBoxLayout()
        self.open_btn = QPushButton("Open PDF")
        self.save_btn = QPushButton("Save PDF")
        self.save_btn.setEnabled(False)
        
        toolbar_layout.addWidget(self.open_btn)
        toolbar_layout.addWidget(self.save_btn)
        toolbar_layout.addStretch()
        
        # Content area with thumbnails and preview
        content_layout = QHBoxLayout()
        
        # Thumbnails list on the left
        self.thumbnails_list = QListWidget()
        self.thumbnails_list.setDragDropMode(QListWidget.DragDropMode.InternalMove)
        self.thumbnails_list.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        
        # Preview area on the right
        self.preview_widget = QLabel("Select a page to preview")
        self.preview_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        content_layout.addWidget(self.thumbnails_list, 1)
        content_layout.addWidget(self.preview_widget, 2)
        
        # Add layouts to main layout
        main_layout.addLayout(toolbar_layout)
        main_layout.addLayout(content_layout)
        
        # Set central widget
        self.setCentralWidget(central_widget)
        
        # Create status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")
        
        # Connect signals
        self.open_btn.clicked.connect(self.open_pdf)
        self.save_btn.clicked.connect(self.save_pdf)
        
    def open_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open PDF File", "", "PDF Files (*.pdf)"
        )
        if file_path:
            # Here you'll add code to load the PDF
            self.statusBar.showMessage(f"Opened: {os.path.basename(file_path)}")
            self.save_btn.setEnabled(True)
    
    def save_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save PDF File", "", "PDF Files (*.pdf)"
        )
        if file_path:
            # Here you'll add code to save the PDF
            self.statusBar.showMessage(f"Saved as: {os.path.basename(file_path)}")