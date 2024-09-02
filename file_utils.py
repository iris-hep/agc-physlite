# Please refer to the https://opendata.cern.ch/record/80017 for file indexes of the PHYSLITE data. 
# The paths here are copied from the corresponding file indexes.
# The data used is Monte Carlo simulation.

# Please refer to the https://opendata.atlas.cern/docs/documentation/overview_data/data_research_2024/#metadata
# for info about metadata and the source from which the metadata.csv was downloaded.

import pandas as pd
import requests

df_metadata = pd.read_csv('metadata.csv')

MAX_NUM_OF_FILES = 1

def get_list_of_files(indexfile_url):
    
    response = requests.get(indexfile_url)
    
    # Raise an exception if there was an issue with the request
    response.raise_for_status()

    # Decode the content and split it into lines
    lines = response.text.splitlines()

    return lines[:MAX_NUM_OF_FILES]

# index file named mc20_13TeV_MC_PowhegPythia8EvtGen_A14_singletop_schan_lept_top_file_index.txt see https://opendata.cern.ch/record/80017
url_PowhegPythia8EvtGen_A14_singletop_schan_lept_top = "https://opendata.cern.ch/record/80017/files/mc20_13TeV_MC_PowhegPythia8EvtGen_A14_singletop_schan_lept_top_file_index.txt"
filenames_PowhegPythia8EvtGen_A14_singletop_schan_lept_top = get_list_of_files(url_PowhegPythia8EvtGen_A14_singletop_schan_lept_top)

metadata_PowhegPythia8EvtGen_A14_singletop_schan_lept_top = df_metadata[ df_metadata["physics_short"] == "PowhegPythia8EvtGen_A14_singletop_schan_lept_top" ]
metadata_PowhegPythia8EvtGen_A14_singletop_schan_lept_top = metadata_PowhegPythia8EvtGen_A14_singletop_schan_lept_top.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop_file_index.txt see https://opendata.cern.ch/record/80017
url_PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop = "https://opendata.cern.ch/record/80017/files/mc20_13TeV_MC_PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop_file_index.txt"
filenames_PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop = get_list_of_files(url_PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop)

metadata_PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop = df_metadata[ df_metadata["physics_short"] == "PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop" ]
metadata_PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop = metadata_PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_PhPy8EG_A14_tchan_BW50_lept_top_file_index.txt see https://opendata.cern.ch/record/80017
url_PhPy8EG_A14_tchan_BW50_lept_top = "https://opendata.cern.ch/record/80017/files/mc20_13TeV_MC_PhPy8EG_A14_tchan_BW50_lept_top_file_index.txt"
filenames_PhPy8EG_A14_tchan_BW50_lept_top = get_list_of_files(url_PhPy8EG_A14_tchan_BW50_lept_top)

metadata_PhPy8EG_A14_tchan_BW50_lept_top = df_metadata[ df_metadata["physics_short"] == "PhPy8EG_A14_tchan_BW50_lept_top" ]
metadata_PhPy8EG_A14_tchan_BW50_lept_top = metadata_PhPy8EG_A14_tchan_BW50_lept_top.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_PhPy8EG_A14_tchan_BW50_lept_antitop_file_index.txt see https://opendata.cern.ch/record/80017
url_PhPy8EG_A14_tchan_BW50_lept_antitop = "https://opendata.cern.ch/record/80017/files/mc20_13TeV_MC_PhPy8EG_A14_tchan_BW50_lept_antitop_file_index.txt"
filenames_PhPy8EG_A14_tchan_BW50_lept_antitop = get_list_of_files(url_PhPy8EG_A14_tchan_BW50_lept_antitop)

metadata_PhPy8EG_A14_tchan_BW50_lept_antitop = df_metadata[ df_metadata["physics_short"] == "PhPy8EG_A14_tchan_BW50_lept_antitop" ]
metadata_PhPy8EG_A14_tchan_BW50_lept_antitop = metadata_PhPy8EG_A14_tchan_BW50_lept_antitop.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_PhPy8EG_tW_dyn_DR_incl_antitop_file_index.txt see https://opendata.cern.ch/record/80017
url_PhPy8EG_tW_dyn_DR_incl_antitop = "https://opendata.cern.ch/record/80017/files/mc20_13TeV_MC_PhPy8EG_tW_dyn_DR_incl_antitop_file_index.txt"
filenames_PhPy8EG_tW_dyn_DR_incl_antitop = get_list_of_files(url_PhPy8EG_tW_dyn_DR_incl_antitop)

