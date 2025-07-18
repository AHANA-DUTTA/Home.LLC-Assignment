# Home.LLC-Assignment

# Real Estate ETL Pipeline with MySQL & Docker Compose
This project implements an end-to-end ETL (Extract, Transform, Load) pipeline in Python that reads nested JSON real estate data and normalizes it, and loads it into a structured MySQL database using Docker Compose.

# Project Features
- **Extracts** data from structured JSON files
- **Transforms** nested and inconsistent fields into normalized relational tables
- **Loads** data into a MySQL database container via SQLAlchemy
- Containerized with **Docker Compose**
- Supports repeated batch loading with null handling and schema validation

Normalized into four tables:
- properties – Basic property info
- valuations – List price, rent estimates, ARVs
- hoa_fees – HOA costs and flags
- rehab_items – Rehab cost breakdowns and flags
- All foreign-key linked via property_title.


