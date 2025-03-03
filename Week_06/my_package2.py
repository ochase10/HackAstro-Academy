def redshift_calc(lam, lam0):
    '''
    Compute the redshift of an object given an emission line
    
    Inputs:
    lam: Observed line wavelength
    lam0: Laboratory line wavelength
    
    Returns:
    z: The redshift of a source for which the lab line (lam0) is 
        observed at the given wavelength (lam)
    '''
    return (lam-lam0)/lam0

print("Hi")