import numpy as np

class phy:
    " Class that defines the physics of the model."

    def __init__( self,
                 eps_metal,
                 eps_back,
                 mu,
                 scale,
                 wavelength,
                 alpha = 0.0):
        """
        @ n_metal : Value for the refractive index of the metal.
        @ k_r : Value for the exctinction coefficient of the metal.
        @ n_metal: Value for the refractive index of the waveguide.
        @ n_back: Value for the refractive index of the cladding.
        @ scale: scale of the physical problem; i.e. 1e-9 for nm.
        @ wavelength: Wavelength of the problem (Frequency domain solver).
        """

        # ------------------------------------------------------------------
        # ELECTROMAGNETICS 
        # ------------------------------------------------------------------

        self.eps_metal = eps_metal
        self.eps_back = eps_back

        self.mu = mu
        self.scale = scale
        self.wavelength = wavelength
        self.k = 2 * np.pi / (self.wavelength * self.scale)

        self.eps_0 = 8.85e-12
        self.mu_0 = 1.257e-6
        self.c = 3e8
        self.Z0 = np.sqrt(self.mu_0/self.eps_0)
        self.alpha = alpha

