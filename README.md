# Topology optimization for waveguide bandwidth maximization
The FEM code uses rectangular vector edge elements [1] to solve the Helmholtz equation in the form of eigenvalue problem 

$ \begin{bmatrix}
A_{tt} & 0 \\
0 & 0 
\end{bmatrix} 
\begin{Bmatrix}
e_{t} \\
e_z
\end{Bmatrix}  = -k_z^2
\begin{bmatrix}
B_{tt} & B_{tz} \\
B_{zy} & B_{zz} 
\end{bmatrix} 
\begin{Bmatrix}
e_{t} \\
e_z
\end{Bmatrix}$

For more details about the operators see [1] pg.290.

In the FEM code a linear interpolation of effective dielectric permittivity is assumed

$\epsilon_\mathrm{r} (x) = \epsilon_\mathrm{r, bck} + x(\epsilon_\mathrm{r, met} - \epsilon_\mathrm{r, bck})$,

where $\epsilon_\mathrm{r, met} = 10000^2$ and $\epsilon_\mathrm{r, bck} = 1.0003^2$. At the start we compare the mode cutoff frequencies calculated from the propagation wavelength as

$f_c = \frac{c\sqrt{1-(\frac{\lambda}{\lambda_\mathrm{g}})^2}}{\lambda}$, where $c$ stands for the speed of light in vacuum, $\lambda_\mathrm{g}$ is the propagation wavelength and is related to the eigenvalues as $\kappa = -k_z^2$, where $\kappa$ is the eigenvalue and $\lambda$ is the wavelength of the wave traveling in an unbounded medium whose electrical parameters $\epsilon$ and $\mu$ are the same as those of the medium inside the waveguide [2].

## References

[1] Jianming Jin. 2014. The Finite Element Method in Electromagnetics (3rd. ed.). Wiley-IEEE Press.

[2] Constantine A. Balanis. 2012. Advanced Engineering Electromagnetics. Wiley.