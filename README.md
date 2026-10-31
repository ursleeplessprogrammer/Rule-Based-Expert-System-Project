
# Student Evaluation Expert System 🎓

<p align="center">
      <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

A Python-based Rule-Based Expert System designed to evaluate student academic conditions and determine their academic support status using predefined knowledge, inference rules, and uncertainty factors.

This project is a Python recreation of an existing ASP-based expert system back on my college days. Instead of relying on ASP, the system implements its reasoning mechanisms using Python, allowing the evaluation process to run through a desktop application with an Excel-based knowledge base.

The system analyzes student information, evaluates conditions through forward and backward chaining, and generates conclusions to determine whether a student is classified as **Aman (Safe)** or **Peringatan (Warning)**.

---

## 📌 Project Overview

The Student Evaluation Expert System is designed to assist in evaluating students' academic conditions based on several predefined criteria.

Rather than manually examining each student's academic information, the system uses a collection of rules and logical relationships to determine the appropriate evaluation status.

The application collects student information through an interactive questionnaire, processes the answers using an inference engine, and displays the resulting evaluation alongside its Working Memory Table.

The knowledge base is stored in an Excel workbook, making it possible to organize questions, answer choices, premises, and evaluation rules separately from the Python implementation.

### 🎯 Objectives

- Recreate an existing ASP-based expert system using Python.
- Implement rule-based reasoning through forward and backward chaining.
- Evaluate student academic conditions using predefined rules.
- Incorporate uncertainty factors into the reasoning process.
- Organize the knowledge base using an Excel database.
- Provide an interactive desktop interface for student evaluation.
- Display the reasoning process through a Working Memory Table.

---

## ✨ Features

- **Rule-Based Evaluation** – Evaluate student academic conditions using predefined IF-THEN rules.
- **Forward Chaining** – Process available information and evaluate rules to derive conclusions.
- **Backward Chaining** – Start from a target conclusion and investigate the premises required to establish it.
- **Uncertainty Factor** – Incorporate user confidence and rule uncertainty into the reasoning process.
- **Interactive Questionnaire** – Dynamically display questions based on the attributes required by the inference engine.
- **Working Memory Table** – Store and display collected answers, derived attributes, and their uncertainty values.
- **Excel-Based Knowledge Base** – Manage evaluation questions, choices, premises, and rules using Microsoft Excel.
- **Automatic Conclusion** – Generate an academic evaluation status based on the satisfied rules.
- **Desktop Application** – Provide a graphical interface using Python Tkinter.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application and inference engine |
| Tkinter | Desktop graphical user interface |
| Pandas | Excel data loading and manipulation |
| NumPy | Numerical and data-processing support |
| Excel (.xlsx) | Knowledge base and rule database |
| OpenPyXL | Excel workbook support through Pandas |

---

## 📂 Project Structure

