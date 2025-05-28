import imageio.v3 as iio

filenames = []

fileNameBase = ""

amount = 0

images = []





try:
    print("please make sure that the pictures you want to use follow the correct naming convention: name1.png")
    fileNameBase = input("What is the name of your photo? without the number and the .png " )
    amount = int(input(f"how many photos are there from which the name starts with {fileNameBase} "))
    outputName = input("as what would you like to save the created GIF? ")

    for number in range(1,amount+1):
        filenames.append(f"{fileNameBase}{number}.png")

    for filename in filenames:
   
        images.append(
            iio.imread(
               filename
            )
        )


    iio.imwrite(
        f'{outputName}.gif', 
        images, 
        duration = 500, 
        loop = 0
    )
except FileNotFoundError:
    print("this image does not exist!")

except ValueError:
    print("please only use numbers!")