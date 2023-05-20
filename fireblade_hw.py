# Fireblade Hardware Information Processor

from jnpr.junos import Device

# get hardware info
def hw_dict(dev):
    return dev.facts

# chassis type for JUNOS installation purpose
def chassis(dev):

    model_info = hw_dict(dev)['model_info']

    models = set(model_info.values())

    if len(models) == 1:
        chassis = models.pop()
    else:
        chassis = 'mixed'
    
    return chassis

# routing engine model
def model(dev):
    return hw_dict(dev)['model']

# chassis role
def role(dev):
    h = hw_dict(dev)['hostname'].lower()
    r = 'edge' if h.find('edge') != -1 else 'core' if h.find('core') != -1 else 'ext' if h.find('ext') != -1 else None
    return r

# campus info
def campus(dev):
    h = hw_dict(dev)['hostname'].lower()
    campus = h.split('-')[0]
    return campus

# building info
def bld(dev):
    h = hw_dict(dev)['hostname'].lower()
    bld = h.split('-')[1]