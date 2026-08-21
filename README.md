# Subscription Behavior Analysis

> **Analyzing customer renewal patterns using Python, SQL, and MySQL**

<br>

![Python](https://img.shields.io/badge/Python-Data%20Preparation-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Analysis-F29111?style=for-the-badge&logo=mysql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![VS%20Code](https://img.shields.io/badge/VS%20Code-Development-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)


---

**Goal:** Identify patterns in subscription renewals and determine which customer segments may require greater retention attention.

**Workflow:** Python → MySQL → SQL Analysis → Business Insights

---
## ⏬ Table of Contents

- [Project Overview](#-project-overview)
- [Business Questions](#-business-questions)
- [Tools & Technologies](#️-tools--technologies)
- [Data & Database Structure](#️-data--database-structure)
- [Python Data Preparation](#-python-data-preparation)
- [Analysis & SQL](#-analysis--sql)
- [Key Findings & Business Insights](#-key-findings--business-insights)
- [Business Recommendations](#-business-recommendations)

---
## Project Overview

This project analyzes customer subscription behavior to identify patterns associated with subscription renewals.

The analysis focuses on:

-  **Industry**
-  **Subscription type**
-  **Renewal trends over time**
-  **Economic conditions**

Python was used for data preparation and validation, while MySQL and SQL were used for database analysis.

### Project Goal

> Identify renewal patterns and determine which customer segments may require greater retention attention.

---
## Business Questions

| # | Question | Analysis Focus |
|---|---|---|
| 1 | Which industries have the highest and lowest renewal rates? |  Customer industry |
| 2 | Does subscription type appear to influence renewal behavior? |  Monthly vs. Yearly |
| 3 | How has renewal changed over time? | 2018–2022 trends |
| 4 | Do economic conditions appear to coincide with renewal changes? |  Inflation & GDP |

---
## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data preparation and validation |
| VS Code | Python development environment |
| MySQL | Database and SQL analysis |
| MySQL Workbench | Database management and query development |
| SQL | Aggregation, grouping, joins, and renewal analysis |

---
## Data & Database Structure

The project uses three related tables to analyze subscription behavior from both customer and economic perspectives.

### Database Structure

| Table | Description | Key Fields |
|---|---|---|
| `client_details` | Customer information and industry classification | `client_id`, `industry` |
| `subscription_records` | Subscription activity and renewal outcomes | `client_id`, `subscription_type`, `start_date`, `renewed` |
| `economic_indicators` | Quarterly economic conditions | `start_date`, `end_date`, `inflation_rate`, `gdp_growth_rate` |

### Table Relationships

The tables were connected using customer IDs and dates:

- `client_details` → `subscription_records`
  - Joined using `client_id`
  - Used to analyze renewal behavior by industry.

- `subscription_records` → `economic_indicators`
  - Matched subscription start dates to the corresponding economic quarter.
  - Used to explore renewal behavior alongside inflation and GDP growth.

### Key Fields

**`client_details`**

- `client_id` — unique customer identifier
- `industry` — customer's industry

**`subscription_records`**

- `client_id` — customer identifier
- `subscription_type` — Monthly or Yearly
- `start_date` — subscription start date
- `renewed` — renewal outcome (1 = renewed, 0 = not renewed)

**`economic_indicators`**

- `start_date` — beginning of economic quarter
- `end_date` — end of economic quarter
- `inflation_rate` — quarterly inflation rate
- `gdp_growth_rate` — quarterly GDP growth rate

---

## Python Data Preparation

Python and pandas were used in VS Code to prepare and validate the source datasets before loading them into MySQL.

The preparation included:

- Loading the CSV datasets
- Converting date fields
- Removing an unnecessary column
- Calculating subscription duration
- Checking data types, missing values, and duplicates

### Data Preparation

<img width="717" height="414" alt="Screenshot 2026-08-21 at 2 03 43 AM" src="https://github.com/user-attachments/assets/8e63542a-1925-4976-9276-c28cbc3981f0" />

### Data Validation

<img width="616" height="280" alt="Screenshot 2026-08-21 at 2 04 39 AM" src="https://github.com/user-attachments/assets/4506a458-4537-425c-981a-563181f6dc76" />

The validated datasets were then imported into MySQL Workbench for database analysis.

---
## Analysis & SQL

The SQL analysis was designed around the business questions defined above. 
Rather than analyzing every available field, I focused on a small set of metrics that could directly answer the subscription renewal questions.

### Key Metrics

- **Subscriptions** — total subscription records
- **Renewals** — number of subscriptions that were renewed
- **Renewal Rate** — percentage of subscriptions that were renewed

> **Renewal Rate = Renewals ÷ Subscriptions × 100**

### 1. Renewal Rate by Industry

**Business Question:**  
Which industries have the highest and lowest subscription renewal rates?

**Approach:**  
Joined `client_details` and `subscription_records` using `client_id` and calculated renewal rates by industry.

> **Key Observation:** Gaming had the highest renewal rate at **72.73%**, while Crypto had the lowest at **44.00%**.

<details>
<summary>View SQL Query</summary>

 <img width="813" height="224" alt="Screenshot 2026-08-21 at 1 06 16 AM" src="https://github.com/user-attachments/assets/040f5338-8010-47c4-91ea-0cab543cef05" />
</details>

<details>
<summary>View Results</summary>


<img width="813" height="230" alt="Screenshot 2026-08-21 at 1 09 28 AM" src="https://github.com/user-attachments/assets/c3e9ff4c-d5d4-4ea0-9323-e9e2bd2e8935" />

</details>

---

### 2. Renewal Rate by Subscription Type

**Business Question:**  
Does subscription type appear to influence renewal behavior?

**Approach:**  
Compared monthly and yearly renewal rates within each industry.

> ⭐ **Key Observation:** Monthly subscriptions generally showed higher renewal rates than yearly subscriptions. AI had the largest difference, with **83.33%** monthly renewal compared with **40.00%** yearly renewal.

<details>
<summary>View SQL Query</summary>

<img width="813" height="319" alt="Screenshot 2026-08-21 at 1 12 55 AM" src="https://github.com/user-attachments/assets/64725fe9-ca8f-461b-966b-dac776cdd7c9" />

</details>

<details>
<summary>View Results</summary>

<img width="813" height="255" alt="Screenshot 2026-08-21 at 1 14 34 AM" src="https://github.com/user-attachments/assets/b87d54af-88b4-4f73-a180-d33f3bd02b20" />

</details>

---

### 3. Renewal Rate Over Time

**Business Question:**  
How has subscription renewal changed over time?

**Approach:**  
Grouped subscription records by year from 2018–2022.

> ⭐ **Key Observation:** Renewal rates remained relatively stable, ranging from **50.00% to 58.82%**.

<details>
<summary>View SQL Query</summary>

<img width="813" height="325" alt="Screenshot 2026-08-21 at 1 18 39 AM" src="https://github.com/user-attachments/assets/8a1d168a-e4c4-44dc-8d75-46e622b032cb" />

</details>

<details>
<summary>View Results</summary>

<img width="813" height="235" alt="Screenshot 2026-08-21 at 1 19 06 AM" src="https://github.com/user-attachments/assets/fec4370a-3b82-48aa-ba62-202a30eba33b" />

</details>

---

### 4. Exploratory Analysis: Economic Conditions

**Business Question:**  
Do economic conditions appear to coincide with changes in renewal rates?

**Approach:**  
Matched subscription start dates to quarterly economic indicators and compared renewal rates with inflation and GDP growth.

> 🔎 **Key Observation:** Renewal rates varied across economic conditions, but the available data did not provide enough evidence to conclude that inflation or GDP growth directly influenced renewal behavior.

<details>
<summary>View SQL Query</summary>

<img width="813" height="321" alt="Screenshot 2026-08-21 at 1 21 28 AM" src="https://github.com/user-attachments/assets/63cbd556-dc0f-4aac-aed1-60fd451e6fc2" />

</details>

<details>
<summary>View Results</summary>

<img width="813" height="383" alt="Screenshot 2026-08-21 at 1 21 44 AM" src="https://github.com/user-attachments/assets/06daab96-427f-4f82-a168-34846ed11cce" />

</details>

---

##  Key Findings & Business Insights

The analysis identified several patterns in subscription renewal behavior.

###  Key Findings

| Finding | Result |
|---|---|
|  **Industry differences** | Gaming had the highest renewal rate at **72.73%**, while Crypto had the lowest at **44.00%**. |
|  **Subscription type** | Monthly subscriptions generally showed higher renewal rates than yearly subscriptions. |
|  **Renewal over time** | Renewal rates remained relatively stable between **50.00% and 58.82%** from 2018–2022. |
|  **Economic conditions** | No clear relationship between renewal rates and inflation or GDP growth was identified. |

###  Business Insights

These findings suggest that customer retention may vary more across **customer segments and subscription structures** than across broader economic conditions.

- **Prioritize lower-retention segments:** Industries with lower renewal rates may benefit from targeted retention strategies.
- **Evaluate subscription structure:** The higher renewal rates observed among monthly subscriptions suggest that subscription structure may be worth further investigation.
- **Monitor retention trends:** Relatively stable renewal rates indicate that changes in retention may require more granular customer-level analysis rather than relying solely on year-to-year trends.
- **Avoid overinterpreting economic factors:** The current analysis does not provide enough evidence to treat inflation or GDP growth as direct drivers of renewal behavior.

---
##  Business Recommendations

Based on the analysis, I would recommend the following actions:

### 1. Prioritize Lower-Renewal Industries

Industries with lower renewal rates, particularly Crypto and E-commerce, could be prioritized for additional retention analysis.

**Potential action:**  
Investigate whether these customers experience different onboarding, pricing, or engagement patterns and develop targeted retention strategies.

---

### 2. Investigate Subscription Structure

Monthly subscriptions generally showed higher renewal rates than yearly subscriptions.

**Potential action:**  
Further investigate why monthly customers renew at higher rates before changing pricing or subscription offerings. Consider testing different renewal incentives or engagement strategies.

---

### 3. Monitor Renewal Performance by Segment

Overall renewal rates remained relatively stable, but meaningful differences appeared across industries and subscription types.

**Potential action:**  
Track renewal rates by customer segment regularly rather than relying only on an overall company-wide renewal rate.

---

### 4.  Collect More Customer-Level Data

The current analysis identifies patterns but cannot explain *why* customers renew or do not renew.

**Potential action:**  
Collect additional information such as customer tenure, engagement, company size, location, pricing, and previous subscription history to identify specific drivers of renewal.
