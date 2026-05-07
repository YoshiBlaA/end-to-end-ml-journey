"""
Create a function that receives named configuration parameters and returns a dictionary with
    default values for those who weren't specified.

Expected parameters: debug, timeout, retries, log_level
Examples: 
    configure(debug=True, timeout=30) → must complete remaining values
"""

def configure(**kwargs):
    keys = list(kwargs.keys())
    #print(keys)
    return {
                'debug': kwargs["debug"] if "debug" in keys else False,
                'timeout':  kwargs["timeout"] if "timeout" in keys else 10,
                'retries':  kwargs["retries"] if "retries" in keys else 3,
                'log_level':  kwargs["log_level"] if "log_level" in keys  else 30
        
            }
    
processor_configuration = configure(debug=True, timeout=30)
print(processor_configuration)