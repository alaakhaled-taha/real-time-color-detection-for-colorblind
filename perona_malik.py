import numpy as np

# Coefficient function for Perona-Malik
def coefficient(I, k):
    return 1 / (1 + ((I / k) ** 2))

# Perona-Malik denoising function
def automated_perona_malik(image, iterations, tau=0.01):
    image = image / 255.0  # Normalize the image
    f = image.copy()
    new_image = np.zeros(image.shape, dtype=image.dtype)
    M, N = image.shape
    sigma1 = 0.01

    for t in range(iterations):
        I_North = image[:-2, 1:-1] - image[1:-1, 1:-1]
        I_South = image[2:, 1:-1] - image[1:-1, 1:-1]
        I_East = image[1:-1, 2:] - image[1:-1, 1:-1]
        I_West = image[1:-1, :-2] - image[1:-1, 1:-1]
        gradient_magnitude = np.sqrt(I_North**2 + I_South**2 + I_East**2 + I_West**2)

        k = 1 + 0.25 * gradient_magnitude
        divergence = (coefficient(I_North, k) * I_North +
                      coefficient(I_South, k) * I_South +
                      coefficient(I_East, k) * I_East +
                      coefficient(I_West, k) * I_West)

        lambda1 = np.sum(image - f) * divergence / (M * N * sigma1)
        new_image[1:-1, 1:-1] = image[1:-1, 1:-1] + tau * (
            divergence - lambda1 * (image[1:-1, 1:-1] - f[1:-1, 1:-1])
        )

        image = new_image.copy()

    return new_image
