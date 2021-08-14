# this program runs the optimizer model, and ensures that all the results are 
# reasonable using a couple useful checks to make sure there's nothing wacky 
# going on.

#check that as time increases, more people can be fed

#check that stored food plus meat is always used at the 
#highest rate during the largest food shortage.

import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
	sys.path.append(module_path)
from src.optimizer import Optimizer

constants = {}
constants['inputs'] = {}

constants['inputs']['NMONTHS'] = 24
constants['inputs']['LIMIT_SEAWEED_AS_PERCENT_KCALS'] = True

constants['inputs']['ASSUMED_WASTE_PERCENT'] = 35
constants['inputs']['ASSUMED_WASTE_PERCENT_M1'] = 35
constants['inputs']['ASSUMED_WASTE_PERCENT_AFTER_M1'] = 30
# constants['inputs']['ALL_BIOFUEL'] = 22e6#tons dry caloric equivalent
constants['inputs']['M1_ADDITIONAL_WASTE'] = 5e9/12#tons dry caloric equivalent
# constants['inputs']['KCALS_DAILY'] = 2100#(1800+2700)/2 #kcals per person per day
# constants['inputs']['FAT_DAILY'] = (35+70)/2 #grams per person per day
# constants['inputs']['PROTEIN_DAILY'] = (51+78.75)/2 #grams per person per day

constants['inputs']['KCALS_DAILY'] = 2100 #kcals per person per day
constants['inputs']['FAT_DAILY'] = 35 #grams per person per day
constants['inputs']['PROTEIN_DAILY'] = 51 #grams per person per day

constants['inputs']['INITIAL_MILK_COWS'] = 264e6
constants['inputs']['MAX_SEAWEED_AS_PERCENT_KCALS'] = 30
constants['inputs']['INIT_SMALL_ANIMALS'] = 28.2e9
constants['inputs']['INIT_MEDIUM_ANIMALS'] = 3.2e9
constants['inputs']['INIT_LARGE_ANIMALS'] = 1.9e9
constants['inputs']['HARVEST_LOSS'] = 15 # percent (seaweed)
constants['inputs']['INITIAL_SEAWEED'] = 1 # 1000 tons (seaweed)
constants['inputs']['INITIAL_AREA'] = 1 # 1000 tons (seaweed)
constants['inputs']['NEW_AREA_PER_DAY'] = 4.153 # 1000 km^2 (seaweed)
constants['inputs']['MINIMUM_DENSITY'] = 400 #tons/km^2 (seaweed)
constants['inputs']['MAXIMUM_DENSITY'] = 4000 #tons/km^2 (seaweed)
constants['inputs']['MAXIMUM_AREA'] = 1000 # 1000 km^2 (seaweed)
constants['inputs']['PRODUCTION_RATE'] = 10 # percent (seaweed)
constants['inputs']['TONS_DRY_CALORIC_EQIVALENT_SF'] = 1602542*1000.
constants['inputs']['INITIAL_SF_PROTEIN'] = 203607 #1000 tons protein per unit mass initial
constants['inputs']['INITIAL_SF_FAT'] = 63948 # 1000 tons fat per unit mass initial
constants['CHECK_CONSTRAINTS'] = False
constants['inputs']['RATIO_KCALS_POSTDISASTER_Y1'] = 0.4
constants['inputs']['RATIO_KCALS_POSTDISASTER_Y2'] = 0.2
constants['inputs']['RATIO_KCALS_POSTDISASTER_Y3'] = 0.2
constants['inputs']['RATIO_KCALS_POSTDISASTER_Y4'] = 0.2
optimizer = Optimizer()


constants['inputs']['ADD_FISH'] = False
constants['inputs']['ADD_SEAWEED'] = False
constants['inputs']['ADD_CELLULOSIC_SUGAR'] = False
constants['inputs']['ADD_GREENHOUSES'] = False
constants['inputs']['ADD_NONEGG_NONDAIRY_MEAT'] = False
constants['inputs']['ADD_DAIRY'] = False
constants['inputs']['ADD_STORED_FOOD'] = True
constants['inputs']['ADD_OUTDOOR_GROWING'] = False
max_fed=optimizer.optimize(constants)
print('max fed')
print(max_fed)
quit()

