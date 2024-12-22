import cv2 
import numpy as np
import matplotlib.pyplot as plt
import os 
from tqdm import tqdm

def read_image(filename, gray=False):
    im = cv2.imread(filename) 
    if gray: 
        im = gray(im)
    return cv2.cvtColor(im, cv2.COLOR_BGR2RGB) if im is not None else None

def show_images(col, row, images, titles=[], cmaps=[], scale=2):
    plt.figure(figsize=(row * scale, col * scale))
    titles = titles if titles else ["No Title" for i in range(len(images))]
    cmaps = cmaps if cmaps else [0 for i in images]
    for i in range(len(images)):
        plt.subplot(col, row, i + 1)
        if cmaps[i]: 
            plt.imshow(images[i])
        else:
            plt.imshow(images[i], cmap="gray")
        plt.title(titles[i])
        plt.axis("off")
    plt.tight_layout()
    plt.show()

# -----------------------------------------

def gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def negative(img):
    return 255 - img

def invert(img):
    return cv2.bitwise_not(img)

def threshold(img, thresh=0, maxval=255, type=cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU):
    _, bw_img = cv2.threshold(img, thresh, maxval, type=type)
    return bw_img

def dilate(img, kernel_size=3, iterations=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilated_img = cv2.dilate(img, kernel, anchor=(-1, -1), iterations=iterations)
    return dilated_img

def erode(img, kernel_size=3, iterations=4):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    erod_img = cv2.erode(img, kernel, anchor=(-1, -1), iterations=iterations)
    return erod_img

# -----------------------------------------

def process_image(img, effects, titles=[], verbose=True, col=1, row=-1, cmaps=[], img_scale=3):
    titles = ["Original"] if not titles else titles
    images = [img]
    prev_img = img  
    for index, effect in enumerate(effects):
        effect_name = effect[0]
        params = ["prev_img"] + effect[1:]
        params_literal = ", ".join(map(str, params)) 
        expression = f"{effect_name}({params_literal})"
        if len(titles) <= index+1 : 
            titles.append(expression)

        prev_img = eval(expression)
        images.append(prev_img)

    if verbose:
        row = round(len(images)/col) if row == -1 else row
        show_images(col, row, images, titles, scale=img_scale, cmaps=cmaps)
    
    return images

def  motion_blur_kernel(kernel_size = 3, angle = 0, standard=True):

    kernel = np.zeros((kernel_size, kernel_size))  # 開一個全黑畫布
    center = kernel_size // 2  # 計算核的中心位置

    cv2.line(kernel, (center, 0), (center, kernel_size - 1), 1, thickness=1)  # 在核中畫一條垂直的直線

    rotation_matrix = cv2.getRotationMatrix2D((center, center), angle, 1)  # 生成旋轉矩陣
    kernel = cv2.warpAffine(kernel, rotation_matrix, (kernel_size, kernel_size))  # 將旋轉矩陣應用到模糊核上
    if standard: 
        kernel /= kernel.sum()
    return kernel

def motion_blur(image, kernel_size, angle):

    kernel = np.zeros((kernel_size, kernel_size))  
    center = kernel_size // 2  # 計算核的中心位置
    cv2.line(kernel, (center, 0), (center, kernel_size - 1), 1, thickness=1)  # 在核中畫一條垂直的直線

    # 使用子圖顯示影像
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(kernel, cmap='gray')
    plt.title("Initial Kernel (Line)")
    plt.axis('off')


    # 旋轉模糊核
    rotation_matrix = cv2.getRotationMatrix2D((center, center), angle, 1)  # 生成旋轉矩陣
    kernel = cv2.warpAffine(kernel, rotation_matrix, (kernel_size, kernel_size))  # 將旋轉矩陣應用到模糊核上

    # 標準化模糊核
    kernel /= kernel.sum()

    # 對影像進行濾波
    blurred = cv2.filter2D(image, -1, kernel)

    plt.subplot(1, 3, 2)
    plt.imshow(kernel, cmap='gray')
    plt.title("Rotated Kernel")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(blurred)
    plt.title("Blurred Image")
    plt.axis('off')

    plt.show()

    return blurred, kernel

def wiener_filter(image, kernel, K=0.01, verbose=True):

    result = np.zeros_like(image)
    plt.figure(figsize=(12, 8))

    def process_gray_image():
        kernel_padded = np.pad(kernel, [(0, image.shape[0] - kernel.shape[0]), 
                                         (0, image.shape[1] - kernel.shape[1])], 
                                  mode='constant')
        kernel_fft = np.fft.fft2(kernel_padded)
        image_fft = np.fft.fft2(image)
        kernel_conj = np.conj(kernel_fft)
        wiener_result = (kernel_conj / (np.abs(kernel_fft)**2 + K)) * image_fft
        return np.abs(np.fft.ifft2(wiener_result)), kernel_fft, image_fft

    def display_gray_images(kernel_fft, image_fft, restored_image):
        plt.subplot(2, 3, 1)
        plt.imshow(kernel, cmap='gray')
        plt.title("Kernel")
        plt.axis('off')

        plt.subplot(2, 3, 2)
        plt.imshow(image, cmap='gray')
        plt.title("Blurred Image")
        plt.axis('off')

        plt.subplot(2, 3, 3)
        plt.imshow(np.log(1 + np.abs(image_fft)), cmap='gray')
        plt.title("FFT of Blurred Image")
        plt.axis('off')

        plt.subplot(2, 3, 4)
        plt.imshow(np.log(1 + np.abs(np.fft.fft2(image))), cmap='gray')
        plt.title("FFT of Original Image")
        plt.axis('off')

        plt.subplot(2, 3, 5)
        plt.imshow(np.abs(kernel_fft), cmap='gray')
        plt.title("FFT of Kernel")
        plt.axis('off')

        plt.subplot(2, 3, 6)
        plt.imshow(restored_image, cmap='gray')
        plt.title("Restored Image")
        plt.axis('off')

    if len(image.shape) == 2:  # 灰階影像
        restored_image, kernel_fft, image_fft = process_gray_image()
        if verbose:
            display_gray_images(kernel_fft, image_fft, restored_image)

    else:  # 彩色影像
        for i in range(image.shape[2]):  # 對每個通道處理
            channel = image[:, :, i]
            kernel_padded = np.pad(kernel, [(0, channel.shape[0] - kernel.shape[0]), 
                                             (0, channel.shape[1] - kernel.shape[1])], 
                                      mode='constant')
            kernel_fft = np.fft.fft2(kernel_padded)
            channel_fft = np.fft.fft2(channel)
            kernel_conj = np.conj(kernel_fft)
            wiener_result = (kernel_conj / (np.abs(kernel_fft)**2 + K)) * channel_fft
            result[:, :, i] = np.abs(np.fft.ifft2(wiener_result))

        if verbose:
            for i in range(image.shape[2]):
                plt.subplot(4, 3, i + 1)
                plt.imshow(image[:, :, i])
                plt.title(f"Blurred Image Channel {i+1}")
                plt.axis('off')

                plt.subplot(4, 3, i + 4)
                plt.imshow(np.log(1 + np.abs(np.fft.fftshift(np.fft.fft2(image[:, :, i])))), cmap='gray')
                plt.title(f"FFT of Blurred Image Channel {i+1}")
                plt.axis('off')

                plt.subplot(4, 3, i + 7)
                plt.imshow(result[:, :, i])
                plt.title(f"Restored Image Channel {i+1}")

                plt.subplot(4, 3, i + 10)
                plt.imshow(np.log(1 + np.abs(np.fft.fftshift(np.fft.fft2(result[:, :, i])))), cmap='gray')
                plt.title(f"FFT of Restored Image Channel {i+1}")
                plt.axis('off')

    plt.tight_layout()
    plt.show()
    return result

# -----------------------------------------

import cv2

def mean_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

def median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

def gaussian_filter(image, kernel_size=3, sigma=1):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

def histogram_equalization(image):
    if len(image.shape) == 3:  # 彩色影像

        yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb) 
        yuv_image[:, :, 0] = cv2.equalizeHist(yuv_image[:, :, 0])
        return cv2.cvtColor(yuv_image, cv2.COLOR_YCrCb2BGR)
    else:  # 灰度影像
        return cv2.equalizeHist(image)

