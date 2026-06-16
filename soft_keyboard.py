"""
SENTRO GINHAWA — Soft Keyboard Module
Responsive on-screen keyboard for touch-enabled kiosks
Designed for elderly users with large, accessible buttons
"""

import tkinter as tk
from tkinter import font as tkfont

class SoftKeyboard:
    """
    Responsive soft keyboard for touchscreen kiosks.
    - Automatically scales to any screen size
    - Themed to match the Sentro Ginhawa UI
    - No blinking transitions
    - Can be invoked on any Entry widget
    """
    
    def __init__(self, parent, color_scheme=None):
        """
        Initialize the soft keyboard.
        
        Args:
            parent: Root Tkinter window
            color_scheme: Dictionary with color definitions (uses defaults if None)
        """
        self.parent = parent
        self.active_entry = None
        self.keyboard_window = None
        
        # Color scheme (matches Sentro Ginhawa theme)
        self.colors = color_scheme or {
            "bg": "#f0f4f8",
            "surface": "#ffffff",
            "header": "#1a3a6b",
            "accent": "#1a56a0",
            "accent_light": "#dbeafe",
            "key_normal": "#e8f0fe",
            "key_hover": "#dbeafe",
            "key_press": "#1a56a0",
            "text": "#0f172a",
            "text_light": "#475569",
            "border": "#e2e8f0",
            "spacebar": "#1a56a0",
            "delete": "#dc2626",
            "delete_hover": "#b91c1c",
        }
        
        # Layout: QWERTY with support for numbers and special characters
        self.layout = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '@'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '.', '/', '-'],
        ]
        
        self.shift_active = False
        self.key_buttons = {}
        self.shift_button = None
        
    def get_scale_factor(self):
        """Calculate scale factor based on screen size."""
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        scale = max(0.7, min(sw / 1100, sh / 690))
        return scale
    
    def sc(self, value):
        """Scale value based on screen size."""
        return max(1, int(round(value * self.get_scale_factor())))
    
    def sf(self, size):
        """Scale font size based on screen size."""
        return max(9, int(round(size * self.get_scale_factor())))
    
    def show(self, entry_widget):
        """Show the keyboard attached to an Entry widget."""
        self.active_entry = entry_widget
        if self.keyboard_window and self.keyboard_window.winfo_exists():
            self.keyboard_window.lift()
            return
        self._create_keyboard_window()
    
    def _create_keyboard_window(self):
        """Create and display the keyboard window."""
        self.keyboard_window = tk.Toplevel(self.parent)
        self.keyboard_window.title("Input Keyboard")
        self.keyboard_window.attributes('-type', 'splash')
        
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        kb_width = self.sc(1000)
        kb_height = self.sc(340)
        kb_x = max(0, (sw - kb_width) // 2)
        kb_y = max(0, sh - kb_height - self.sc(60))
        
        self.keyboard_window.geometry(f"{kb_width}x{kb_height}+{kb_x}+{kb_y}")
        self.keyboard_window.resizable(False, False)
        self.keyboard_window.configure(bg=self.colors["bg"])
        self.keyboard_window.attributes('-topmost', True)
        self.keyboard_window.grab_set_global()
        
        main_frame = tk.Frame(
            self.keyboard_window,
            bg=self.colors["bg"],
            padx=self.sc(8),
            pady=self.sc(8)
        )
        main_frame.pack(fill="both", expand=True)
        
        # Header bar
        header = tk.Frame(main_frame, bg=self.colors["header"], height=self.sc(36))
        header.pack(fill="x", pady=(0, self.sc(8)))
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="⌨  Touch Keyboard",
            font=("Helvetica", self.sf(13), "bold"),
            bg=self.colors["header"],
            fg="white"
        ).pack(side="left", padx=self.sc(12), pady=self.sc(6))
        
        close_btn = tk.Button(
            header,
            text="✕ Hide",
            font=("Helvetica", self.sf(11), "bold"),
            bg=self.colors["delete"],
            fg="white",
            relief="flat",
            bd=0,
            padx=self.sc(12),
            pady=self.sc(4),
            cursor="hand2",
            command=self.hide
        )
        close_btn.pack(side="right", padx=self.sc(8), pady=self.sc(6))
        
        # Keyboard grid frame
        keyboard_frame = tk.Frame(main_frame, bg=self.colors["bg"])
        keyboard_frame.pack(fill="both", expand=True)
        self.key_buttons.clear()
        
        for row_idx, row_keys in enumerate(self.layout):
            row_frame = tk.Frame(keyboard_frame, bg=self.colors["bg"])
            row_frame.pack(fill="x", pady=self.sc(3))
            for key_idx, key in enumerate(row_keys):
                self._create_key_button(row_frame, key, row_idx, key_idx)
        
        # Bottom row: Shift, Space, Backspace
        bottom_frame = tk.Frame(keyboard_frame, bg=self.colors["bg"])
        bottom_frame.pack(fill="x", pady=(self.sc(6), 0))
        
        self.shift_button = self._create_special_button(
            bottom_frame, "⇧ SHIFT", self._toggle_shift, bg=self.colors["accent"]
        )
        self.shift_button.pack(side="left", padx=self.sc(2), fill="x", expand=False)
        
        spacebar = self._create_special_button(
            bottom_frame, "SPACE", lambda: self._key_press(" "), bg=self.colors["spacebar"]
        )
        spacebar.pack(side="left", padx=self.sc(2), fill="x", expand=True)
        
        backspace_btn = self._create_special_button(
            bottom_frame, "⌫ BACK", self._backspace, bg=self.colors["delete"]
        )
        backspace_btn.pack(side="left", padx=self.sc(2), fill="x", expand=False)
    
    def _create_key_button(self, parent, key, row_idx, col_idx):
        """Create a regular key button."""
        btn = tk.Button(
            parent,
            text=key,
            font=("Helvetica", self.sf(14), "bold"),
            bg=self.colors["key_normal"],
            fg=self.colors["text"],
            relief="flat",
            bd=0,
            padx=self.sc(8),
            pady=self.sc(10),
            cursor="hand2",
            command=lambda k=key: self._key_press(k),
            activebackground=self.colors["key_hover"],
            activeforeground=self.colors["text"]
        )
        btn.pack(side="left", padx=self.sc(2), fill="x", expand=True)
        btn.bind("<Enter>", lambda e, b=btn: self._on_key_hover(b))
        btn.bind("<Leave>", lambda e, b=btn: self._on_key_leave(b))
        self.key_buttons[key] = btn
        return btn
    
    def _create_special_button(self, parent, label, command, bg=None):
        """Create a special button (Shift, Space, Backspace)."""
        btn = tk.Button(
            parent,
            text=label,
            font=("Helvetica", self.sf(12), "bold"),
            bg=bg or self.colors["accent"],
            fg="white",
            relief="flat",
            bd=0,
            padx=self.sc(6),
            pady=self.sc(10),
            cursor="hand2",
            command=command,
            activebackground=self._dim(bg or self.colors["accent"]),
            activeforeground="white"
        )
        btn.bind("<Enter>", lambda e, b=btn, c=bg: self._on_special_hover(e, b, c))
        btn.bind("<Leave>", lambda e, b=btn, c=bg: self._on_special_leave(e, b, c))
        return btn
    
    def _on_key_hover(self, btn):
        """Handle key hover effect."""
        btn.configure(bg=self.colors["key_hover"], relief="raised")
    
    def _on_key_leave(self, btn):
        """Handle key leave effect."""
        btn.configure(bg=self.colors["key_normal"], relief="flat")
    
    def _on_special_hover(self, event, btn, color):
        """Handle special button hover."""
        btn.configure(bg=self._dim(color or self.colors["accent"]))
    
    def _on_special_leave(self, event, btn, color):
        """Handle special button leave."""
        btn.configure(bg=color or self.colors["accent"])
    
    @staticmethod
    def _dim(color):
        """Darken a hex color for hover effects."""
        r = color.lstrip('#')
        r, g, b = int(r[0:2], 16), int(r[2:4], 16), int(r[4:6], 16)
        return f'#{max(0, r-22):02x}{max(0, g-22):02x}{max(0, b-22):02x}'
    
    def _toggle_shift(self):
        """Toggle shift key state."""
        self.shift_active = not self.shift_active
        if self.shift_button:
            if self.shift_active:
                self.shift_button.configure(bg=self.colors["key_press"], fg="white")
            else:
                self.shift_button.configure(bg=self.colors["accent"], fg="white")
        for key, btn in self.key_buttons.items():
            display_text = key.upper() if self.shift_active else key.lower()
            btn.configure(text=display_text)
    
    def _key_press(self, key):
        """Handle key press - insert character into active entry."""
        if not self.active_entry or not self.active_entry.winfo_exists():
            return
        try:
            current_text = self.active_entry.get()
            cursor_pos = self.active_entry.index(tk.INSERT)
            insert_char = key.upper() if self.shift_active else key
            new_text = current_text[:cursor_pos] + insert_char + current_text[cursor_pos:]
            self.active_entry.delete(0, tk.END)
            self.active_entry.insert(0, new_text)
            self.active_entry.icursor(cursor_pos + 1)
            if self.shift_active and key.isalpha():
                self._toggle_shift()
            self.active_entry.event_generate("<<Change>>")
        except Exception as e:
            print(f"[SoftKeyboard] Error inserting character: {e}")
    
    def _backspace(self):
        """Handle backspace - delete previous character."""
        if not self.active_entry or not self.active_entry.winfo_exists():
            return
        try:
            current_text = self.active_entry.get()
            cursor_pos = self.active_entry.index(tk.INSERT)
            if cursor_pos > 0:
                new_text = current_text[:cursor_pos - 1] + current_text[cursor_pos:]
                self.active_entry.delete(0, tk.END)
                self.active_entry.insert(0, new_text)
                self.active_entry.icursor(cursor_pos - 1)
                self.active_entry.event_generate("<<Change>>")
        except Exception as e:
            print(f"[SoftKeyboard] Error on backspace: {e}")
    
    def hide(self):
        """Hide the keyboard."""
        if self.keyboard_window and self.keyboard_window.winfo_exists():
            self.keyboard_window.destroy()
            self.keyboard_window = None
        self.active_entry = None
    
    def toggle(self, entry_widget):
        """Toggle keyboard on/off."""
        if self.keyboard_window and self.keyboard_window.winfo_exists():
            self.hide()
        else:
            self.show(entry_widget)