```text
Rule-Based-Expert-System-Project/
│
├── database/
│   └── Evaluasi Mahasiswa.xlsx
│
├── main.py
├── forward.py
├── backward.py
├── uncertainty.py
├── test.py
│
└── README.md
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Main application implementing the student evaluation process, Tkinter interface, rule evaluation, and uncertainty handling. |
| `forward.py` | Implements the forward-chaining inference approach. |
| `backward.py` | Implements the backward-chaining inference approach. |
| `uncertainty.py` | Implements uncertainty-factor calculations during the inference process. |
| `test.py` | A separate Tkinter text-editor experiment. |
| `database/Evaluasi Mahasiswa.xlsx` | Excel workbook containing the knowledge base, evaluation rules, questions, and working memory structure. |

---

## 🧠 Expert System Architecture

The application uses a rule-based inference mechanism supported by a knowledge base and working memory.

### 1. Knowledge Base

The knowledge base contains the information required by the inference engine to evaluate student conditions.

It is maintained in `Evaluasi Mahasiswa.xlsx` and consists of seven worksheets:

| Worksheet | Description |
|---|---|
| `Premise Table` | Stores attributes, possible values, and premise clause statuses. |
| `Detail Rules` | Defines the relationships between evaluation rules and their premises. |
| `Questions` | Contains questions associated with student attributes and conclusions. |
| `Choices` | Stores the available answers for each question. |
| `Queue Table` | Provides a structure for storing queued attributes and rules. |
| `Working Memory Table` | Stores the attributes, values, and uncertainty factors used during evaluation. |
| `Rules` | Contains inference rules, conclusions, evaluation attributes, and rule uncertainty values. |

### 2. Working Memory

The Working Memory Table (WM) maintains information collected and inferred during the evaluation process.

It contains three primary attributes:

| Attribute | Description |
|---|---|
| `Attribute` | The student attribute being evaluated. |
| `Value` | The selected answer or inferred conclusion. |
| `Uncertainty` | The confidence value associated with the information. |

Examples of attributes stored in working memory include:

- `status_aktif`
- `masa_studi`
- `ips1`
- `ips2`
- `ipk`
- `beban_studi`
- `nilai_d`
- `masa_eval`
- `status_ips`
- `support`

The Working Memory Table is updated whenever the user provides an answer or the inference engine successfully derives a new conclusion.

### 3. Premise Clause Status

The system evaluates premises using three statuses:

| Status | Meaning | Description |
|---|---|---|
| `TU` | True | The premise matches the information stored in working memory. |
| `FA` | False | The premise does not match the information stored in working memory. |
| `FR` | Unresolved | The premise has not yet been evaluated. |

These statuses determine whether an inference rule can be executed, discarded, or requires additional information.

---

## ⚙️ Inference Mechanisms

The project implements two primary inference approaches: forward chaining and backward chaining.

### 1. Forward Chaining

Forward chaining is a data-driven inference technique.

The system begins with available information and evaluates rules based on the collected student answers.

The general process is:

1. Initialize the knowledge base and working memory.
2. Identify the attributes required by the evaluation rules.
3. Collect answers for unresolved attributes.
4. Update the premise statuses based on the collected information.
5. Evaluate rules against their corresponding premises.
6. Discard rules containing false premises.
7. Continue evaluating rules with unresolved premises.
8. Generate a conclusion when all required premises are satisfied.

**Inference workflow:**

```text
      Student Answers
             |
             v
      Working Memory
             |
             v
      Update Premises
             |
             v
       Evaluate Rules
             |
       +-----+-----+
       |     |     |
       v     v     v
      FA    FR    TU
       |     |     |
    Discard  Ask   Rule
    Rule   More  Satisfied
           Data    |
                   v
              Conclusion
```

### 2. Backward Chaining

Backward chaining is a goal-driven inference technique.

Instead of evaluating all available rules from the beginning, the system starts with a target conclusion and works backward to identify the premises necessary to establish that conclusion.

The general process is:

1. Define the target attribute or conclusion.
2. Identify rules capable of producing the target conclusion.
3. Examine the premises associated with each rule.
4. Determine whether the required attributes are already available in working memory.
5. Collect additional answers or derive intermediate conclusions when necessary.
6. Evaluate the rule after its premises have been resolved.
7. Generate the target conclusion when a rule is satisfied.

**Inference workflow:**

```text
       Target Goal
             |
             v
      Find Related Rules
             |
             v
      Examine Premises
             |
             v
   Are Premises Available?
             |
       +-----+-----+
       |           |
      No          Yes
       |           |
       v           v
  Resolve or    Evaluate
  Ask Questions   Rule
       |           |
       +-----+-----+
             |
             v
       Check Conditions
             |
             v
        Final Goal
```

### 3. Uncertainty Factor

The uncertainty mechanism allows the system to consider the user's confidence in the answers provided during the evaluation process.

Unlike a purely deterministic rule-based system, the uncertainty implementation stores a confidence value alongside each answer.

#### User Confidence

For each applicable question, the user provides:

- An answer selected from the available choices.
- A confidence value within the range of `0` to `1`.

Example:

| Attribute | Value | Uncertainty |
|---|---|---|
| `status_aktif` | iya | 1.0 |
| `masa_studi` | 5 | 0.9 |
| `ipk` | more_than_equals_2.00 | 0.8 |

These values are stored in the Working Memory Table.

#### Rule Uncertainty

Each evaluation rule contains an `Uncertainty_Rule` value in the Excel knowledge base.

When a rule is successfully satisfied, the implementation calculates its resulting uncertainty using:

\[
CF_{result} = CF_{premise(min)} \times CF_{rule}
\]

Where:

- `CF_result` = Resulting uncertainty of the conclusion.
- `CF_premise(min)` = Minimum uncertainty among the premises associated with the satisfied rule.
- `CF_rule` = Uncertainty value assigned to the rule.

**Example:**

```text
Minimum Premise Confidence = 0.80
Rule Uncertainty           = 1.00

