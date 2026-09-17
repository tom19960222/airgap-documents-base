---
collection: "opensearch"
version: "2.19"
title: "Metadata Queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/sql/sql/metadata.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/sql/sql/metadata.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/sql/sql/metadata/"
canonical_url: "https://docs.opensearch.org/latest/sql-and-ppl/sql/metadata/"
canonical_route: "/sql-and-ppl/sql/metadata/"
redirect_from: ["/search-plugins/sql/metadata/","/sql-and-ppl/sql/metadata/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "SQL and PPL"
layout: "default"
nav_order: 9
parent: "SQL"
---
# Metadata queries

To see basic metadata about your indexes, use the `SHOW` and `DESCRIBE` commands.

### Syntax

Rule `showStatement`:

![showStatement](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/showStatement.png)

Rule `showFilter`:

![showFilter](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/showFilter.png)

### Example 1: See metadata for indexes

To see metadata for indexes that match a specific pattern, use the `SHOW` command.
Use the wildcard `%` to match all indexes:

```sql
SHOW TABLES LIKE %
```

| TABLE_CAT | TABLE_SCHEM | TABLE_NAME | TABLE_TYPE | REMARKS | TYPE_CAT | TYPE_SCHEM | TYPE_NAME | SELF_REFERENCING_COL_NAME | REF_GENERATION
:--- | :---
docker-cluster | null | accounts | BASE TABLE | null | null | null | null | null | null
docker-cluster  | null | employees_nested | BASE TABLE | null | null | null | null | null | null

### Example 2: See metadata for a specific index

To see metadata for an index name with a prefix of `acc`:

```sql
SHOW TABLES LIKE acc%
```

| TABLE_CAT | TABLE_SCHEM | TABLE_NAME | TABLE_TYPE | REMARKS | TYPE_CAT | TYPE_SCHEM | TYPE_NAME | SELF_REFERENCING_COL_NAME | REF_GENERATION
:--- | :---
docker-cluster | null | accounts | BASE TABLE | null | null | null | null | null | null

### Example 3: See metadata for fields

To see metadata for field names that match a specific pattern, use the `DESCRIBE` command:

```sql
DESCRIBE TABLES LIKE accounts
```

| TABLE_CAT | TABLE_SCHEM | TABLE_NAME | COLUMN_NAME | DATA_TYPE | TYPE_NAME | COLUMN_SIZE | BUFFER_LENGTH | DECIMAL_DIGITS | NUM_PREC_RADIX | NULLABLE | REMARKS | COLUMN_DEF | SQL_DATA_TYPE | SQL_DATETIME_SUB | CHAR_OCTET_LENGTH | ORDINAL_POSITION | IS_NULLABLE | SCOPE_CATALOG | SCOPE_SCHEMA | SCOPE_TABLE | SOURCE_DATA_TYPE | IS_AUTOINCREMENT | IS_GENERATEDCOLUMN
:--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---
docker-cluster | null | accounts | account_number | null | long | null | null | null | 10 | 2 | null | null | null | null | null | 1 |  | null | null | null | null | NO |
docker-cluster | null | accounts | firstname | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 2 |  | null | null | null | null | NO |
docker-cluster | null | accounts | address | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 3 |  | null | null | null | null | NO |
docker-cluster | null | accounts | balance | null | long | null | null | null | 10 | 2 | null | null | null | null | null | 4 |  | null | null | null | null | NO |
docker-cluster | null | accounts | gender | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 5 |  | null | null | null | null | NO |
docker-cluster | null | accounts | city | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 6 |  | null | null | null | null | NO |
docker-cluster | null | accounts | employer | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 7 |  | null | null | null | null | NO |
docker-cluster | null | accounts | state | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 8 |  | null | null | null | null | NO |
docker-cluster | null | accounts | age | null | long | null | null | null | 10 | 2 | null | null | null | null | null | 9 |  | null | null | null | null | NO |
docker-cluster | null | accounts | email | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 10 |  | null | null | null | null | NO |
docker-cluster | null | accounts | lastname | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 11 |  | null | null | null | null | NO |
