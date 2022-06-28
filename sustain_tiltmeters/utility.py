import numpy as np


def integrate_by_frequency(
    x: np.ndarray, dt: float, fmin: float = None, fmax: float = None
) -> np.ndarray:
    """Integrate `x` in frequency space.

    Parameters
    ----------
    x : numpy.ndarray
        Time series array to integrate
    dt : float
        Time step of the data
    fmin : float, optional
        Low cut-off frequency
    fmax : float, optional
        High cut-off frequency

    Returns
    -------
    out : numpy.ndarray
        Integral of `x`
    """
    f = np.fft.fftfreq(x.size, dt)
    s = np.fft.fft(x)
    s[1:] /= 1j * 2 * np.pi * f[1:]
    if fmin:
        s[(f < fmin) & (f > -fmin)] = 0
    if fmax:
        s[(f > fmax) | (f < -fmax)] = 0
    return np.fft.ifft(s).real