metadata_PhPy8EG_tW_dyn_DR_incl_antitop = df_metadata[ df_metadata["physics_short"] == "PhPy8EG_tW_dyn_DR_incl_antitop" ]
metadata_PhPy8EG_tW_dyn_DR_incl_antitop = metadata_PhPy8EG_tW_dyn_DR_incl_antitop.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_PhPy8EG_tW_dyn_DR_incl_top_file_index.txt see https://opendata.cern.ch/record/80017
url_PhPy8EG_tW_dyn_DR_incl_top = "https://opendata.cern.ch/record/80017/files/mc20_13TeV_MC_PhPy8EG_tW_dyn_DR_incl_top_file_index.txt"
filenames_PhPy8EG_tW_dyn_DR_incl_top = get_list_of_files(url_PhPy8EG_tW_dyn_DR_incl_top)

metadata_PhPy8EG_tW_dyn_DR_incl_top = df_metadata[ df_metadata["physics_short"] == "PhPy8EG_tW_dyn_DR_incl_top" ]
metadata_PhPy8EG_tW_dyn_DR_incl_top = metadata_PhPy8EG_tW_dyn_DR_incl_top.to_dict(orient='records')[0]

###############################################################################################################
## W and jets samples
###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wenu_maxHTpTV2_BFilter_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wenu_maxHTpTV2_BFilter = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wenu_maxHTpTV2_BFilter_file_index.txt"
filenames_Sh_2211_Wenu_maxHTpTV2_BFilter = get_list_of_files(url_Sh_2211_Wenu_maxHTpTV2_BFilter)

metadata_Sh_2211_Wenu_maxHTpTV2_BFilter = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wenu_maxHTpTV2_BFilter" ]
metadata_Sh_2211_Wenu_maxHTpTV2_BFilter = metadata_Sh_2211_Wenu_maxHTpTV2_BFilter.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wenu_maxHTpTV2_CFilterBVeto_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wenu_maxHTpTV2_CFilterBVeto = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wenu_maxHTpTV2_CFilterBVeto_file_index.txt"
filenames_Sh_2211_Wenu_maxHTpTV2_CFilterBVeto = get_list_of_files(url_Sh_2211_Wenu_maxHTpTV2_CFilterBVeto)

metadata_Sh_2211_Wenu_maxHTpTV2_CFilterBVeto = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wenu_maxHTpTV2_CFilterBVeto" ]
metadata_Sh_2211_Wenu_maxHTpTV2_CFilterBVeto = metadata_Sh_2211_Wenu_maxHTpTV2_CFilterBVeto.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wenu_maxHTpTV2_CVetoBVeto_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wenu_maxHTpTV2_CVetoBVeto = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wenu_maxHTpTV2_CVetoBVeto_file_index.txt"
filenames_Sh_2211_Wenu_maxHTpTV2_CVetoBVeto = get_list_of_files(url_Sh_2211_Wenu_maxHTpTV2_CVetoBVeto)

metadata_Sh_2211_Wenu_maxHTpTV2_CVetoBVeto = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wenu_maxHTpTV2_CVetoBVeto" ]
metadata_Sh_2211_Wenu_maxHTpTV2_CVetoBVeto = metadata_Sh_2211_Wenu_maxHTpTV2_CVetoBVeto.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wmunu_maxHTpTV2_BFilter_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wmunu_maxHTpTV2_BFilter = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wmunu_maxHTpTV2_BFilter_file_index.txt"
filenames_Sh_2211_Wmunu_maxHTpTV2_BFilter = get_list_of_files(url_Sh_2211_Wmunu_maxHTpTV2_BFilter)

metadata_Sh_2211_Wmunu_maxHTpTV2_BFilter = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wmunu_maxHTpTV2_BFilter" ]
metadata_Sh_2211_Wmunu_maxHTpTV2_BFilter = metadata_Sh_2211_Wmunu_maxHTpTV2_BFilter.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wmunu_maxHTpTV2_CFilterBVeto_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wmunu_maxHTpTV2_CFilterBVeto = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wmunu_maxHTpTV2_CFilterBVeto_file_index.txt"
filenames_Sh_2211_Wmunu_maxHTpTV2_CFilterBVeto = get_list_of_files(url_Sh_2211_Wmunu_maxHTpTV2_CFilterBVeto)