def center_shift(frequency_spectrum):
    """ 將頻譜的低頻移動到中心 """
    return np.fft.fftshift(frequency_spectrum)


def add(img, val):
    return cv2.add(img, np.array([val, val, val]))

def adjust(img, contrast = 1, brightness = 0, saturation = 1):
    img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
    
    # Convert to HSV color space to adjust saturation
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * saturation, 0, 255)  # Adjust saturation channel
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return img

#------------------------------------------------------
import cv2
import numpy as np
import matplotlib.pyplot as plt

def notch_reject_filter(shape, d0=9, x=0, y=0, verbose=True):
    P, Q, C = shape
    H = np.ones((P, Q, 3))  # 初始化為全通濾波器 (值為1) for each color channel

    # 將座標轉換到頻譜中心
    x_c = x - Q / 2
    y_c = y - P / 2
    if verbose:
        print(f"\td0 = {d0:<5} x = {x:<5} y = {y:<5}")
        print(f"\td0 = {d0:<5} x = {round(Q/2 - x_c):<5} y = {round(P/2 - y_c):<5} (Conjugation)")

    # 針對頻譜每個點計算距離，決定是否濾波
    for v in range(P):
        for u in range(Q):
            # 計算距離 (針對目標頻率點和對稱頻率點)
            u_c = u - Q / 2 
            v_c = v - P / 2
            D_uv = np.sqrt((u_c + x_c) ** 2 + (v_c + y_c) ** 2)
            D_muv = np.sqrt((u_c - x_c) ** 2 + (v_c - y_c) ** 2)

            # 如果在半徑範圍內，設為0 (濾波區域)
            if D_uv <= d0 or D_muv <= d0:
                H[v, u, :] = 0.0  # Set all color channels to 0
    return H

