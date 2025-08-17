CREATE OR REPLACE FUNCTION insert_schedule()
RETURNS TRIGGER AS $$
BEGIN
INSERT INTO schedule (id_profile) VALUES (NEW.id_profile);
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER create_schedule_trigger
AFTER INSERT ON profile
FOR EACH ROW
EXECUTE FUNCTION insert_schedule();