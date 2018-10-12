DROP PROCEDURE IF EXISTS raise_application_error;
DELIMETER $$
CREATE PROCEDURE raise_application_error(
  IN CODE INTEGER,
  IN MESSAGE VARCHAR(255)
)
SQL SECURITY INVOKER
DETERMINISTIC
BEGIN
  DECLARE ERROR CHAR(2);

  SELECT CODE, MESSAGE;
DELIMITER $$
CREATE TRIGGER tri_before_insert_couple 
BEFORE INSERT ON COUPLES FOR EACH ROW
BEGIN  
  IF (NEW.FK_id_type_inter_IT_CP <> 1 AND NEW.FK_id_lysis_LT_CP IS NOT NULL) THEN 
		SIGNAL SQLSTATE '02000' set message_text = 'It is not possible to insert a type not validated with a quality of lysis!';
  END IF;
END;
$$

DELIMITER $$
CREATE TRIGGER tri_before_update_couple 
BEFORE update ON COUPLES FOR EACH ROW
BEGIN  
  IF (NEW.FK_id_type_inter_IT_CP <> 1 AND NEW.FK_id_lysis_LT_CP IS NOT NULL) THEN
	SIGNAL SQLSTATE '02001' set message_text = 'It is not possible to update a type not validated with a quality of lysis!';
  END IF;
END;
$$


#-------------------------------- FOr COUPLES
DELIMITER $$
CREATE TRIGGER tri_before_insert_couple_pb_verification
BEFORE INSERT ON COUPLES FOR EACH ROW
BEGIN
	DECLARE type_bacterium INT;
	DECLARE type_phage INT;
	
	SET @type_bacterium := (SELECT FK_id_type_TY_OR FROM ORGANISMS WHERE id_organism_OR = NEW.FK_id_organism_bact_OR_CP);
	SET @type_phage := (SELECT FK_id_type_TY_OR FROM ORGANISMS WHERE id_organism_OR = NEW.FK_id_organism_phage_OR_CP);
	IF (@type_bacterium <> 1 or @type_phage <>2) THEN
		SIGNAL SQLSTATE '02002' set message_text = 'To insert a couple it is necessary one phage and one bacterium';
	END IF;
END;
$$

DELIMITER $$
CREATE TRIGGER tri_before_update_couple_pb_verification
BEFORE UPDATE ON COUPLES FOR EACH ROW
BEGIN
	DECLARE type_bacterium INT;
	DECLARE type_phage INT;
	
	SET @type_bacterium := (SELECT FK_id_type_TY_OR FROM ORGANISMS WHERE id_organism_OR = NEW.FK_id_organism_bact_OR_CP);
	SET @type_phage := (SELECT FK_id_type_TY_OR FROM ORGANISMS WHERE id_organism_OR = NEW.FK_id_organism_phage_OR_CP);
	IF (@type_bacterium <> 1 or @type_phage <>2) THEN
		SIGNAL SQLSTATE '02003' set message_text = 'To insert a couple it is necessary one phage and one bacterium';
	END IF;
END;
$$

DELIMITER $$
CREATE TRIGGER unic_keys_insert
BEFORE INSERT ON DATASET_CONTENT
FOR EACH ROW
begin
	DECLARE qty_couples integer;
    select count(*) into qty_couples FROM DATASET_CONTENT WHERE FK_id_couple_CP_DC = NEW.FK_id_couple_CP_DC and FK_id_dataset_DS_DC = NEW.FK_id_dataset_DS_DC;
    IF (qty_couples > 0) THEN
		SIGNAL SQLSTATE '02000' set message_text = 'You already put this couple in your dataset';
	END IF;
end;
$$
