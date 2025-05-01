-- This script creates an index on the first letter of the name field, and the
-- score field.
CREATE INDEX idx_name_first_score ON names (name(1), score);
