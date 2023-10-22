

1.(a) **Smoothing Kernel:**
A smoothing kernel is used for blurring or smoothing an image by reducing its noise and details. A common example is the Gaussian Kernel. A 3x3 Gaussian kernel might look like this:

\[\frac{1}{16} \begin{pmatrix}1 & 2 & 1 \\2 & 4 & 2 \\1 & 2 & 1\end{pmatrix}\]



1.(b) **Sharpening Kernel:**
A sharpening kernel is used to enhance the edges within an image. One commonly used sharpening kernel is the Laplacian kernel. A 3x3 Laplacian kernel can be represented as:

\[
\begin{pmatrix}
0 & -1 & 0 \\
-1 & 5 & -1 \\
0 & -1 & 0
\end{pmatrix}
\]

2. **ANMS Algorithm:**
ANMS (Adaptive Non-Maximal Suppression) algorithm is utilized to select a subset of interest points that are distributed as uniformly as possible over the image domain. In essence, it's a technique to ensure that the selected points are not clustered in one region of the image but are spread out evenly.

3. **GMM and Color Class Prior:**
In Gaussian Mixture Model (GMM) for image thresholding, a common choice for the prior distribution of a color class could be a Dirichlet distribution. The Dirichlet distribution is a conjugate prior of the multinomial distribution and can be useful in this context to model the probability of a pixel belonging to a particular color class.

 
4. **Role of RANSAC in Estimating Homography in Project 2**:
   In many projects, the role of RANSAC (Random Sample Consensus) is to robustly estimate the homography matrix from point correspondences between two images while mitigating the effects of outliers. It iteratively selects random subsets of correspondences to compute candidate homographies, evaluates the fit of these homographies over all correspondences, and keeps the best-fitting homography. This process leads to a robust estimation of the homography matrix, enabling accurate alignment or stitching of images in tasks such as panorama creation.

5. **Differences Between Affine and Projective Transforms**:
   - **Parallelism Preservation**:
     - Affine Transform: Preserves parallelism of lines from the source to the target coordinate space. This means that lines that are parallel in the original space remain parallel in the transformed space.
     - Projective Transform (Homography): Does not preserve parallelism. Lines that are parallel in the original space may converge or diverge in the transformed space.
   
   - **Coordinate Representation**:
     - Affine Transform: Typically represented in Cartesian coordinates and does not handle points at infinity.
     - Projective Transform (Homography): Represented in homogeneous coordinates, allowing for the representation and transformation of points at infinity.

   These fundamental differences illustrate how affine and projective transforms relate to geometric properties and the representation of space in image processing and computer vision tasks.


   6. **Principal Point and K Matrix**:
    The principal point coordinates (\(c_x, c_y\)) in the camera calibration matrix \(K\) typically correspond to the image center. If the captured image size is \( (I_x, I_y) \), then usually \(c_x = I_x/2\) and \(c_y = I_y/2\). In matrix form, \(K\) would look like:

\[
K = \begin{pmatrix}
f_x & s & c_x \\
0 & f_y & c_y \\
0 & 0 & 1
\end{pmatrix}
\]

7. **Gaussian Filters Before Edge Detection**:
    Applying Gaussian filters before edge and corner detection helps in reducing noise and smoothing out the image. This makes the subsequent edge/corner detection more reliable, as it reduces the likelihood of detecting false positives caused by noise or minor texture variations.

8. **Vanishing Points in Orthographic Projections**:
    Vanishing points do not exist in orthographic projections as parallel lines remain parallel and do not converge. In Perspective Projection, vanishing points exist as parallel lines appear to converge at a point in the distance due to perspective effects.

9. **Choice in SIFT Before Subsampling**:
    (b) Image Blurring is chosen before subsampling in Scale-Invariant Feature Transform (SIFT) to reduce noise and to ensure that features are scale invariant.

10. **Field of View with Different Sensor Sizes**:
     The larger sensor (35 mm × 35 mm) will provide a larger field of view compared to the smaller sensor (24 mm × 24 mm), given the same focal length lens is used on both.

11. **Brightness Conservation in Optical Flow Computation**:
     True. The brightness constancy assumption is a fundamental premise in optical flow computation. It assumes that the brightness (intensity) of a particular pixel remains consistent between consecutive frames, which aids in determining the motion of that pixel over time.
