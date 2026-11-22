# Power BI DAX measures

These are the measures used in the project. Replace the table name if yours differs.

```dax
Total Sessions =
DISTINCTCOUNT('ecommerce_user_behavior_sessions'[session_id])

Cart Additions =
SUM('ecommerce_user_behavior_sessions'[added_to_cart])

Total Purchases =
SUM('ecommerce_user_behavior_sessions'[purchased])

Conversion Rate =
DIVIDE([Total Purchases], [Total Sessions])

Total Revenue =
SUM('ecommerce_user_behavior_sessions'[order_value_usd])

Average Order Value =
DIVIDE([Total Revenue], [Total Purchases])

Average Pages Viewed =
AVERAGE('ecommerce_user_behavior_sessions'[pages_viewed])

Average Time on Site =
AVERAGE('ecommerce_user_behavior_sessions'[time_on_site_minutes])
```

Calculated column:

```dax
Purchase Status =
IF(
    'ecommerce_user_behavior_sessions'[purchased] = 1,
    "Purchased",
    "Not Purchased"
)
```

Format `Conversion Rate` as a percentage (two decimals for 37.12%). Currency measures use USD.
