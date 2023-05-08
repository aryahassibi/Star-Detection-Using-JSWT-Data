![](/Notebooks/img/space_banner_graphic.png)

# Astrophysical Image Processing Using James Webb Space Telescope Obersvations
The aim of this project was to detect and count the number of stars in the [Pillars of Creation](https://www.nasa.gov/feature/goddard/2022/nasa-s-webb-takes-star-filled-portrait-of-pillars-of-creation) image captured by the James Webb Space Telescope ([JWST](https://webb.nasa.gov/)) on October 21st, 2022. The methods and algorithms used for this procedure are covered in the documentation of the project.

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter">
  &nbsp;
  <img src="https://img.shields.io/pypi/l/ansicolortags.svg" />
</p>

---

# People
## Team members
- Arya Hassibi ([LinkedIn](https://www.linkedin.com/in/aryahassibi/), [GitHub](https://github.com/aryahassibi))
- Milad Bafarassat ([LinkedIn](https://www.linkedin.com/in/miladbafarassat/), [GitHub](https://github.com/Miladbaf))
- Rasul Barak ([LinkedIn](https://www.linkedin.com/in/rasul-barak-548360227/), [GitHub](https://github.com/rasulbarak))
- Kourosh Sharifi ([LinkedIn](https://www.linkedin.com/in/kouroshsharifi/), [GitHub](https://github.com/KouroshKSH/))

At the time, all 4 members were sophomore computer science students (3rd semester) at Sabancı University, and completed this project for their PROJ 201 course.

## Supervisor
This project was supervised by Prof. [Ersin Göğüş](http://people.sabanciuniv.edu/ersing/) from [Sabancı University](https://www.sabanciuniv.edu/en).

---

# Tools
## Libraries
The list of libraries employed for this project:
- [Astropy](https://www.astropy.org/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Scikit-image](https://scikit-image.org/)
- [SciPy](https://scipy.org/)

---

# How to run
The majority of the code is in the [Notebook](https://github.com/KouroshKSH/Astrophysical-Image-Processing-Using-JWST/tree/main/Notebooks) folder. Once cloned or downloaded, simply run each cell in a sequential manner. Make sure that the `.fits` data sets are in the same directory as the Jupyter notebookes that you wish to run. They are:
1. `carine_nircam.fits` ([link](https://github.com/KouroshKSH/Astrophysical-Image-Processing-Using-JWST/blob/main/Notebooks/carina_nircam.fits))
2. `m16_nircam.fits` ([link](https://github.com/KouroshKSH/Astrophysical-Image-Processing-Using-JWST/blob/main/Notebooks/carina_nircam.fits))

For more information regarding this project, feel free to read the [project report](https://github.com/KouroshKSH/Astrophysical-Image-Processing-Using-JWST/blob/main/Project%20Report.pdf). The rest of this `README` file will be the content of the report.

---
---

# Project Report
## Abstract
The goal of this project was to use computational methods to analyze and process the quantitative data provided by the James Webb Space Telescope (JWST). Specifically, the team worked with images taken by the Near-Infrared Camera (NIRCam) instrument of the JWST. These images were unique due to the use of advanced electron absorption technology, which enabled the team to capture highly detailed infrared wavelength data with unparalleled precision. The project aimed to detect and count the stars in a specific region of the Milky Way Galaxy, called the Pillars of Creation. To accomplish this, various image processing techniques were employed. The rest of the report is dedicated to explain each phase of the project in more detail.

---

## Introduction
The James Webb Space telescope is a space observatory that is optimized for infrared wavelengths. This optimization for infrared wavelengths will enable scientists to go back further in time and see red-shifted light as well as inside nebulas, and other objects that are harder to observe with visible light spectrum. This information sheds light on the universe’s past, present, and future. To tackle this project, a team of four sophomore computer science students have set out to find the answer to the question below:
> “How to count the number of stars in a specific region of an image taken by James Webb Space Telescope (JWST), and to categorize them based on their mass and temperature, in order to compare these findings with other academic literature for different galaxies”

To be able to record and measure these wavelengths, Webb uses the previously mentioned instruments in specific conditions. All instruments are kept cold at temperatures below 54 Kelvin, with MIRI being kept at only 7K, to reduce the unwanted noise from the instruments as much as possible. Thereafter, the light gets reflected back to the secondary mirror by the 18 primary mirrors that are precisely positioned relative to each other, which are coated with a layer of gold to maximize the reflection of infrared light. The primary goal of the JWST is to study galaxy, star, and planet formations. The JWST has a total of 4 instruments in the ISIM. Each of these instruments are specialized for a specific set of tasks. For instance, NIRCam is Webb’s primary camera, which covers the infrared wavelength range from 0.6 - 5.0 micrometers. NIRCam’s data, and its analysis, are the primary subjects of this group project. NIRCam uses its near-IR HgCdTe detector to start its electron sensing process. Meanwhile, a semiconductor absorbs an incoming photon, which generates mobile electron hole pairs. These electrons travel under the influence of pre-built and applied electric fields until they find their way to where they can be collected.

---

## Methods & Materials
A wide variety of tools were employed to develop this project. Namely:
- Python 3.8: As the main programming language
- Astropy: For acquiring, reading and employing FIST data
- NumPy: For applying mathematical function to the data
- Matplotlib: For visualizing the data using graphs and charts
- SciPy: For optimizing part of the code concerned with computation
- Mikulski Archive for Space Telescopes: To acquire FITS data
- OpenCV: For image manipulation, algorithm implementation and image generation
- ScikitLearn: For linear regression

The algorithms utilized were many, including:
- Canny Edge Detection
- Median Blurring
- Otsu Thresholding

More information can be found in the upcoming pages, regarding algorithms used, a broad description of each, their use-case, why they were used, and what was obtained by implementing them in the code. As for a brief description on the whole process:
1. The required data was collected from an archive.
2. The downloaded data was processed.
3. A number of statistics were obtained after the modifications.
4. Conclusions were made after visualizing and reasoning the data

---

## Data Collection
### Source
The first step was to obtain the information about the m16 region (also known as the Pillars of Creation) via Flexible Image Transport System (FITS) from the Mikulski Archive for Space Telescopes (MAST). By specifying the desired space telescope as James Webb, the portal then displayed the necessary parameters to choose and filter the data.

As for the camera, the Near Infrared Camera (NIRCam) was chosen as the observer. Thereafter, the file was downloaded, unzipped and then stored with the Jupyter notebook at hand. For the sake of learning, some sample runs were conducted to understand the content of the dataset, and how to visualize the data.

### Python Library
After that, the team began to construct the first part of the program using the Astropy library. This library is a collection of software packages for astronomy and astrophysics. It provides a wide range of tools and functions for working with astronomical data, including functions for reading and writing data files, handling celestial coordinates, performing photometry and spectroscopy, and much more.

---

## Background Estimation
### Gaussian Distribution
### Median Blur

---

## Otsu Method
## Canny Edge Detection
## Rectangle Detection (OpenCV)
### Plotting Intensity per Pixel

---

## Plotting the Data
### Normal Scale
### Log Scale
### 3D

---

## Comparison Using Anderson-Darling Test

---

## Regression & Best-fit Curve
### Linear Regression
### Power Law Trend

---

## Results
## Initial Hypothesis
## Discussion & Conclusion
