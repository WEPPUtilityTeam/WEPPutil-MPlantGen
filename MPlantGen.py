import csv

dir = "out/"
fin = 'param_inputs.csv'
prefix = 'sen'
comment = "sensitivity analysis input"

with open(fin) as csvfile:
    reader = csv.DictReader(csvfile)
    print reader
    for r in reader:
        for k in r.keys():
            try:
                r[k] = float(r[k])
            except:
                pass
        p_call = "pln_{id:04d}".format(id = int(r['id']))
        i_call = "ini_{id:04d}".format(id = int(r['id']))
        r_call = "man_{id:04d}".format(id = int(r['id']))
        proj_call = "prj_{id:04d}".format(id = int(r['id']))
        op = open("{}/db/{}.db".format(dir,p_call), 'w')
        oi = open("{}/db/{}.db".format(dir,i_call), 'w')
        orot = open("{}/rot/{}.rot".format(dir,r_call), 'w')
        oprj = open("{}/prj/{}.prj".format(dir,proj_call), 'w')
        
        op.write("2004.1    0\n1\n")
        op.write("{}   0\n".format(p_call))
        op.write("test_{:04d}\n".format(int(r['id'])))
        op.write("test\n")
        op.write("(null)\n")
        op.write("{}\n".format(comment))
        op.write("{lu:.0f}\n{h_units}\n".format(**r))
        op.write("{canopy_cover} {canopy_param} {e_ratio} {temp} {resid_par} {gdd_em} {grazing_bio} {p_cut} {pct_canopy_sen} {p_diameter}\n".format(**r))
        op.write("{pct_to_max_lai} {pct_biomass_sen} {rad_coeff} {resid_adj} {dw_frict_fact} {gdd_season} {harvest} {canopy_max}\n".format(**r))
        op.write("{mfo_value:.0f}\n".format(**r))
        op.write("{decomp_above} {decomp_below} {temp_opt} {drought_tol} {p_space} {root_depth_max} {root_shoot} {root_mass_max} {sen_length} {temp_max_crit}\n".format(**r))
        op.write("{temp_min_crit} {lai_max} {yield_opt}".format(**r))




        oi.write("2004.1    2\n1\n")
        oi.write("{}   0\n".format(i_call))
        oi.write("{:04d}\n".format(int(r['id'])))
        oi.write("test\n")
        oi.write("(null)\n")
        oi.write("{}\n".format(comment))
        oi.write("{}\n".format(p_call))
        oi.write("{lu:.0f}\n".format(**r))
        oi.write("{bd} {cc_init} {days_harv} {days_till} {frost_init} {ir_cover_init}\n".format(bd = r['bd'], cc_init = r['cc_init'], days_till = r['days_till'], days_harv = r['days_harv'], frost_init = r['frost_init'], ir_cover_init = r['ir_cover_init']))
        oi.write("{mgmt:.0f}\n".format(mgmt = r['mgmt']))
        oi.write("{rain_till} {ridge_init} {r_cover_init} {rough_init} {rill_space}\n".format(**r))
        oi.write("{r_type:.0f}\n".format(r_type = r['r_type']))
        oi.write("{snow_d} {thaw_d} {sec_till_d} {pri_till_d} {ir_width}\n".format(**r))
        oi.write("{root_init} {res_sub}\n".format(**r))


        orot.write("Version = 98.7\nName = {id:04d}\nDescription {{\n}}\nColor = 0 128 0\nLandUse = 1\nInitialConditions = IniCropDef.{init} {{0.000000, 0}}".format(id = int(r['id']),init = i_call))
        
        
        
        
        
        man_str = "{}\{}.rot".format("Sensitivity",r_call)
        oprj.write("Version = 98.6\nName = default\nComments {{\nCreated by TOPAZ interface\n}}\nUnits = Metric\nLanduse = 1\nLength = 100\nProfile {{\nFile = \"default.slp\"\n}}\nClimate {{\nFile = \"Arizona\BLACK RIVER PUMPS AZ.cli\"\n}}\nSoil {{\nBreaks = 0\ndefault {{\nDistance = 100\nFile = \"OFE3\\baldy_high.sol\"\n}}\n}}\nManagement {{\nBreaks = 0\ndefault {{\nDistance = 100\nFile = \"{}\"\n}}\n}}\nRunOptions {{\nVersion = 1\nSoilLossOutputType = 1\nSoilLossOutputFile = AutoName\nPlotFile = AutoName\nEventFile = AutoName\nFinalSummaryFile = AutoName\nSimulationYears = 1\nSmallEventByPass = 1\n}}".format(man_str))
        
        
        op.close()
        oi.close()
        orot.close()
        oprj.close()

