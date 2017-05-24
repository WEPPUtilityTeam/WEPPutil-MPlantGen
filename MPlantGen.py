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







