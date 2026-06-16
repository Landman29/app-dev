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
- Automatically scales to any screen size
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
pip install tkinter pillow opencv-python reportlab numpy
```

### Running the Application

```bash
python sentro_ginhawa\ view\ history.py
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
- **24" Touchscreen**: Large, accessible buttons
- **32" Kiosk Display**: Full utilization of space
- **15" Portable**: Compact but usable layout

### Color Scheme
Matches the Sentro Ginhawa UI:
- **Key Normal**: Light blue (#e8f0fe)
- **Key Hover**: Darker blue (#dbeafe)
- **Spacebar**: Deep blue (#1a56a0)
- **Backspace**: Red (#dc2626)

### No Blinking
- Smooth transitions
- No flickering on keypress
- Persistent state during input

## Integration

The keyboard is automatically attached to all Entry fields:

```python
from soft_keyboard import SoftKeyboard

# Initialize keyboard
keyboard = SoftKeyboard(root, color_scheme=C)

# Show keyboard on entry focus
entry.bind("<FocusIn>", lambda e: keyboard.show(entry))

# Hide keyboard on focus out
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

Click the title bar 3 times rapidly to access the admin panel.

## License & Terms

This system includes comprehensive Data Privacy and Liability disclaimers compliant with the Data Privacy Act of 2012 (Republic Act No. 10173).

## Support

For issues or feature requests, contact the development team at STI College Caloocan.

---

**Sentro Ginhawa** — *Smart Health, Empowered Communities*