constants['inputs']['ADD_SEAWEED'] = False
constants['inputs']['ADD_CELLULOSIC_SUGAR'] = True
constants['inputs']['ADD_GREENHOUSES'] = True
constants['inputs']['ADD_NONEGG_NONDAIRY_MEAT'] = True
constants['inputs']['ADD_DAIRY'] = True
constants['inputs']['ADD_STORED_FOOD'] = True
constants['inputs']['ADD_OUTDOOR_GROWING'] = True

seaweed_omitted=optimizer.optimize(constants)
print('seaweed omitted')
print(seaweed_omitted-max_fed)


constants['inputs']['ADD_SEAWEED'] = True
constants['inputs']['ADD_CELLULOSIC_SUGAR'] = False
constants['inputs']['ADD_GREENHOUSES'] = True
constants['inputs']['ADD_NONEGG_NONDAIRY_MEAT'] = True
constants['inputs']['ADD_DAIRY'] = True
constants['inputs']['ADD_STORED_FOOD'] = True
constants['inputs']['ADD_OUTDOOR_GROWING'] = True
cell_sugar_omitted=optimizer.optimize(constants)
print('cellulosic sugar omitted')
print(cell_sugar_omitted-max_fed)


constants['inputs']['ADD_SEAWEED'] = True
constants['inputs']['ADD_CELLULOSIC_SUGAR'] = True
constants['inputs']['ADD_GREENHOUSES'] = False
constants['inputs']['ADD_NONEGG_NONDAIRY_MEAT'] = True
constants['inputs']['ADD_DAIRY'] = True
constants['inputs']['ADD_STORED_FOOD'] = True
constants['inputs']['ADD_OUTDOOR_GROWING'] = True
greenhouses_omitted=optimizer.optimize(constants)
print('greenhouses omitted')
print(greenhouses_omitted-max_fed)


constants['inputs']['ADD_SEAWEED'] = False
constants['inputs']['ADD_CELLULOSIC_SUGAR'] = False
constants['inputs']['ADD_GREENHOUSES'] = False
constants['inputs']['ADD_NONEGG_NONDAIRY_MEAT'] = True
constants['inputs']['ADD_DAIRY'] = True
constants['inputs']['ADD_STORED_FOOD'] = True
constants['inputs']['ADD_OUTDOOR_GROWING'] = True
no_intervention=optimizer.optimize(constants)
print('no intervention')
print(no_intervention)


constants['inputs']['ADD_SEAWEED'] = True
constants['inputs']['ADD_CELLULOSIC_SUGAR'] = False
constants['inputs']['ADD_GREENHOUSES'] = False
constants['inputs']['ADD_NONEGG_NONDAIRY_MEAT'] = True
constants['inputs']['ADD_DAIRY'] = True
constants['inputs']['ADD_STORED_FOOD'] = True
constants['inputs']['ADD_OUTDOOR_GROWING'] = True
just_seaweed=optimizer.optimize(constants)
print('just seaweed')
print(just_seaweed-no_intervention)


constants['inputs']['ADD_SEAWEED'] = False
constants['inputs']['ADD_CELLULOSIC_SUGAR'] = True
constants['inputs']['ADD_GREENHOUSES'] = False
constants['inputs']['ADD_NONEGG_NONDAIRY_MEAT'] = True
constants['inputs']['ADD_DAIRY'] = True
constants['inputs']['ADD_STORED_FOOD'] = True
constants['inputs']['ADD_OUTDOOR_GROWING'] = True
just_cell_sugar=optimizer.optimize(constants)
print('just CS')
print(just_cell_sugar-no_intervention)



constants['inputs']['ADD_SEAWEED'] = False
constants['inputs']['ADD_CELLULOSIC_SUGAR'] = False
constants['inputs']['ADD_GREENHOUSES'] = True
constants['inputs']['ADD_NONEGG_NONDAIRY_MEAT'] = True
constants['inputs']['ADD_DAIRY'] = True
constants['inputs']['ADD_STORED_FOOD'] = True
constants['inputs']['ADD_OUTDOOR_GROWING'] = True
just_greenhouses=optimizer.optimize(constants)
print('just Greenhouses')
print(just_greenhouses-no_intervention)