def is_overlay(d0, x, y, notch_p):
    for (prev_d0, prev_x, prev_y) in notch_p:
        D_uv = np.sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
        if D_uv < d0:  # Check if the distance is less than the notch radius
            return True
    return False



def apply_notch_filters(img, notch_p, verbose=True, auto=False, threshold=250, auto_d0=30):
    
    print("hello 1")
    img_shape = img.shape
    channels = img_shape[2] if len(img_shape) == 3 else 1  # Check if image has multiple channels
    NotchFilter = np.ones(img_shape)  # Initialize NotchFilter for multiplication
    
    if auto:
        auto_notch_p = []
        magnitude_spectrum = np.log10(1 + np.abs(np.fft.fftshift(np.fft.fft2(img[:, :, 0]))))

        for u in range(magnitude_spectrum.shape[0]//2 - 10):
            for v in range(magnitude_spectrum.shape[1]):
                spectrum_value = magnitude_spectrum[u][v]
                d0 = auto_d0 + (100*(spectrum_value-threshold))
                if (spectrum_value > threshold).any() and (v < 400 or v > 600) \
                    and (u < 300 or v > 450) and not is_overlay(d0*1.2, v, u, auto_notch_p):
                    print(f"value:{spectrum_value}, d0 = {d0}")
                    auto_notch_p.append((d0, v, u))  

        notch_p = auto_notch_p  

    print(len(notch_p))
    print(notch_p)

    for index, (d0, x, y) in (enumerate(notch_p)):
        print(f"\nNotch Filters ({index+1}): ")
        mask = notch_reject_filter(img_shape, d0=d0, x=x, y=y)
        NotchFilter = (NotchFilter * mask) if index else mask

    result = np.zeros_like(img)  # Initialize result array

    for c in range(channels):
        f = np.fft.fft2(img[:, :, c])  # Compute Fourier transform for each channel
        fshift = np.fft.fftshift(f)  # Shift zero frequency component to the center
        NotchRejectCenter = fshift * NotchFilter[:, :, c]  # Apply notch filter for each channel
        NotchReject = np.fft.ifftshift(NotchRejectCenter)  # Inverse shift
        inverse_NotchReject = np.fft.ifft2(NotchReject)  # Inverse Fourier transform
        result[:, :, c] = np.abs(inverse_NotchReject)  # Store the result for each channel
    
    # Normalize result to the range [0, 255] for display
    result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    def show_results():
        c, r = channels, 2  # Adjusted for number of channels
        plt.figure(figsize=(c*3, r*3))

        plt.subplot(c, r, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Original Image')
        plt.axis('off')

        for i in range(channels):
            plt.subplot(c, r, i + 2)
            magnitude_spectrum = np.log10(1 + np.abs(np.fft.fftshift(np.fft.fft2(img[:, :, i]))))
            plt.imshow(magnitude_spectrum, cmap='gray')  # Show each channel of the magnitude spectrum
            plt.title(f'Magnitude Spectrum (Channel {i + 1})')

        plt.subplot(c, r, c + 2)
        plt.imshow(result, cmap="gray")
        plt.title("Filtered Image (Result)")

        plt.subplot(c, r, c + 3)
        plt.imshow(magnitude_spectrum * NotchFilter[:, :, 0], cmap="gray")  # Use one channel for display
        plt.title("Notch Reject Filter")
        plt.tight_layout()
        plt.show()

    if verbose:
        show_results()

    return result


# -----------------------------------------

def apply_sobel(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape

    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

    output = np.zeros((output_height, output_width))

    for i in range(output_height):
        for j in range(output_width):
            output[i, j] = np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel).clip(0, 255)

    return output

def show_sobel_result(image, show_edge_xy=False):
    # 讀取圖像

    # 如果是彩色圖像，轉換成灰度圖
    if image.ndim == 3:
        image = image.mean(axis=2)

    # 定義Sobel核
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # 應用Sobel核
    edge_x = apply_sobel(image, sobel_x)
    edge_y = apply_sobel(image, sobel_y)

    # 計算梯度幅度
    magnitude = np.sqrt(edge_x**2 + edge_y**2).clip(0, 255)
    print(magnitude.max())

    # 顯示結果
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(magnitude, cmap='gray'), plt.title('Sobel Edge Detection')
    plt.show()

    if show_edge_xy:

        # 顯示結果
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1), plt.imshow(edge_x**2, cmap='gray'), plt.title('edge_x')
        plt.subplot(1, 2, 2), plt.imshow(edge_y**2, cmap='gray'), plt.title('edge_y')
        plt.show()
