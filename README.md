# E-Commerce Conversion & Customer Behavior Analysis

**Power BI | Data Analysis | KPI Reporting | Customer Behavior | Data Visualization**

A self-initiated data analytics portfolio project by **Zainab Teniola Lukman** (B.Sc. Statistics, University of Ilorin).

> **Business question:** What are website sessions that end in a purchase doing differently from sessions that do not?

![Power BI dashboard overview](assets/dashboard.png)

## Project overview

This project explores **2,500 e-commerce website sessions** recorded from **January 1, 2023 to December 30, 2024**. The aim is to establish overall conversion performance, compare engagement between purchasing and non-purchasing sessions, and describe variation by traffic source, device, product category, and country.

A **session** is a recorded website visit identified by `session_id`; it is **not necessarily a unique customer**. This is a descriptive and diagnostic analysis, **not a causal study**.

## Objectives

1. Measure website sessions, purchases, conversion rate, cart additions, revenue, and average order value.
2. Compare average pages viewed and time on site by purchase status.
3. Examine conversion patterns across traffic sources, devices, product categories, and countries.
4. Translate findings into business questions and recommendations for further investigation.

## Tools and techniques

- **Power BI:** interactive dashboard, filters, charts, and KPI cards.
- **DAX:** measures for sessions, purchases, conversion, revenue, and engagement.
- **Data validation:** missing values, duplicate records, unique session IDs, and field checks.
- **Descriptive statistics:** group averages, rates, and segment comparisons.
- **Python (reproducibility companion):** a separate script to verify summary results; **the original dashboard was built in Power BI**.

## Dataset

| Property | Detail |
|---|---|
| Source | Kaggle dataset: *Global E-Commerce User Behavior & Conversion Data* (dataset link/creator to be added after verification) |
| Observations | 2,500 sessions |
| Variables | 11 |
| Date range | 2023-01-01 to 2024-12-30 |
| Geographic coverage | 6 countries |
| Device categories | 3 |
| Traffic sources | 6 |
| Product categories | 6 |
| Missing values | 0 |
| Duplicate rows / duplicate session IDs | 0 / 0 |

The raw CSV is **not redistributed in this repository** pending confirmation of its source attribution and reuse terms. To reproduce the checks, obtain the dataset from its original Kaggle listing and save it as `data/ecommerce_user_behavior_sessions.csv`.

See [Data dictionary](docs/DATA_DICTIONARY.md) and [Methodology](docs/METHODOLOGY.md).

## Performance snapshot

| Metric | Result |
|---|---:|
| Total sessions | **2,500** |
| Recorded purchases | **928** |
| Conversion rate | **37.12%** |
| Sessions with recorded cart addition | **1,119** |
| Total recorded revenue | **$73,370.36** |
| Average order value | **$79.06** |

**Calculation:** Conversion rate = 928 / 2,500 × 100 = **37.12%**. Average order value = $73,370.36 / 928 = **$79.06**.

**Interpretation caution:** Cart additions (1,119) and purchases (928) are separate recorded totals. The two numbers alone do not demonstrate that 928 cart additions converted to purchases, nor establish a sequential funnel.

## Key findings

### 1. Purchasing sessions showed slightly higher average engagement

| Engagement measure | Purchased | Not purchased |
|---|---:|---:|
| Average pages viewed | 6.28 | 5.95 |
| Average time on site (minutes) | 6.09 | 6.00 |

The differences are modest (approximately **0.33 pages** and **0.10 minutes**). These are observed associations, **not evidence that additional browsing or time causes purchase**.

### 2. Conversion varied by traffic source

| Traffic source | Observed conversion rate |
|---|---:|
| Social Media | 38.86% |
| Referral | 38.03% |
| Paid Ads | 37.84% |
| Direct | 37.58% |
| Email | 35.61% |
| Organic Search | 34.76% |

Social Media recorded the highest observed rate **in this sample**; this does not establish it as universally superior.

### 3. Conversion varied by device

| Device | Observed conversion rate |
|---|---:|
| Desktop | 38.86% |
| Tablet | 36.67% |
| Mobile | 35.61% |

### 4. Product categories and countries showed variation

**Product category:** Books **40.71%**, Electronics **40.30%**, Fashion **37.20%**, Sports **36.19%**, Home **34.23%**, Beauty **33.67%**.

**Country:** India **40.86%**, Canada **38.65%**, Australia **38.23%**, UK **36.45%**, USA **34.78%**, Germany **33.65%**.

These are descriptive comparisons and should not be treated as adjusted effects.

## Dashboard

The dashboard contains KPI cards, a session/cart/purchase outcome overview, engagement comparisons by purchase status, and conversion rates by traffic source, device, and product category. Slicers support filtering by date, country, device, and traffic source.

![Full Power BI dashboard](assets/dashboard.png)

The source `.pbix` file is **not included** in this package. The dashboard screenshot documents the visual output; it is not an interactive Power BI file.

## Recommendations and next steps

- Monitor conversion alongside engagement rather than relying on traffic volume alone.
- Investigate where non-purchasing sessions disengage, using more detailed behavioral or event-level data if available.
- Compare source, device, category, and country performance with segment sizes and business context.
- As a future statistical extension, consider **logistic regression** because `purchased` is binary, to examine associations while considering several predictors together. **Logistic regression was proposed, not performed in this project.**

## Repository structure

```text
ecommerce-conversion-customer-behavior-analysis/
├── README.md
├── assets/
│   └── dashboard.png
├── presentation/
│   └── Ecommerce_Conversion_Analysis_Presentation.pptx
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── METHODOLOGY.md
│   └── POWER_BI_MEASURES.md
├── analysis/
│   └── verify_metrics.py
├── data/
│   └── README.md
├── requirements.txt
└── .gitignore
```

## Reproduce the metrics

After obtaining the original CSV and placing it in `data/`:

```bash
pip install -r requirements.txt
python analysis/verify_metrics.py data/ecommerce_user_behavior_sessions.csv
```

This prints the main KPIs, data-quality checks, and segment-level conversion rates. The companion script is provided for verification and is not presented as the original Power BI workflow.

## Presentation

See the [project presentation](presentation/Ecommerce_Conversion_Analysis_Presentation.pptx) for the business question, dashboard interpretation, key findings, and recommended next steps.

## Project scope and limitations

- Self-initiated portfolio project, **not commissioned client work**.
- Observational, session-level data; no causal conclusions or unique-customer counts.
- No hypothesis tests or multivariable regression reported as completed.
- Aggregate cart additions and purchases should not be interpreted as a verified sequential funnel.
- The Power BI dashboard screenshot is provided; the editable `.pbix` is not currently available.

## Author

**Zainab Teniola Lukman**  
Data Analytics | Power BI | Excel | Data Visualization  
B.Sc. Statistics, University of Ilorin
