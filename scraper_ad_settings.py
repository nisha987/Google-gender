import sys, os
##sys.path.append("../core")        # files from the core
import ads                          # interacting with Google ad settings

log_file = 'log.demo.txt'
site_file = 'male.txt'

def make_browser(unit_id, treatment_id):
    b = ads.GoogleAdsSettingsUnit(browser='firefox', log_file=log_file, unit_id=unit_id,treatment_id=treatment_id, headless=False, proxy = None)
    return b

# web.pre_experiment.alexa.collect_sites(make_browser, num_sites=5, output_file=site_file,
#     alexa_link="http://www.alexa.com/topsites")

# Control Group treatment
def control_treatment(unit):
    unit.create_user('male')
    unit.visit_sites(site_file,delay=5)
    #pass


def measurement(unit):
    unit.save_gender(log_file)


# Shuts down the browser once we are done with it.
def cleanup_browser(unit):
    unit.quit()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