print "Complete... "













'''
# ~plant_db 

version = ' '
callable = ' '
plant_name = ' '
description = ' '
source = ' '
comment = ' '

#value dictionaries by type
p_dic = {'e_ratio': ' ','gdd_em': ' ','gdd_season': ' ','p_space': ' ','p_diameter': ' ','p_cut': ' ','harvest': ' ',
              'temp': ' ','temp_opt': ' ','temp_max_crit': ' ','temp_min_crit': ' ','rad_coeff': ' ', 'canopy_cover': ' ',
              'canopy_param': ' ','canopy_max': ' ','lai_max': ' ','root_depth_max': ' ','root_shoot': ' ','root_mass_max': ' ',
              'pct_to_max_lai': ' ','sen_length': ' ','pct_canopy_sen': ' ','pct_biomass_sen': ' ',
              'resid_par': ' ','resid_adj': ' ','decomp_above': ' ','decomp_below': ' ','mfo_value': ' ',
              'drought_tol': 'asdf ','grazing_bio': ' ','dw_frict_fact': ' ','h_units': ' ','yield_opt': ' '}



print "{canopy_cover} {canopy_param} {e_ratio} {temp} {resid_par} {gdd_em} {grazing_bio} {p_cut} {pct_canopy_sen} {p_diameter}".format(canopy_cover = p_dic['canopy_cover'], canopy_param = p_dic['canopy_param'], e_ratio = p_dic['e_ratio'], temp = p_dic['temp'], resid_par = p_dic['resid_par'], gdd_em = p_dic['gdd_em'], grazing_bio = p_dic['grazing_bio'], p_cut = p_dic['p_cut'], pct_canopy_sen = p_dic['pct_canopy_sen'], p_diameter = p_dic['p_diameter'])
print "{pct_to_max_lai} {pct_biomass_sen} {rad_coeff} {resid_adj} {dw_frict_fact} {gdd_season} {harvest} {canopy_max}".format(pct_to_max_lai = p_dic['pct_to_max_lai'], pct_biomass_sen = p_dic['pct_biomass_sen'], rad_coeff = p_dic['rad_coeff'], resid_adj = p_dic['resid_adj'], dw_frict_fact = p_dic['dw_frict_fact'], gdd_season = p_dic['gdd_season'], harvest = p_dic['harvest'], canopy_max = p_dic['canopy_max'])
print "{mfo_value}".format(mfo_value = p_dic['mfo_value'])
print "{decomp_above} {decomp_below} {temp_opt} {drought_tol} {p_space} {root_depth_max} {root_shoot} {root_mass_max} {sen_length} {temp_max_crit}".format(decomp_above = p_dic['decomp_above'], decomp_below = p_dic['decomp_below'], temp_opt = p_dic['temp_opt'], drought_tol = p_dic['drought_tol'], p_space = p_dic['p_space'], root_depth_max = p_dic['root_depth_max'], root_shoot = p_dic['root_shoot'], root_mass_max = p_dic['root_mass_max'], sen_length = p_dic['sen_length'], temp_max_crit = p_dic['temp_max_crit'])

# alternate method; less text
"{} {} {} {} {} {} {} {} {} {}".format(p_dic['canopy_cover'], p_dic['canopy_param'], p_dic['e_ratio'], p_dic['temp'], p_dic['resid_par'], p_dic['gdd_em'], p_dic['grazing_bio'], p_dic['p_cut'], p_dic['pct_canopy_sen'], p_dic['p_diameter'])
"{} {} {} {} {} {} {} {}".format(p_dic['pct_to_max_lai'], p_dic['pct_biomass_sen'], p_dic['rad_coeff'], p_dic['resid_adj'], p_dic['dw_frict_fact'], p_dic['gdd_season'], p_dic['harvest'], p_dic['canopy_max'])
"{}".format(p_dic['mfo_value'])
"{} {} {} {} {} {} {} {} {} {}".format(p_dic['decomp_above'], p_dic['decomp_below'], p_dic['temp_opt'], p_dic['drought_tol'], p_dic['p_space'], p_dic['root_depth_max'], p_dic['root_shoot'], p_dic['root_mass_max'], p_dic['sen_length'], p_dic['temp_max_crit'])
#





#`init

version = ' '
callable = ' '

description = ' '
source = ' '
comment = ' '
callable_plant = ' '
i_dic = {'lu': ' ', 'bd': ' ', 'cc_init': ' ', 'days_till': ' ', 'days_harv': ' ', 'frost_init': ' ', 'ir_cover_init': ' ', 
         'mgmt': ' ', 'rain_till': ' ', 'ridge_init': ' ', 'r_cover_init': ' ', 'rough_init': ' ', 'rill_space': ' ', 'r_type': ' ', 
         'snow_d': ' ', 'thaw_d': ' ', 'sec_till_d': ' ', 'pri_till_d': ' ', 'ir_width': ' ', 'root_init': ' ', 'res_sub': ' ', }



print "{lu} ".format(lu = i_dic['lu'])
print "{bd} {i_dic} {days_harv} {days_till} {frost_init} {ir_cover_init} ".format(bd = i_dic['bd'], cc_init = i_dic['cc_init'], days_till = i_dic['days_till'], days_harv = i_dic['days_harv'], frost_init = i_dic['frost_init'], ir_cover_init = i_dic['ir_cover_init'])
print "{mgmt} ".format(mgmt = i_dic['mgmt'])
print "{rain_till} {ridge_init} {r_cover_init} {rough_init} {rill_space} ".format(rain_till = i_dic['rain_till'], ridge_init = i_dic['ridge_init'], r_cover_init = i_dic['r_cover_init'], rough_init = i_dic['rough_init'], rill_space = i_dic['rill_space'])
print "{r_type} ".format(r_type = i_dic['r_type'])
print "{snow_d} {thaw_d} {sec_till_d} {pri_till_d} {ir_width} ".format(snow_d = i_dic['snow_d'], thaw_d = i_dic['thaw_d'], sec_till_d = i_dic['sec_till_d'], pri_till_d = i_dic['pri_till_d'], ir_width = i_dic['ir_width'])
print "{root_init} {res_sub} ".format(root_init = i_dic['root_init'], res_sub = i_dic['res_sub'])










# .prj file

# WEPP GIS project for Hill 81
#
Version = 98.6
Name = default
Comments {
Created by TOPAZ interface
}
Units = Metric
Landuse = 1
Length = 100
Profile {
   File = "default.slp"
}
Climate {
   File = "Arizona\BLACK RIVER PUMPS AZ.cli"
}
Soil {
   Breaks = 0
   default {
   Distance = 100
      File = "OFE3\mollic_eutroboralfs.sol"
}
}
Management {
   Breaks = 0
   default {
   Distance = 100
      File = "ManagementBurn\forest.rot"
}
}
RunOptions {
Version = 1
SoilLossOutputType = 1
SoilLossOutputFile = AutoName
PlotFile = AutoName
EventFile = AutoName
FinalSummaryFile = AutoName
SimulationYears = 1
SmallEventByPass = 1
}"""




'''







