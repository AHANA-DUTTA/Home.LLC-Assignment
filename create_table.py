properties = """CREATE TABLE IF NOT EXISTS properties (
  id SERIAL PRIMARY KEY,
  property_title VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  reviewed_status VARCHAR(255),
  most_recent_status VARCHAR(255),
  source VARCHAR(100),
  market VARCHAR(100),
  occupancy VARCHAR(5),
  flood VARCHAR(100),
  street_address VARCHAR(255),
  city VARCHAR(100),
  state CHAR(2),
  zip CHAR(10),
  property_type VARCHAR(50),
  highway VARCHAR(50),
  train VARCHAR(50),
  tax_rate NUMERIC(5,2),
  sqft_basement INTEGER,
  htw VARCHAR(5),
  pool VARCHAR(5),
  commercial VARCHAR(5),
  water VARCHAR(50),
  sewage VARCHAR(50),
  year_built INTEGER,
  sqft_mu INTEGER,
  sqft_total INTEGER,
  parking VARCHAR(50),
  bed INTEGER,
  bath NUMERIC(4,1),
  BasementYesNo VARCHAR(5),
  layout VARCHAR(50),
  net_yield NUMERIC(5,2),
  irr NUMERIC(5,2),
  rent_restricted VARCHAR(5),
  neighborhood_rating INTEGER,
  latitude DOUBLE PRECISION,
  longitude DOUBLE PRECISION,
  subdivision VARCHAR(100),
  taxes NUMERIC(12,2),
  selling_reason VARCHAR(255),
  seller_retained_broker VARCHAR(255),
  final_reviewer VARCHAR(100),
  school_average NUMERIC(4,2)
);"""

valuations = """CREATE TABLE IF NOT EXISTS valuations (
  id SERIAL PRIMARY KEY,
  property_title VARCHAR(255) NOT NULL REFERENCES properties(property_title),
  list_price NUMERIC(12,2),
  previous_rent NUMERIC(10,2),
  zestimate NUMERIC(12,2),
  expected_rent NUMERIC(10,2),
  rent_zestimate NUMERIC(10,2),
  arv NUMERIC(12,2),
  redfin_value NUMERIC(12,2),
  low_fmr NUMERIC(10,2),
  high_fmr NUMERIC(10,2)
);"""

hoa = """CREATE TABLE IF NOT EXISTS hoa (
  id SERIAL PRIMARY KEY,
  property_title VARCHAR(255) NOT NULL REFERENCES properties(property_title),
  hoa NUMERIC(10,2),
  hoa_flag VARCHAR(5)
);"""

rehab = """CREATE TABLE IF NOT EXISTS rehab (
  id SERIAL PRIMARY KEY,
  property_title VARCHAR(255) NOT NULL REFERENCES properties(property_title),
  underwriting_rehab NUMERIC(12,2),
  rehab_calculation NUMERIC(12,2),
  paint VARCHAR(5),
  flooring_flag VARCHAR(5),
  foundation_flag VARCHAR(5),
  roof_flag VARCHAR(5),
  hvac_flag VARCHAR(5),
  kitchen_flag VARCHAR(5),
  bathroom_flag VARCHAR(5),
  appliances_flag VARCHAR(5),
  windows_flag VARCHAR(5),
  landscaping_flag VARCHAR(5),
  trashout_flag VARCHAR(5)
);"""


final_properties = """CREATE TABLE IF NOT EXISTS final_properties (
  id SERIAL PRIMARY KEY,
  property_title VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  reviewed_status VARCHAR(255),
  most_recent_status VARCHAR(255),
  source VARCHAR(100),
  market VARCHAR(100),
  occupancy VARCHAR(5),
  flood VARCHAR(100),
  street_address VARCHAR(255),
  city VARCHAR(100),
  state CHAR(2),
  zip CHAR(10),
  property_type VARCHAR(50),
  highway VARCHAR(50),
  train VARCHAR(50),
  tax_rate NUMERIC(5,2),
  sqft_basement INTEGER,
  htw VARCHAR(5),
  pool VARCHAR(5),
  commercial VARCHAR(5),
  water VARCHAR(50),
  sewage VARCHAR(50),
  year_built INTEGER,
  sqft_mu INTEGER,
  sqft_total INTEGER,
  parking VARCHAR(50),
  bed INTEGER,
  bath NUMERIC(4,1),
  BasementYesNo VARCHAR(5),
  layout VARCHAR(50),
  net_yield NUMERIC(5,2),
  irr NUMERIC(5,2),
  rent_restricted VARCHAR(5),
  neighborhood_rating INTEGER,
  latitude DOUBLE PRECISION,
  longitude DOUBLE PRECISION,
  subdivision VARCHAR(100),
  taxes NUMERIC(12,2),
  selling_reason VARCHAR(255),
  seller_retained_broker VARCHAR(255),
  final_reviewer VARCHAR(100),
  school_average NUMERIC(4,2)
  list_price NUMERIC(12,2),
  previous_rent NUMERIC(10,2),
  zestimate NUMERIC(12,2),
  expected_rent NUMERIC(10,2),
  rent_zestimate NUMERIC(10,2),
  arv NUMERIC(12,2),
  redfin_value NUMERIC(12,2),
  low_fmr NUMERIC(10,2),
  high_fmr NUMERIC(10,2)
  hoa NUMERIC(10,2),
  hoa_flag VARCHAR(5)
  underwriting_rehab NUMERIC(12,2),
  rehab_calculation NUMERIC(12,2),
  paint VARCHAR(5),
  flooring_flag VARCHAR(5),
  foundation_flag VARCHAR(5),
  roof_flag VARCHAR(5),
  hvac_flag VARCHAR(5),
  kitchen_flag VARCHAR(5),
  bathroom_flag VARCHAR(5),
  appliances_flag VARCHAR(5),
  windows_flag VARCHAR(5),
  landscaping_flag VARCHAR(5),
  trashout_flag VARCHAR(5)
);"""