Result = 0.80 × 1.00
       = 0.80
```

The resulting conclusion is therefore stored with an uncertainty value of `0.80`.

---

## 📚 Student Evaluation Criteria

The Excel knowledge base defines several attributes used to evaluate student academic conditions.

### Evaluation Attributes

| Attribute | Description |
|---|---|
| `status_aktif` | Student active status. |
| `masa_studi` | Current semester or study duration. |
| `ips1` | Grade Point Average (IPS) of the latest semester. |
| `ips2` | Grade Point Average (IPS) of the previous semester. |
| `ipk` | Cumulative Grade Point Average (IPK). |
| `beban_studi` | Number of completed study credits (SKS). |
| `nilai_d` | Number of credits with a D grade. |
| `masa_eval` | Intermediate evaluation result based on study duration. |
| `status_ips` | Intermediate evaluation result based on semester GPA. |
| `support` | Final student evaluation conclusion. |

### Available Evaluation Conclusions

The final evaluation attribute, `support`, contains two possible conclusions:

| Conclusion | Description |
|---|---|
| `aman` | Student is classified as safe based on the applicable evaluation rules. |
| `peringatan` | Student is classified as requiring attention or warning based on the applicable evaluation rules. |

The system uses intermediate conclusions such as `masa_eval` and `status_ips` to support the final evaluation.

---

## 🔄 System Workflow

The complete student evaluation process follows this general workflow:

```text
              START
                |
                v
       Load Excel Knowledge Base
                |
                v
        Initialize Working Memory
                |
                v
        Define Target: SUPPORT
                |
                v
       Start Inference Process
                |
                v
       Identify Required Attributes
                |
                v
       Collect Student Information
                |
                v
        Update Working Memory
                |
                v
        Update Premise Status
                |
                v
         Evaluate Inference Rules
                |
                v
      Derive Intermediate Conclusions
                |
                v
        Evaluate Final Conditions
                |
                v
         Calculate Uncertainty
                |
                v
         Generate Final Result
                |
                v
       Display Student Evaluation
                |
                v
               END
```

---

## 🚀 Getting Started

### Prerequisites

Before running the application, make sure you have:

- Python 3.9 or later.
- Microsoft Excel or another application capable of opening `.xlsx` files.
- Required Python libraries.
- Git (optional, for cloning the repository).

### 1. Clone the Repository

```bash
git clone https://github.com/ursleeplessprogrammer/Rule-Based-Expert-System-Project.git

cd Rule-Based-Expert-System-Project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pandas numpy openpyxl
```

`tkinter` is included with most standard Python installations. On some Linux distributions, it may need to be installed separately.

---

## ▶️ Running the Application

The project contains different Python implementations for the inference approaches.

Before running the scripts, ensure that the Excel workbook is located at:

```text
database/Evaluasi Mahasiswa.xlsx
```

### Main Application

```bash
python main.py
```

### Forward Chaining

```bash
python forward.py
```

### Backward Chaining

```bash
python backward.py
```

### Uncertainty Factor

```bash
python uncertainty.py
```

---

## ⚠️ Notes & Limitations

- The knowledge base is maintained in an Excel workbook.
- The application depends on the expected worksheet names and column structures.
- The Excel workbook must remain accessible through the relative path `database/Evaluasi Mahasiswa.xlsx`.
- Student evaluation results depend on the predefined rules and available answer choices.
- The uncertainty calculation uses the minimum premise confidence multiplied by the corresponding rule uncertainty.
- The current implementation uses a Tkinter desktop interface rather than a web-based application.
- The system is intended to assist with academic evaluation based on its configured rules, not to replace official academic decisions.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork this repository.
2. Create a new feature branch.

   ```bash
   git checkout -b feature/your-feature
   ```

3. Commit your changes.

   ```bash
   git commit -m "Add: your feature description"
   ```

4. Push your branch.

   ```bash
   git push origin feature/your-feature
   ```

5. Open a Pull Request.

---

## 📄 License

Please refer to the repository for applicable licensing information.

## 👨‍💻 Author

**ursleeplessprogrammer**

GitHub: [@ursleeplessprogrammer](https://github.com/ursleeplessprogrammer)

---

<p align="center">
  Built with Python 🐍
</p>
