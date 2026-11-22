# Data dictionary

Each row represents one recorded website session.

| Column | Meaning |
|---|---|
| `session_id` | Session identifier; not proof of a unique customer |
| `visit_date` | Date of session |
| `country` | Country assigned to session |
| `device_type` | Device category (Desktop, Mobile, Tablet) |
| `traffic_source` | Acquisition/traffic source |
| `product_category_viewed` | Product category viewed in the session |
| `pages_viewed` | Number of pages viewed in the session |
| `time_on_site_minutes` | Time on site in minutes |
| `added_to_cart` | Binary indicator (1 = recorded cart addition, 0 = none recorded) |
| `purchased` | Binary indicator (1 = recorded purchase, 0 = no purchase recorded) |
| `order_value_usd` | Recorded order value in US dollars |

The dataset has 2,500 rows and 11 columns, with no missing values or duplicate session IDs in the supplied copy.
