-- This script creates an index on the first letter of the name field.
CREATE INDEX idx_name_first ON names (name(1));
