# OrangeHRM Automation Testing

This repository contains automated test scripts for OrangeHRM Leave Management module using **Selenium with Python**.

## 📌 Test Flows Covered

1. ✅ Login functionality  
2. 📝 Apply Leave scenario  
3. ❌ Cancel Leave scenario  

---

## 🧰 Tech Stack

- **Language**: Python 3.13.5  
- **Automation Tool**: Selenium WebDriver  
- **Test Framework**: PyTest  
- **Reporting**: (Optional) Allure  
- **Traceability**: (Optional) [Qase.io](https://qase.io/) integration  
- **Design Pattern**: Page Object Model (POM)

---

## 📁 Project Structure

orangehrm-automation/
│
├── pages/ # Page Object files
│ ├── __init__.py
│ ├── login_page.py
│ └── leave_page.py
│
├── tests/ # Test cases
│ ├── __init__.py
│ ├── test_leave.py
│ └── test_login.py
│
├── utils/ # Base classes, config, utilities
│ ├── __init__.py
│ └── base_test.py
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/orangehrm-automation.git
cd orangehrm-automation

2. Create a Virtual Environment (Optional but Recommended)

    python -m venv venv
    source venv/bin/activate     # On Linux/Mac
    venv\Scripts\activate        # On Windows

3. Install Dependencies

    pip install -r requirements.txt

4. Run Tests

    pytest tests/

5. Generate Allure Report (Optional)

    pytest --alluredir=reports/
    allure serve reports/
    🔌 Qase Integration (Optional)
    To enable Qase integration:

    Create a project in Qase.io.

    Generate your API token.

    Set up your Qase reporter (like using qaseio/pytest-qase plugin).

    Update test case metadata with Qase IDs.

🧪 Sample Test Credentials
Username: Admin
Password: admin123

