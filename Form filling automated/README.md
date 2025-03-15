# 🚀 Automated Form Filler using Selenium

This Python script automates form filling on the [DemoQA Practice Form](https://demoqa.com/automation-practice-form) using **Selenium WebDriver**. The script fills in required fields, selects a gender, and submits the form.

---

## 📌 Features

✅ Automatically fills in **First Name, Last Name, Email, Phone Number**
✅ **Selects Gender** (Male)
✅ Scrolls and submits the form using **JavaScript execution**
✅ **Bypasses CAPTCHA issues** (human-like wait times)
✅ Adds a **custom message**: `The automated form filler was created by S. Morozov`

---

## 🛠️ Requirements

Make sure you have the following installed:

- **Python 3.x** ([Download here](https://www.python.org/downloads/))
- **Google Chrome** (Latest version)
- **ChromeDriver** (Matching your Chrome version) ([Download here](https://sites.google.com/chromium.org/driver/))
- **Selenium** (Python package)

### Install Selenium:

```sh
pip install selenium
```

---

## 🚀 How to Use

### 2️⃣ Run the script:

```sh
python form_filler.py
```

The script will launch a **Chrome browser**, navigate to the form, fill it in, and submit it automatically.

---

## 🛠 Troubleshooting

- **Issue:** `selenium.common.exceptions.NoSuchElementException`
  - **Solution:** Ensure the website structure hasn't changed. Try increasing wait times.
- **Issue:** `ChromeDriver version mismatch`
  - **Solution:** Update ChromeDriver to match your Chrome version.
- **Issue:** CAPTCHA verification
  - **Solution:** This script uses human-like delays, but if issues persist, consider using an **AI solver**.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

### 💡 Author: **S. Morozov**

If you found this useful, feel free to ⭐ the repository!
