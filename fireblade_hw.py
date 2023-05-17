# Fireblade Hardware Information Processor

from jnpr.junos import Device

# virtual-chassis type
def chassis_type(dev):

    # get hardware info
    hostname = dev.facts['hostname']
    model_info = dev.facts['model_info']

    models = set(model_info.values())

    if len(models) == 1:
        chassis_type = models.pop()
    else:
        chassis_type = 'mixed'
    
    return chassis_type