metadata_Sh_2211_Wmunu_maxHTpTV2_CFilterBVeto = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wmunu_maxHTpTV2_CFilterBVeto" ]
metadata_Sh_2211_Wmunu_maxHTpTV2_CFilterBVeto = metadata_Sh_2211_Wmunu_maxHTpTV2_CFilterBVeto.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wmunu_maxHTpTV2_CVetoBVeto_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wmunu_maxHTpTV2_CVetoBVeto = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wmunu_maxHTpTV2_CVetoBVeto_file_index.txt"
filenames_Sh_2211_Wmunu_maxHTpTV2_CVetoBVeto = get_list_of_files(url_Sh_2211_Wmunu_maxHTpTV2_CVetoBVeto)

metadata_Sh_2211_Wmunu_maxHTpTV2_CVetoBVeto = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wmunu_maxHTpTV2_CVetoBVeto" ]
metadata_Sh_2211_Wmunu_maxHTpTV2_CVetoBVeto = metadata_Sh_2211_Wmunu_maxHTpTV2_CVetoBVeto.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wtaunu_L_maxHTpTV2_BFilter_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wtaunu_L_maxHTpTV2_BFilter = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wtaunu_L_maxHTpTV2_BFilter_file_index.txt"
filenames_Sh_2211_Wtaunu_L_maxHTpTV2_BFilter = get_list_of_files(url_Sh_2211_Wtaunu_L_maxHTpTV2_BFilter)

metadata_Sh_2211_Wtaunu_L_maxHTpTV2_BFilter = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wtaunu_L_maxHTpTV2_BFilter" ]
metadata_Sh_2211_Wtaunu_L_maxHTpTV2_BFilter = metadata_Sh_2211_Wtaunu_L_maxHTpTV2_BFilter.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wtaunu_L_maxHTpTV2_CFilterBVeto_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wtaunu_L_maxHTpTV2_CFilterBVeto = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wtaunu_L_maxHTpTV2_CFilterBVeto_file_index.txt"
filenames_Sh_2211_Wtaunu_L_maxHTpTV2_CFilterBVeto = get_list_of_files(url_Sh_2211_Wtaunu_L_maxHTpTV2_CFilterBVeto)

metadata_Sh_2211_Wtaunu_L_maxHTpTV2_CFilterBVeto = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wtaunu_L_maxHTpTV2_CFilterBVeto" ]
metadata_Sh_2211_Wtaunu_L_maxHTpTV2_CFilterBVeto = metadata_Sh_2211_Wtaunu_L_maxHTpTV2_CFilterBVeto.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wtaunu_L_maxHTpTV2_CVetoBVeto_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wtaunu_L_maxHTpTV2_CVetoBVeto = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wtaunu_L_maxHTpTV2_CVetoBVeto_file_index.txt"
filenames_Sh_2211_Wtaunu_L_maxHTpTV2_CVetoBVeto = get_list_of_files(url_Sh_2211_Wtaunu_L_maxHTpTV2_CVetoBVeto)

metadata_Sh_2211_Wtaunu_L_maxHTpTV2_CVetoBVeto = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wtaunu_L_maxHTpTV2_CVetoBVeto" ]
metadata_Sh_2211_Wtaunu_L_maxHTpTV2_CVetoBVeto = metadata_Sh_2211_Wtaunu_L_maxHTpTV2_CVetoBVeto.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wtaunu_H_maxHTpTV2_BFilter_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wtaunu_H_maxHTpTV2_BFilter = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wtaunu_H_maxHTpTV2_BFilter_file_index.txt"
filenames_Sh_2211_Wtaunu_H_maxHTpTV2_BFilter = get_list_of_files(url_Sh_2211_Wtaunu_H_maxHTpTV2_BFilter)

