# -*- coding: utf-8 -*-
"""
Created on Fri May 4 09:05:16 2018

@author: Diogo
"""

from SQL_obj_new.COGS_preview_sql_new import _COGS_preview_sql_new

class COGS_preview(object):
    """
    This class treat the COGS_preview object has it exists in COGS_preview table database
    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_cog_preview = -1, FK_id_prot_bact = -1, FK_id_prot_phage = -1, FK_id_interaction = -1, FK_id_couple = -1):
        """
        Constructor of the Organism object. All the parameters have a default value

        :param id_cog_preview: id cog preview - -1 if unknown
        :param FK_id_prot_bact: FK id protein of the bacterium - -1 if unknown
        :param FK_id_prot_phage: FK id protein of the phage - -1 if unknown
        :param FK_id_interaction: fk of the interaction - -1 if unknown
        :param FK_id_couple: fk of the interaction - -1 if unknown

        :param id_cog_preview: int - not required
        :param FK_id_prot_bact: int - required
        :param FK_id_prot_phage: int - required
        :param FK_id_interaction: int - required
        :param FK_id_couple: int - required
        """
        self.id_cog_preview = id_cog_preview
        self.FK_id_prot_bact = FK_id_prot_bact
        self.FK_id_prot_phage = FK_id_prot_phage
        self.FK_id_interaction = FK_id_interaction
        self.FK_id_couple = FK_id_couple


    def create_COGS_preview(self):
        """
        Insert a COG_preview in the database. 
        
        The id of the COG_preview is updated

        :return: id of the COG_preview
        :rtype: int
        """
        COG_id = None
        sqlObj = _COGS_preview_sql_new()

        COG_id = sqlObj.insert_COGS_preview(self.FK_id_prot_bact, self.FK_id_prot_phage, self.FK_id_interaction, self.FK_id_couple)
        self.id_cog_preview = COG_id
        return COG_id


    def get_COG_preview_grouped_by_couple_id(couple_id):
        """
        Return all COG scores grouped in a array given its couple id

        :param id_couple: id of the couple - -1 if unknown

        :type id_couple: text - required 

        :return: array of COGS_preview scores
        :rtype: array(COGS_preview_new)
        """
        list_scores_COG_preview = []
        sqlObj = _COGS_preview_sql_new()
        results = sqlObj.select_all_COGS_preview_grouped_by_couple_id(couple_id)
        for element in results:
            list_scores_COG_preview.append(COGS_preview(element[0], element[1], element[2], element[3], element[4]))
        return list_scores_COG_preview

    def get_all_COGS_preview_couple():
        """
        Return all COGS preview couple treated

        :return: array of COGS_preview scores
        :rtype: array(COGS_preview_new)
        """
        list_scores_COGS_fk_couple = []
        sqlObj = _COGS_preview_sql_new()
        results = sqlObj.select_all_COGS_preview()
        for element in results:
            list_scores_COGS_fk_couple.append(COGS_preview(element[0], element[1], element[2], element[3], element[4]))
        return list_scores_COGS_fk_couple

    def delete_COGS_preview_by_cogProt_id(id_prot_cog):
        """
        remove a COG_preview given fk of the cog of the protein
        :NOTE it verify for the phage and bacterium protein cog preview

        :param id_prot_cog: id of the protein

        :type id_prot_cog: int - required

        :return: COG_prot it removed
        :rtype: int
        """
        sqlObj = _COGS_preview_sql_new()
        id_couple = sqlObj.remove_COG_preview_by_prot_id(id_prot_cog)
        return id_couple

    def remove_COG_preview_fk_interaction_cog_source(id_cog_source):
        """
        remove a COG_preview given fk of the cog interaction

        :param id_cog_source: id of the cog interaction

        :type id_cog_source: int - required

        :return: COG_prot it removed
        :rtype: int
        """
        sqlObj = _COGS_preview_sql_new()
        id_couple = sqlObj.remove_COG_preview_by_interaction_id(id_cog_source)
        return id_couple

    def remove_COG_preview_by_its_id(id_cog_preview):
        """
        remove a COG_preview given fk of the cog interaction

        :param id_cog_preview: id of the cog preview

        :type id_cog_preview: int - required

        :return: COG_prot it removed
        :rtype: int
        """
        sqlObj = _COGS_preview_sql_new()
        id_couple = sqlObj.remove_COG_preview_by_id(id_cog_source)
        return id_couple

    def get_all_COGS_preview_couple_give_fk_cog_interaction(FK_id_interaction_cog_source_CSI_CPR):
        """
        Return the COGS preview couple treated with a given FK id interaction

        :return: array of COGS_preview scores
        :rtype: array(COGS_preview_new)
        """
        list_scores_COGS_fk_couple = []
        sqlObj = _COGS_preview_sql_new()
        results = sqlObj.get_COGS_ppi_preview_by_fk_id_interactions(FK_id_interaction_cog_source_CSI_CPR)
        for element in results:
            list_scores_COGS_fk_couple.append(COGS_preview(element[0], element[1], element[2], element[3], element[4]))
        return list_scores_COGS_fk_couple

    def verify_COG_preview_exist(self):
        """
        Verify if a given COG_preview exists

        :param FK_id_prot_bact: FK id protein of the bacterium - -1 if unknown
        :param FK_id_prot_phage: FK id protein of the phage - -1 if unknown
        :param FK_id_interaction: fk of the interaction - -1 if unknown
        :param FK_id_couple: fk of the interaction - -1 if unknown

        :param FK_id_prot_bact: int - required
        :param FK_id_prot_phage: int - required
        :param FK_id_interaction: int - required
        :param FK_id_couple: int - required
        """
        
        sqlObj = _COGS_preview_sql_new()
        results = sqlObj.verify_COG_preview_exits(self.FK_id_prot_bact, self.FK_id_prot_phage, self.FK_id_interaction, self.FK_id_couple)
        return results[0]

    def update_id_cog_interaction_by_cog_preview_id(id_cog_preview, FK_id_interaction):
        """
        update cog_preview interaction given id_cog_preview

        :param id_cog_preview: id cog_preview that it is necessary to update - -1 if unknown
        :param FK_id_interaction: FK id protein of the phage - -1 if unknown

        :param id_cog_preview: int - required
        :param FK_id_interaction: int - required
        """
        sqlObj = _COGS_preview_sql_new()
        results = sqlObj.update_id_interaction_cog_by_cog_preview_id(id_cog_preview, FK_id_interaction)
        
