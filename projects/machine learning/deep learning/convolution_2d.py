import numpy as np
image = np.random.random((3,5,5)) #generate 2d image data from [0, 1)

#used for fastfowarding of convolution neural network
def conv2d(image, filter_levels, filter_size, padding, stride):
    #setting up the dimensions
    image_channel, image_height, image_width = image.shape[0], image.shape[1], image.shape[2]
    #filter for each image channel
    filter_channel, filter_height, filter_width = image_channel, filter_size[0], filter_size[1]
    filter = np.random.random((filter_channel, filter_height, filter_width))
    #output construction
    output_height = int(((image_height - filter_height + 2 * padding) / stride) + 1)
    output_width = int(((image_width - filter_width + 2 * padding) / stride) + 1)
    #number of output_channel is equal to filter_number since each filter layer will give out outputs
    output_channel = filter_levels
    #set output shape by zero at first
    output = np.zeros((output_channel, output_height, output_width))
    #padding fuction for the input image 
    if padding != 0:
        #padded added
        padded_image = np.zeros((image_channel, image_height + 2 * padding, image_width + 2 * padding ))
        #use negative index to put image in the padded zeros
        padded_image[:, padding:(-1 * padding), padding:(-1 * padding)] = image 
    #user report of padded
        print('='*50)
        print('padded_image')
        print(f'padded_image shape : {padded_image.shape}')
        print(padded_image)
    else: 
        padded_image = image
    #cross correlation operation for 2d image 
    for z in range(0, output_channel):
        #setting outputs with zeros first for each filter
        output_per_filter = np.zeros((output_height, output_width))
        #croess correlation operation done with stride applied 
        for y in range(0, output_height):
            #each start of the operation starts at y * stride
            #the final start of the operation which is the size of filter always must be lesser than padded_image_height
            if (y * stride + filter_height) <= padded_image.shape[1]:
                for x in range(0, output_width):
                    #each start starts at x * stride 
                    #the final start must be lesser than the padded_image-width
                    if (x * stride + filter_width) <= padded_image.shape[2]:
                        #summing of cross correlation operation after multiplying it with filter, 3d multiplication used for multiple filters 
                        output_per_filter[y][x] = np.sum(padded_image[:, y * stride: y * stride + filter_height, x * stride : x * stride + filter_width] * filter)
        output[z, :, :] = output_per_filter
    #user reporting of output
    print('='*50)
    print('output')
    print(f'output shape : {output.shape}')
    print(output)
    print('='*50)
    return output 

conv2d(image, 1, (4,4), padding = 0, stride = 1)