metadata_Sh_2211_Wtaunu_H_maxHTpTV2_BFilter = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wtaunu_H_maxHTpTV2_BFilter" ]
metadata_Sh_2211_Wtaunu_H_maxHTpTV2_BFilter = metadata_Sh_2211_Wtaunu_H_maxHTpTV2_BFilter.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wtaunu_H_maxHTpTV2_CFilterBVeto_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wtaunu_H_maxHTpTV2_CFilterBVeto = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wtaunu_H_maxHTpTV2_CFilterBVeto_file_index.txt"
filenames_Sh_2211_Wtaunu_H_maxHTpTV2_CFilterBVeto = get_list_of_files(url_Sh_2211_Wtaunu_H_maxHTpTV2_CFilterBVeto)

metadata_Sh_2211_Wtaunu_H_maxHTpTV2_CFilterBVeto = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wtaunu_H_maxHTpTV2_CFilterBVeto" ]
metadata_Sh_2211_Wtaunu_H_maxHTpTV2_CFilterBVeto = metadata_Sh_2211_Wtaunu_H_maxHTpTV2_CFilterBVeto.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_Sh_2211_Wtaunu_H_maxHTpTV2_CVetoBVeto_file_index.txt see https://opendata.cern.ch/record/80010
url_Sh_2211_Wtaunu_H_maxHTpTV2_CVetoBVeto = "https://opendata.cern.ch/record/80010/files/mc20_13TeV_MC_Sh_2211_Wtaunu_H_maxHTpTV2_CVetoBVeto_file_index.txt"
filenames_Sh_2211_Wtaunu_H_maxHTpTV2_CVetoBVeto = get_list_of_files(url_Sh_2211_Wtaunu_H_maxHTpTV2_CVetoBVeto)

metadata_Sh_2211_Wtaunu_H_maxHTpTV2_CVetoBVeto = df_metadata[ df_metadata["physics_short"] == "Sh_2211_Wtaunu_H_maxHTpTV2_CVetoBVeto" ]
metadata_Sh_2211_Wtaunu_H_maxHTpTV2_CVetoBVeto = metadata_Sh_2211_Wtaunu_H_maxHTpTV2_CVetoBVeto.to_dict(orient='records')[0]

###############################################################################################################
## t-tbar samples
###############################################################################################################

# index file named mc20_13TeV_MC_PhPy8EG_A14_ttbar_hdamp258p75_nonallhad_file_index.txt see https://opendata.cern.ch/record/80017
url_PhPy8EG_A14_ttbar_hdamp258p75_nonallhad = "https://opendata.cern.ch/record/80017/files/mc20_13TeV_MC_PhPy8EG_A14_ttbar_hdamp258p75_nonallhad_file_index.txt"
filenames_PhPy8EG_A14_ttbar_hdamp258p75_nonallhad = get_list_of_files(url_PhPy8EG_A14_ttbar_hdamp258p75_nonallhad)

metadata_PhPy8EG_A14_ttbar_hdamp258p75_nonallhad = df_metadata[ df_metadata["physics_short"] == "PhPy8EG_A14_ttbar_hdamp258p75_nonallhad" ]
metadata_PhPy8EG_A14_ttbar_hdamp258p75_nonallhad = metadata_PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.to_dict(orient='records')[0]

###############################################################################################################

# index file named mc20_13TeV_MC_PowhegHerwig7EvtGen_tt_hdamp258p75_713_SingleLep_file_index.txt see https://opendata.cern.ch/record/80018
url_PowhegHerwig7EvtGen_tt_hdamp258p75_713_SingleLep = "https://opendata.cern.ch/record/80018/files/mc20_13TeV_MC_PowhegHerwig7EvtGen_tt_hdamp258p75_713_SingleLep_file_index.txt"
filenames_PowhegHerwig7EvtGen_tt_hdamp258p75_713_SingleLep = get_list_of_files(url_PowhegHerwig7EvtGen_tt_hdamp258p75_713_SingleLep)

metadata_PowhegHerwig7EvtGen_tt_hdamp258p75_713_SingleLep = df_metadata[ df_metadata["physics_short"] == "PowhegHerwig7EvtGen_tt_hdamp258p75_713_SingleLep" ]
metadata_PowhegHerwig7EvtGen_tt_hdamp258p75_713_SingleLep = metadata_PowhegHerwig7EvtGen_tt_hdamp258p75_713_SingleLep.to_dict(orient='records')[0]
