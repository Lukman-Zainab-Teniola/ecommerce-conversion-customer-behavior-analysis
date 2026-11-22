# Methodology

## Business question
What are sessions that end in a purchase doing differently from sessions that do not?

## Workflow
1. Import the session-level CSV.
2. Check dimensions, data types, null values, duplicate rows, and duplicate session IDs.
3. Define performance KPIs using DAX in Power BI.
4. Compare engagement (`pages_viewed`, `time_on_site_minutes`) by purchase status.
5. Calculate descriptive conversion rates across traffic source, device, product category, and country.
6. Build a dashboard and interpret results with business caveats.

## Definitions
- **Conversion rate:** purchases / total sessions.
- **Average order value:** total recorded revenue / number of purchases.
- **Cart additions:** sum of the `added_to_cart` indicator; this is not a verified funnel stage linked to subsequent purchases.
- **Segment conversion rate:** purchases in segment / sessions in segment.

## Interpretation and limitations
- One session does not necessarily equal one customer.
- Findings are observational and descriptive; no causal effect is established.
- Small percentage differences do not necessarily imply statistical significance.
- No logistic regression or significance testing was performed in the documented dashboard analysis.
- The dataset does not, by itself, establish a stepwise cart-to-purchase journey from aggregate totals.
