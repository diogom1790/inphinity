/*before insert or update */
/* This code verifiy that each protein is part of its organism according the couple*/
declare 
	id_bact_orga integer;
	id_phage_orga integer;
	id_bact_orga_cp integer;
	id_phage_orga_cp integer;
	
	begin
        id_bact_orga_cp := (SELECT FK_id_organism_bact_OR_CP from COUPLES WHERE id_couple_CP = New.FK_couple_CP_PCP);
        id_phage_orga_cp := (SELECT FK_id_organism_phage_OR_CP from COUPLES WHERE id_couple_CP = New.FK_couple_CP_PCP);
		
        id_bact_orga := (SELECT FK_id_organism_OR_GE from GENES WHERE FK_id_protein_PT_GE = New.FK_prot_bact_PT_PCP);
        id_phage_orga := (SELECT FK_id_organism_OR_GE from GENES WHERE FK_id_protein_PT_GE = New.FK_prot_phage_PT_PCP);
		
		if (id_bact_orga <> id_bact_orga_cp) THEN
			RAISE EXCEPTION 'The protein is not part of the bacterium in the couple';
		end if;
		
        if (id_phage_orga <> id_phage_orga_cp) THEN
			RAISE EXCEPTION  'The protein is not part of the bacterium in the couple';
		end if;
		return new;
	end


