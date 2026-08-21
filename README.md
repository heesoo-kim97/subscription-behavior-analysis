# subscription-behavior-analysis

## Project Overview
The project analyzes customer subscription behavior to understand what factors are associated with subscripiton renewals.

The analysis focuses on customer industry, subscription type, renewal trends over time, and broader economic conditions. The goal is to use data to identify differences in renewal behavior and translate those findings into actionable business insights.

I used Python in VS Code to prepare and validate the data, then imported the cleaned data into MySQL Workbench for SQL-based analysis and aggregation.

### Project Goal
- Identify patterns in subscription renewals and determine which customer segements may require greater retention attention.


## Business Questions

The analysis was structured around four questions:

1. **Which industries have the highest and lowest subscription renewal rates?**
   - Identify industries with stronger or weaker customer retention.

2. **Does subscription type affect renewal behavior?**
   - Compare renewal rates between monthly and yearly subscriptions.

3. **How has the renewal rate changed over time?**
   - Examine annual renewal trends from 2018 to 2022.

4. **Do economic conditions appear to coincide with changes in renewal rates?**
   - Explore whether inflation and GDP growth show any noticeable relationship with subscription renewals.


## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data preparation and validation |
| VS Code | Python development environment |
| MySQL | Database and SQL analysis |
| MySQL Workbench | Database management and query development |
| SQL | Aggregation, grouping, joins, and renewal analysis |


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

I grouped subscription records by customer industry and calculated the number of subscriptions, renewals, and overall renewal rate.

SQL:

<img width="813" height="224" alt="Screenshot 2026-08-21 at 1 06 16 AM" src="https://github.com/user-attachments/assets/040f5338-8010-47c4-91ea-0cab543cef05" />

Results:

<img width="813" height="230" alt="Screenshot 2026-08-21 at 1 09 28 AM" src="https://github.com/user-attachments/assets/c3e9ff4c-d5d4-4ea0-9323-e9e2bd2e8935" />


Key Observation: Gaming had the highest renewal rate at 72.73%, while Crypto had the lowest at 44.00%.


### 2. Renewal Rate by Subscription Type

**Business Question:**  
Does subscription type appear to influence renewal behavior?

I compared monthly and yearly subscriptions within each industry to identify differences in renewal rates.

SQL:

<img width="813" height="319" alt="Screenshot 2026-08-21 at 1 12 55 AM" src="https://github.com/user-attachments/assets/64725fe9-ca8f-461b-966b-dac776cdd7c9" />

Results:

<img width="813" height="255" alt="Screenshot 2026-08-21 at 1 14 34 AM" src="https://github.com/user-attachments/assets/b87d54af-88b4-4f73-a180-d33f3bd02b20" />


Key Observations:
- Monthly subscriptions generally showed higher renewal rates than yearly subscriptions.
- The differnece was particularly noticeable in AI, where monthly renewal was 83.33% compared with 40.00% for yearly subscriptions.
- Gaming also showed higher monthly renewal (80.00%) than yearly renewal (66.67%).
  

### 3. Renewal Rate Over Time

**Business Question:**  
How has subscription renewal changed over time?

I grouped subscription records by year to identify changes in renewal performance from 2018 through 2022.

SQL:

<img width="813" height="325" alt="Screenshot 2026-08-21 at 1 18 39 AM" src="https://github.com/user-attachments/assets/8a1d168a-e4c4-44dc-8d75-46e622b032cb" />

Results:

<img width="813" height="235" alt="Screenshot 2026-08-21 at 1 19 06 AM" src="https://github.com/user-attachments/assets/fec4370a-3b82-48aa-ba62-202a30eba33b" />


Key Observation: Renewal rates remained relatively stable, ranging from 50.00% to 58.82% during the five-year period.


### 4. Exploratory Analysis: Economic Conditions

**Business Question:**  
Do economic conditions appear to coincide with changes in renewal rates?

I joined subscription records to quarterly economic indicators using subscription start dates and compared renewal rates with inflation and GDP growth.

SQL:

<img width="813" height="321" alt="Screenshot 2026-08-21 at 1 21 28 AM" src="https://github.com/user-attachments/assets/63cbd556-dc0f-4aac-aed1-60fd451e6fc2" />

Results:

<img width="813" height="383" alt="Screenshot 2026-08-21 at 1 21 44 AM" src="https://github.com/user-attachments/assets/06daab96-427f-4f82-a168-34846ed11cce" />


Key Observation: Renewal rates varied across different economic conditions, but the available data does not provide enough evidence to conclude that inflation or GDP growth directly influenced renewal behavior.

## Key Findings
## Business Insights
## Project Workflow
## Future Improvements
