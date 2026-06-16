# Sentro Ginhawa — Smart Barangay Health Kiosk

**STI College Caloocan — Thesis Project 2025**

A comprehensive health monitoring kiosk system designed for barangay health centers to provide free health screenings and record management for residents.

## Features

✅ **Resident Registration & Login**
- QR code scanning for instant login
- Name-based login with middle name support
- Age calculation from birthdate

✅ **Health Measurements**
- Body Temperature (°C)
- Blood Pressure (mmHg)
- Blood Glucose (mg/dL)
- Height & Weight with automatic BMI calculation
- Manual entry or sensor integration

✅ **Responsive Touch Keyboard**
- Automatically scales to any screen size (7" to 55")
- Large, accessible buttons for elderly users
- QWERTY layout with shift and backspace
- Smooth pop-up (no blinking)
- Themed to match the Sentro Ginhawa UI

✅ **Health Record Management**
- Save, print, and email health records
- Complete health history viewing
- PDF generation with QR codes
- Database persistence with SQLite

✅ **Admin Panel**
- Resident management
- Bulk deletion capabilities
- Health record editing
- Profile updates

✅ **Multi-language Support**
- English & Filipino (Tagalog)
- Toggle between languages anytime

✅ **Elderly-Friendly Design**
- Large fonts and buttons
- High contrast colors
- Soft, non-aggressive color palette
- Clear navigation
- Terms & Conditions display

## Installation

### Requirements
```bash
pip install pillow opencv-python reportlab numpy
```

Note: `tkinter` comes pre-installed with Python.

### Running the Application

```bash
python "sentro_ginhawa view history.py"
```

## File Structure

```
├── sentro_ginhawa view history.py    # Main application file
├── soft_keyboard.py                   # Responsive touch keyboard module
├── sentro_ginhawa.db                  # SQLite database (auto-created)
└── README.md                          # This file
```

## Keyboard Features

### Automatic Scaling
The keyboard automatically adapts to any screen size:

| Screen Size | Usage | Button Size |
|------------|-------|-------------|
| 7" | Portable kiosk | Small but accessible |
| 15" | Bedside display | Medium |
| 24" | Standard kiosk | Large |
| 32" | Wall-mounted | Extra large |
| 55" | Public display | Maximum |

### Color Scheme
Matches the Sentro Ginhawa UI:
- **Key Normal**: Light blue (#e8f0fe)
- **Key Hover**: Darker blue (#dbeafe)
- **Spacebar**: Deep blue (#1a56a0)
- **Backspace**: Red (#dc2626)
- **Header**: Navy (#1a3a6b)

### No Blinking
- Smooth transitions
- No flickering on keypress
- Persistent state during input
- Immediate response to touch

## Integration Guide

The keyboard is automatically integrated into all Entry fields in the application:

### How to Use
1. User taps any text input field
2. Keyboard automatically appears at the bottom of the screen
3. User selects characters using touch
4. Keyboard adapts to screen size
5. User taps "Hide" or clicks outside to dismiss

### Code Integration

```python
from soft_keyboard import SoftKeyboard

# Initialize keyboard with color scheme
keyboard = SoftKeyboard(root, color_scheme=C)

# Attach to any Entry widget
entry.bind("<FocusIn>", lambda e: keyboard.show(entry))
entry.bind("<FocusOut>", lambda e: keyboard.hide())
```

## Database Schema

### Residents Table
```sql
CREATE TABLE residents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age TEXT,
    gender TEXT,
    email TEXT,
    birthdate TEXT
);
```

### Health Records Table
```sql
CREATE TABLE health_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    temp TEXT,
    bp TEXT,
    glucose TEXT,
    height TEXT,
    weight TEXT,
    bmi TEXT,
    timestamp TEXT
);
```

## Email Configuration

To enable email sending, update the credentials in the main file:

```python
EMAIL_SENDER   = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use Gmail App Password
EMAIL_SMTP     = "smtp.gmail.com"
EMAIL_PORT     = 465
```

## Admin Access

**Default Admin Password**: `SentroG`

Click on the "SENTRO GINHAWA" title in the header bar 3 times rapidly to access the admin panel.

## Keyboard Specifications

### Button Layout
- **10 Number Keys**: 1-9, 0
- **10 QWERTY Keys**: Q-P (top row)
- **10 QWERTY Keys**: A-L, @ (middle row)
- **10 QWERTY Keys**: Z-M, ., /, - (bottom row)
- **Special Keys**: SHIFT, SPACE (expandable), BACKSPACE

### Features
- Auto-lowercase by default
- Shift toggles to uppercase
- Auto-deactivates shift after first letter
- Smooth hover effects
- No system keyboard interference
- Touch-optimized spacing

## Accessibility Features

✓ Large, high-contrast buttons
✓ Clear visual feedback on hover/press
✓ No time-based dismissal (elderly-friendly)
✓ Simple, intuitive layout
✓ Color-coded special functions
✓ Responsive to all screen sizes

## Troubleshooting

### Keyboard not appearing
- Ensure the Entry widget is in focus
- Check that `soft_keyboard.py` is in the same directory

### Buttons too small
- Keyboard automatically scales, but you can adjust in `soft_keyboard.py`:
  ```python
  kb_width = self.sc(1000)  # Adjust multiplier
  kb_height = self.sc(340)  # Adjust multiplier
  ```

### Keyboard appears in wrong position
- Verify monitor/screen size detection
- Keyboard positions at bottom-center by default

## Privacy & Security

This system includes comprehensive Data Privacy and Liability disclaimers compliant with:
- Data Privacy Act of 2012 (Republic Act No. 10173)
- Philippine Healthcare Standards
- Barangay Health Center Guidelines

## License & Terms

Developed for STI College Caloocan as a thesis project. Terms & Conditions are displayed to all users upon login.

## Support

For issues or feature requests, contact the development team at STI College Caloocan.

---

**Sentro Ginhawa** — *Smart Health, Empowered Communities* 🏥💙
